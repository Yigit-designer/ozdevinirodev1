class TuringMachine:
    def __init__(self, tape_str, transition_function, initial_state, accept_state, reject_state):
        self.tape = list(tape_str)
        self.head_position = 0
        self.transition_function = transition_function
        self.current_state = initial_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.step_count = 0

    def _ensure_tape_length(self):
        """Bantın, kafa pozisyonunun dışına çıkmamasını sağlar."""
        while self.head_position < 0:
            self.tape.insert(0, '_')
            self.head_position += 1
        while self.head_position >= len(self.tape):
            self.tape.append('_')

    def step(self):
        """Turing makinesinin bir adımını çalıştırır."""
        if self.current_state in [self.accept_state, self.reject_state]:
            return False

        self._ensure_tape_length()
        
        read_symbol = self.tape[self.head_position]
        
        action = self.transition_function(self.current_state, read_symbol, self)

        if action is None:
            # Eğer mevcut durum ve okunan sembol için bir kural yoksa, reddet.
            print(f"Geçiş bulunamadı: Durum='{self.current_state}', Okunan='{read_symbol}'. Reddediliyor.")
            self.current_state = self.reject_state
            return False
        write_symbol, move, next_state = action

        print(f"Adım {self.step_count + 1}:")
        print(f"  Durum : {self.current_state}")
        print(f"  Okunan: {read_symbol}")
        print(f"  Yazılan: {write_symbol}")
        
        self.tape[self.head_position] = write_symbol
        
        if move == 'R':
            self.head_position += 1
            print("  Hareket: R")
        elif move == 'L':
            self.head_position -= 1
            print("  Hareket: L")
        
        self.current_state = next_state
        print(f"  Yeni Durum: {self.current_state}")
        tape_str = "".join(self.tape)
        head_str = " " * self.head_position + "^"
        print(f"  Bant: {tape_str}")
        print(f"       {head_str}\n")

        self.step_count += 1
        return True

    def run(self):
        """Makine kabul veya red durumuna ulaşana kadar çalışır."""
        while self.step():
            pass
        
        print("="*30)
        if self.current_state == self.accept_state:
            print("Islem basariyla tamamlandi (Kabul Durumu).")
        else:
            print("Islem bir hatayla durdu (Red Durumu).")
        print("="*30)

    def get_result(self):
        """'=' karakterinden sonraki sonucu döndürür."""
        try:
            equal_pos = self.tape.index('=')
            result_tape = self.tape[equal_pos + 1:]
            # Baştaki ve sondaki boşlukları temizle
            result_str = "".join(result_tape).strip('_')
            return result_str if result_str else "0"
        except ValueError:
            return "Sonuç bulunamadı."

class BinaryMultiplierProgram:
    def __init__(self, multiplicand_str, multiplier_str):
        self.multiplicand_str = multiplicand_str
        self.multiplier_str = multiplier_str
        self.multiplicand_val = int(multiplicand_str, 2) if multiplicand_str else 0
        self.multiplier_val = int(multiplier_str, 2) if multiplier_str else 0
        self.shift = 0
        self.result_val = 0
        self.need_add = False
        self.write_bits = "0"
        self.write_index = 0

    def _prepare_write_bits(self):
        self.write_bits = bin(self.result_val)[2:] if self.result_val != 0 else "0"
        self.write_index = 0

    def transition(self, state, symbol, tm):
        if state == "q0_scan_star":
            if symbol in {"_", "0", "1"}:
                return (symbol, "R", "q0_scan_star")
            if symbol == "*":
                return ("*", "R", "q1_scan_equal")
            return None

        if state == "q1_scan_equal":
            if symbol in {"0", "1", "X", "Y"}:
                return (symbol, "R", "q1_scan_equal")
            if symbol == "=":
                return ("=", "L", "q3_find_bit")
            return None

        if state == "q3_find_bit":
            if symbol in {"X", "Y"}:
                return (symbol, "L", "q3_find_bit")
            if symbol == "0":
                self.need_add = False
                self.shift += 1
                return ("X", "R", "q4_move_to_equal")
            if symbol == "1":
                self.need_add = True
                self.result_val += (self.multiplicand_val << self.shift)
                self.shift += 1
                self._prepare_write_bits()
                return ("Y", "R", "q4_move_to_equal")
            if symbol == "*":
                return ("*", "R", "q9_cleanup")
            return None

        if state == "q4_move_to_equal":
            if symbol == "=":
                if self.need_add:
                    return ("=", "R", "q6_write_result")
                return ("=", "R", "q8_move_to_multiplier")
            return (symbol, "R", "q4_move_to_equal")

        if state == "q6_write_result":
            if self.write_index < len(self.write_bits):
                write_symbol = self.write_bits[self.write_index]
                self.write_index += 1
                return (write_symbol, "R", "q6_write_result")
            return (symbol, "R", "q7_clear_tail")

        if state == "q7_clear_tail":
            if symbol == "_":
                return ("_", "L", "q8_move_to_multiplier")
            return ("_", "R", "q7_clear_tail")

        if state == "q8_move_to_multiplier":
            if symbol == "=":
                return ("=", "L", "q3_find_bit")
            return (symbol, "L", "q8_move_to_multiplier")

        if state == "q9_cleanup":
            if symbol == "*":
                return ("*", "R", "q9_cleanup")
            if symbol == "X":
                return ("0", "R", "q9_cleanup")
            if symbol == "Y":
                return ("1", "R", "q9_cleanup")
            if symbol in {"0", "1"}:
                return (symbol, "R", "q9_cleanup")
            if symbol == "=":
                return ("=", "R", "q_finalize_result")
            if symbol == "_":
                return ("_", "L", "q_accept")
            return None

        if state == "q_finalize_result":
            if symbol == "_" and self.result_val == 0:
                return ("0", "L", "q_accept")
            if symbol in {"0", "1"}:
                return (symbol, "L", "q_accept")
            return (symbol, "L", "q_accept")

        return None

def validate_binary(s):
    """Verilen string'in sadece '0' ve '1' içerip içermediğini kontrol eder."""
    return all(c in '01' for c in s)

def main():
    while True:
        num1_str = input("1. ikili sayiyi girin (ornek: 1011): ").strip()
        if num1_str.endswith("="):
            num1_str = num1_str[:-1]
        if not num1_str:
            print("Hatali giris. Ilk sayi bos olamaz.")
            continue
        if not validate_binary(num1_str):
            print("Hatali giris. Sadece '0' ve '1' iceren sayilar girin.")
            continue

        num2_str = input("2. ikili sayiyi girin (ornek: 010): ").strip()
        if num2_str.endswith("="):
            num2_str = num2_str[:-1]
        if not num2_str:
            print("Hatali giris. Ikinci sayi bos olamaz.")
            continue
        if not validate_binary(num2_str):
            print("Hatali giris. Sadece '0' ve '1' iceren sayilar girin.")
            continue

        break

    # Bant formatını oluştur: _sayi1*sayi2=_
    # Baştaki ve sondaki boşluklar makinenin sınırları daha rahat yönetmesini sağlar.
    initial_tape_str = f"_{num1_str}*{num2_str}=_"
    
    program = BinaryMultiplierProgram(num1_str, num2_str)
    
    tm = TuringMachine(
        tape_str=initial_tape_str,
        transition_function=program.transition,
        initial_state='q0_scan_star',
        accept_state='q_accept',
        reject_state='q_reject'
    )
    
    tm.run()
    binary_result = tm.get_result()
    
    try:
        decimal_num1 = int(num1_str, 2)
        decimal_num2 = int(num2_str, 2)
        decimal_result = int(binary_result, 2)
        
        print("\n--- SONUÇ ---")
        print(f"Girdi (Binary) : {num1_str} * {num2_str}")
        print(f"Girdi (Decimal): {decimal_num1} * {decimal_num2}")
        print("-" * 15)
        print(f"Sonuç (Binary) : {binary_result}")
        print(f"Sonuç (Decimal): {decimal_result}")
        
        if decimal_num1 * decimal_num2 == decimal_result:
            print("\nDogrulama: Basarili.")
        else:
            print("\nDogrulama: Basarisiz.")

    except ValueError:
        print("Sonuç binary formata dönüştürülemedi.")

if __name__ == "__main__":
    main()
