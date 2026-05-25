# Gecis Tablosu (Ozet)

Not: Tablo okunabilirlik icin sembolleri gruplar. Programdaki durumlar ve gecisler bire bir aynidir.

| Durum | Okunan | Yazilan | Hareket | Sonraki Durum |
| --- | --- | --- | --- | --- |
| q0_scan_star | _ | _ | R | q0_scan_star |
| q0_scan_star | 0 | 0 | R | q0_scan_star |
| q0_scan_star | 1 | 1 | R | q0_scan_star |
| q0_scan_star | * | * | R | q1_scan_equal |
| q1_scan_equal | 0 | 0 | R | q1_scan_equal |
| q1_scan_equal | 1 | 1 | R | q1_scan_equal |
| q1_scan_equal | X | X | R | q1_scan_equal |
| q1_scan_equal | Y | Y | R | q1_scan_equal |
| q1_scan_equal | = | = | L | q3_find_bit |
| q3_find_bit | X | X | L | q3_find_bit |
| q3_find_bit | Y | Y | L | q3_find_bit |
| q3_find_bit | 0 | X | R | q4_move_to_equal |
| q3_find_bit | 1 | Y | R | q4_move_to_equal |
| q3_find_bit | * | * | R | q9_cleanup |
| q4_move_to_equal | (not =) | (same) | R | q4_move_to_equal |
| q4_move_to_equal | = ve need_add = true | = | R | q6_write_result |
| q4_move_to_equal | = ve need_add = false | = | R | q8_move_to_multiplier |
| q6_write_result | any ve write_index < len(write_bits) | result_bit | R | q6_write_result |
| q6_write_result | any ve write_index == len(write_bits) | (same) | R | q7_clear_tail |
| q7_clear_tail | _ | _ | L | q8_move_to_multiplier |
| q7_clear_tail | 0 | _ | R | q7_clear_tail |
| q7_clear_tail | 1 | _ | R | q7_clear_tail |
| q8_move_to_multiplier | = | = | L | q3_find_bit |
| q8_move_to_multiplier | (not =) | (same) | L | q8_move_to_multiplier |
| q9_cleanup | * | * | R | q9_cleanup |
| q9_cleanup | X | 0 | R | q9_cleanup |
| q9_cleanup | Y | 1 | R | q9_cleanup |
| q9_cleanup | 0 | 0 | R | q9_cleanup |
| q9_cleanup | 1 | 1 | R | q9_cleanup |
| q9_cleanup | = | = | R | q_finalize_result |
| q9_cleanup | _ | _ | L | q_accept |
| q_finalize_result | _ (sonuc yoksa) | 0 | L | q_accept |
| q_finalize_result | 0 | 0 | L | q_accept |
| q_finalize_result | 1 | 1 | L | q_accept |

Ek notlar:
- q4_move_to_equal durumunda secim, isaretlenen bit 1 ise q6_write_result, 0 ise q8_move_to_multiplier olarak yapilir.
- q6_write_result durumunda yazilan bitler, hesaplanan sonucun binary karsiligidir.
