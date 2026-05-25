# Proje Raporu: Turing Makinesi ile Binary Çarpma

## 1. Problem Tanımı
Bu projenin amacı, Python programlama dili kullanarak tek bantlı bir Turing Makinesi simülatörü geliştirmektir. Bu makine, ikili (binary) tabanda verilen iki sayıyı, işlemcilerin temel çalışma prensiplerinden biri olan "kaydır ve topla" (shift and add) yöntemiyle çarpacaktır. Simülasyon, sürecin her adımını detaylı olarak göstermelidir.

## 2. Turing Makinesi Modeli
Geliştirilen Turing Makinesi modeli aşağıdaki 7 bileşenden oluşur:
- **Q (Durum Kümesi):** Makinenin bulunabileceği tüm sonlu durumları içerir. (`q0_scan_star`, `q3_find_bit`, `q6_write_result`, `q_accept` vb.)
- **Σ (Giriş Alfabesi):** Bant üzerinde başlangıçta bulunabilen semboller. `{0, 1, *, =}`
- **Γ (Bant Alfabesi):** Bant üzerine yazılabilecek tüm semboller. `{0, 1, *, =, _, X, Y}`. `_` boşluk karakterini, `X, Y` ise işlem sırasında bitleri geçici olarak işaretlemek için kullanılan yardımcı sembollerdir.
- **δ (Geçiş Fonksiyonu):** `(Mevcut Durum, Okunan Sembol) -> (Yeni Durum, Yazılacak Sembol, Kafa Hareketi)` formatında kurallar tanımlar. Projenin kalbidir.
- **q₀ (Başlangıç Durumu):** Makinenin çalışmaya başladığı durum. (`q0_scan_star`)
- **B (Boşluk Sembolü):** Bantın sonsuz kısımlarını temsil eden sembol. (`_`)
- **F (Kabul Durumları):** İşlemin başarıyla bittiğini gösteren durumlar kümesi. (`q_accept`)

## 3. Operand Ayrıştırma Yaklaşımı (Zorunlu Gereksinim)
Bu projenin en kritik gereksinimi, bant üzerindeki iki operandın doğru bir şekilde ayırt edilmesidir. Bant `_sayı1*sayı2=_` formatında hazırlanır. Makine, bu yapıyı şu şekilde ayrıştırır:
1.  **`*` Karakterini Bulma:** Makine `q0_scan_star` durumunda başlar ve `*` karakterini bulana kadar sağa hareket eder. Bu, birinci sayının (multiplicand) sonunu ve ikinci sayının (multiplier) başlangıcını belirler.
2.  **`=` Karakterini Bulma:** Makine `*`'ı geçtikten sonra, `=` karakterini bulana kadar ilerler. Bu, ikinci sayının sonunu ve sonucun yazılacağı alanın başlangıcını belirler.
3.  **İşlem Döngüsü:** Makine, ikinci sayının bitlerini sağdan sola doğru okur. Her bit için, birinci sayıyı referans alarak işlem yapar. Bu süreç boyunca `*` ve `=` ayraçları konumlarını korur ve makinenin hangi bölgede (birinci sayı, ikinci sayı, sonuç) çalıştığını anlamasına yardımcı olur.

Bu yapı sayesinde makine, "sol taraf birinci sayı", "sağ taraf ikinci sayı" ayrımını net bir şekilde yapar ve işlem boyunca bu ayrımı korur.

## 4. Durumların ve Geçiş Mantığının Açıklaması
Makine, belirli bir görevi yerine getiren mantıksal durumlar arasında geçiş yaparak çalışır.

- **`q0_scan_star` (Başlangıç ve `*`'ı Bulma):** Bant üzerinde sağa giderek `*` karakterini arar.
- **`q1_scan_equal` (`=`'yi Bulma):** `*`'dan sonra sağa giderek `=` karakterini arar.
- **`q3_find_bit` (Çarpan Biti Kontrolü):** `=`'nin soluna geçer ve çarpanın (ikinci sayı) en sağdaki işlenmemiş bitini kontrol eder.
  - **Bit `0` ise:** Biti `X` ile işaretler, kaydırma adımını temsil eden sayaç artırılır, sonuç değişmeden kalır.
  - **Bit `1` ise:** Biti `Y` ile işaretler, `multiplicand << shift` değeri sonuç değerine eklenir.
- **`q4_move_to_equal` (Sonuca Gitme):** İşaretlenen bitten sonra `=` karakterine doğru sağa ilerler.
- **`q6_write_result` (Sonucu Yazma):** Güncellenen sonucu `=` karakterinin sağına bit bit yazar.
- **`q7_clear_tail` (Sonuç Kuyruğunu Temizleme):** Önceki sonuç daha uzunsa, kalan bitleri `_` ile temizler.
- **`q8_move_to_multiplier` (Yeni Bite Dönme):** `=` karakterine geri dönerek bir sonraki bitten işlem yapmaya hazırlanır.
- **`q9_cleanup` (Temizlik):** İşlem bitince `X` ve `Y` işaretlerini tekrar `0` ve `1` yapar.
- **`q_finalize_result` (Son Kontrol):** Sonuç alanı boşsa `0` yazar, ardından kabul durumuna geçer.
- **`q_accept` (Kabul Durumu):** İşlem başarıyla sonlanır.
- **`q_reject` (Red Durumu):** Tanımlanmamış bir geçişle karşılaşılırsa bu duruma geçilir.



## Ek: Gecis Tablosu ve Diyagram
Gecis tablosu ozet haliyle [gecis_tablosu.md](gecis_tablosu.md) dosyasinda verilmistir.
Durum gecis diyagrami [durum_gecis_diyagrami.md](durum_gecis_diyagrami.md) dosyasinda verilmistir.
