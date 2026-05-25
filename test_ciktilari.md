# Test Ciktilari (Tum Adimlar)

## Test 1: 11 * 10

```text
1. ikili sayiyi girin (ornek: 1011): 11
2. ikili sayiyi girin (ornek: 010): 10
Adım 1:
  Durum : q0_scan_star
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _11*10=_
        ^

Adım 2:
  Durum : q0_scan_star
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _11*10=_
         ^

Adım 3:
  Durum : q0_scan_star
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _11*10=_
          ^

Adım 4:
  Durum : q0_scan_star
  Okunan: *
  Yazılan: *
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _11*10=_
           ^

Adım 5:
  Durum : q1_scan_equal
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _11*10=_
            ^

Adım 6:
  Durum : q1_scan_equal
  Okunan: 0
  Yazılan: 0
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _11*10=_
             ^

Adım 7:
  Durum : q1_scan_equal
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _11*10=_
            ^

Adım 8:
  Durum : q3_find_bit
  Okunan: 0
  Yazılan: X
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _11*1X=_
             ^

Adım 9:
  Durum : q4_move_to_equal
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q8_move_to_multiplier
  Bant: _11*1X=_
              ^

Adım 10:
  Durum : q8_move_to_multiplier
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _11*1X=_
             ^

Adım 11:
  Durum : q8_move_to_multiplier
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _11*1X=_
            ^

Adım 12:
  Durum : q3_find_bit
  Okunan: X
  Yazılan: X
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _11*1X=_
           ^

Adım 13:
  Durum : q3_find_bit
  Okunan: 1
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _11*YX=_
            ^

Adım 14:
  Durum : q4_move_to_equal
  Okunan: X
  Yazılan: X
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _11*YX=_
             ^

Adım 15:
  Durum : q4_move_to_equal
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _11*YX=_
              ^

Adım 16:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _11*YX=1
               ^

Adım 17:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _11*YX=11
                ^

Adım 18:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 0
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _11*YX=110
                 ^

Adım 19:
  Durum : q6_write_result
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q7_clear_tail
  Bant: _11*YX=110_
                  ^

Adım 20:
  Durum : q7_clear_tail
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _11*YX=110__
                 ^

Adım 21:
  Durum : q8_move_to_multiplier
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _11*YX=110__
                ^

Adım 22:
  Durum : q8_move_to_multiplier
  Okunan: 0
  Yazılan: 0
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _11*YX=110__
               ^

Adım 23:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _11*YX=110__
              ^

Adım 24:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _11*YX=110__
             ^

Adım 25:
  Durum : q8_move_to_multiplier
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _11*YX=110__
            ^

Adım 26:
  Durum : q3_find_bit
  Okunan: X
  Yazılan: X
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _11*YX=110__
           ^

Adım 27:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _11*YX=110__
          ^

Adım 28:
  Durum : q3_find_bit
  Okunan: *
  Yazılan: *
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _11*YX=110__
           ^

Adım 29:
  Durum : q9_cleanup
  Okunan: Y
  Yazılan: 1
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _11*1X=110__
            ^

Adım 30:
  Durum : q9_cleanup
  Okunan: X
  Yazılan: 0
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _11*10=110__
             ^

Adım 31:
  Durum : q9_cleanup
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q_finalize_result
  Bant: _11*10=110__
              ^

Adım 32:
  Durum : q_finalize_result
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q_accept
  Bant: _11*10=110__
             ^

==============================
Islem basariyla tamamlandi (Kabul Durumu).
==============================

--- SONUÇ ---
Girdi (Binary) : 11 * 10
Girdi (Decimal): 3 * 2
---------------
Sonuç (Binary) : 110
Sonuç (Decimal): 6

Dogrulama: Basarili.
```

## Test 2: 101 * 11

```text
1. ikili sayiyi girin (ornek: 1011): 101
2. ikili sayiyi girin (ornek: 010): 11
Adım 1:
  Durum : q0_scan_star
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _101*11=_
        ^

Adım 2:
  Durum : q0_scan_star
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _101*11=_
         ^

Adım 3:
  Durum : q0_scan_star
  Okunan: 0
  Yazılan: 0
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _101*11=_
          ^

Adım 4:
  Durum : q0_scan_star
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _101*11=_
           ^

Adım 5:
  Durum : q0_scan_star
  Okunan: *
  Yazılan: *
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _101*11=_
            ^

Adım 6:
  Durum : q1_scan_equal
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _101*11=_
             ^

Adım 7:
  Durum : q1_scan_equal
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _101*11=_
              ^

Adım 8:
  Durum : q1_scan_equal
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _101*11=_
             ^

Adım 9:
  Durum : q3_find_bit
  Okunan: 1
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _101*1Y=_
              ^

Adım 10:
  Durum : q4_move_to_equal
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _101*1Y=_
               ^

Adım 11:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _101*1Y=1
                ^

Adım 12:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 0
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _101*1Y=10
                 ^

Adım 13:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _101*1Y=101
                  ^

Adım 14:
  Durum : q6_write_result
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q7_clear_tail
  Bant: _101*1Y=101_
                   ^

Adım 15:
  Durum : q7_clear_tail
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _101*1Y=101__
                  ^

Adım 16:
  Durum : q8_move_to_multiplier
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _101*1Y=101__
                 ^

Adım 17:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _101*1Y=101__
                ^

Adım 18:
  Durum : q8_move_to_multiplier
  Okunan: 0
  Yazılan: 0
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _101*1Y=101__
               ^

Adım 19:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _101*1Y=101__
              ^

Adım 20:
  Durum : q8_move_to_multiplier
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _101*1Y=101__
             ^

Adım 21:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _101*1Y=101__
            ^

Adım 22:
  Durum : q3_find_bit
  Okunan: 1
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _101*YY=101__
             ^

Adım 23:
  Durum : q4_move_to_equal
  Okunan: Y
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _101*YY=101__
              ^

Adım 24:
  Durum : q4_move_to_equal
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _101*YY=101__
               ^

Adım 25:
  Durum : q6_write_result
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _101*YY=101__
                ^

Adım 26:
  Durum : q6_write_result
  Okunan: 0
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _101*YY=111__
                 ^

Adım 27:
  Durum : q6_write_result
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _101*YY=111__
                  ^

Adım 28:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _101*YY=1111_
                   ^

Adım 29:
  Durum : q6_write_result
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q7_clear_tail
  Bant: _101*YY=1111_
                    ^

Adım 30:
  Durum : q7_clear_tail
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _101*YY=1111__
                   ^

Adım 31:
  Durum : q8_move_to_multiplier
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _101*YY=1111__
                  ^

Adım 32:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _101*YY=1111__
                 ^

Adım 33:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _101*YY=1111__
                ^

Adım 34:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _101*YY=1111__
               ^

Adım 35:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _101*YY=1111__
              ^

Adım 36:
  Durum : q8_move_to_multiplier
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _101*YY=1111__
             ^

Adım 37:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _101*YY=1111__
            ^

Adım 38:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _101*YY=1111__
           ^

Adım 39:
  Durum : q3_find_bit
  Okunan: *
  Yazılan: *
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _101*YY=1111__
            ^

Adım 40:
  Durum : q9_cleanup
  Okunan: Y
  Yazılan: 1
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _101*1Y=1111__
             ^

Adım 41:
  Durum : q9_cleanup
  Okunan: Y
  Yazılan: 1
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _101*11=1111__
              ^

Adım 42:
  Durum : q9_cleanup
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q_finalize_result
  Bant: _101*11=1111__
               ^

Adım 43:
  Durum : q_finalize_result
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q_accept
  Bant: _101*11=1111__
              ^

==============================
Islem basariyla tamamlandi (Kabul Durumu).
==============================

--- SONUÇ ---
Girdi (Binary) : 101 * 11
Girdi (Decimal): 5 * 3
---------------
Sonuç (Binary) : 1111
Sonuç (Decimal): 15

Dogrulama: Basarili.
```

## Test 3: 111 * 101

```text
1. ikili sayiyi girin (ornek: 1011): 111
2. ikili sayiyi girin (ornek: 010): 101
Adım 1:
  Durum : q0_scan_star
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _111*101=_
        ^

Adım 2:
  Durum : q0_scan_star
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _111*101=_
         ^

Adım 3:
  Durum : q0_scan_star
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _111*101=_
          ^

Adım 4:
  Durum : q0_scan_star
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _111*101=_
           ^

Adım 5:
  Durum : q0_scan_star
  Okunan: *
  Yazılan: *
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _111*101=_
            ^

Adım 6:
  Durum : q1_scan_equal
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _111*101=_
             ^

Adım 7:
  Durum : q1_scan_equal
  Okunan: 0
  Yazılan: 0
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _111*101=_
              ^

Adım 8:
  Durum : q1_scan_equal
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _111*101=_
               ^

Adım 9:
  Durum : q1_scan_equal
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _111*101=_
              ^

Adım 10:
  Durum : q3_find_bit
  Okunan: 1
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _111*10Y=_
               ^

Adım 11:
  Durum : q4_move_to_equal
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _111*10Y=_
                ^

Adım 12:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _111*10Y=1
                 ^

Adım 13:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _111*10Y=11
                  ^

Adım 14:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _111*10Y=111
                   ^

Adım 15:
  Durum : q6_write_result
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q7_clear_tail
  Bant: _111*10Y=111_
                    ^

Adım 16:
  Durum : q7_clear_tail
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*10Y=111__
                   ^

Adım 17:
  Durum : q8_move_to_multiplier
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*10Y=111__
                  ^

Adım 18:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*10Y=111__
                 ^

Adım 19:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*10Y=111__
                ^

Adım 20:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*10Y=111__
               ^

Adım 21:
  Durum : q8_move_to_multiplier
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _111*10Y=111__
              ^

Adım 22:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _111*10Y=111__
             ^

Adım 23:
  Durum : q3_find_bit
  Okunan: 0
  Yazılan: X
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _111*1XY=111__
              ^

Adım 24:
  Durum : q4_move_to_equal
  Okunan: Y
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _111*1XY=111__
               ^

Adım 25:
  Durum : q4_move_to_equal
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*1XY=111__
                ^

Adım 26:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*1XY=111__
               ^

Adım 27:
  Durum : q8_move_to_multiplier
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _111*1XY=111__
              ^

Adım 28:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _111*1XY=111__
             ^

Adım 29:
  Durum : q3_find_bit
  Okunan: X
  Yazılan: X
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _111*1XY=111__
            ^

Adım 30:
  Durum : q3_find_bit
  Okunan: 1
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _111*YXY=111__
             ^

Adım 31:
  Durum : q4_move_to_equal
  Okunan: X
  Yazılan: X
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _111*YXY=111__
              ^

Adım 32:
  Durum : q4_move_to_equal
  Okunan: Y
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _111*YXY=111__
               ^

Adım 33:
  Durum : q4_move_to_equal
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _111*YXY=111__
                ^

Adım 34:
  Durum : q6_write_result
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _111*YXY=111__
                 ^

Adım 35:
  Durum : q6_write_result
  Okunan: 1
  Yazılan: 0
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _111*YXY=101__
                  ^

Adım 36:
  Durum : q6_write_result
  Okunan: 1
  Yazılan: 0
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _111*YXY=100__
                   ^

Adım 37:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 0
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _111*YXY=1000_
                    ^

Adım 38:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _111*YXY=10001
                     ^

Adım 39:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _111*YXY=100011
                      ^

Adım 40:
  Durum : q6_write_result
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q7_clear_tail
  Bant: _111*YXY=100011_
                       ^

Adım 41:
  Durum : q7_clear_tail
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*YXY=100011__
                      ^

Adım 42:
  Durum : q8_move_to_multiplier
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*YXY=100011__
                     ^

Adım 43:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*YXY=100011__
                    ^

Adım 44:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*YXY=100011__
                   ^

Adım 45:
  Durum : q8_move_to_multiplier
  Okunan: 0
  Yazılan: 0
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*YXY=100011__
                  ^

Adım 46:
  Durum : q8_move_to_multiplier
  Okunan: 0
  Yazılan: 0
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*YXY=100011__
                 ^

Adım 47:
  Durum : q8_move_to_multiplier
  Okunan: 0
  Yazılan: 0
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*YXY=100011__
                ^

Adım 48:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _111*YXY=100011__
               ^

Adım 49:
  Durum : q8_move_to_multiplier
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _111*YXY=100011__
              ^

Adım 50:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _111*YXY=100011__
             ^

Adım 51:
  Durum : q3_find_bit
  Okunan: X
  Yazılan: X
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _111*YXY=100011__
            ^

Adım 52:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _111*YXY=100011__
           ^

Adım 53:
  Durum : q3_find_bit
  Okunan: *
  Yazılan: *
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _111*YXY=100011__
            ^

Adım 54:
  Durum : q9_cleanup
  Okunan: Y
  Yazılan: 1
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _111*1XY=100011__
             ^

Adım 55:
  Durum : q9_cleanup
  Okunan: X
  Yazılan: 0
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _111*10Y=100011__
              ^

Adım 56:
  Durum : q9_cleanup
  Okunan: Y
  Yazılan: 1
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _111*101=100011__
               ^

Adım 57:
  Durum : q9_cleanup
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q_finalize_result
  Bant: _111*101=100011__
                ^

Adım 58:
  Durum : q_finalize_result
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q_accept
  Bant: _111*101=100011__
               ^

==============================
Islem basariyla tamamlandi (Kabul Durumu).
==============================

--- SONUÇ ---
Girdi (Binary) : 111 * 101
Girdi (Decimal): 7 * 5
---------------
Sonuç (Binary) : 100011
Sonuç (Decimal): 35

Dogrulama: Basarili.
```

## Test 4: 10 * 0

```text
1. ikili sayiyi girin (ornek: 1011): 10
2. ikili sayiyi girin (ornek: 010): 0
Adım 1:
  Durum : q0_scan_star
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _10*0=_
        ^

Adım 2:
  Durum : q0_scan_star
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _10*0=_
         ^

Adım 3:
  Durum : q0_scan_star
  Okunan: 0
  Yazılan: 0
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _10*0=_
          ^

Adım 4:
  Durum : q0_scan_star
  Okunan: *
  Yazılan: *
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _10*0=_
           ^

Adım 5:
  Durum : q1_scan_equal
  Okunan: 0
  Yazılan: 0
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _10*0=_
            ^

Adım 6:
  Durum : q1_scan_equal
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _10*0=_
           ^

Adım 7:
  Durum : q3_find_bit
  Okunan: 0
  Yazılan: X
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _10*X=_
            ^

Adım 8:
  Durum : q4_move_to_equal
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q8_move_to_multiplier
  Bant: _10*X=_
             ^

Adım 9:
  Durum : q8_move_to_multiplier
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _10*X=_
            ^

Adım 10:
  Durum : q8_move_to_multiplier
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _10*X=_
           ^

Adım 11:
  Durum : q3_find_bit
  Okunan: X
  Yazılan: X
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _10*X=_
          ^

Adım 12:
  Durum : q3_find_bit
  Okunan: *
  Yazılan: *
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _10*X=_
           ^

Adım 13:
  Durum : q9_cleanup
  Okunan: X
  Yazılan: 0
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _10*0=_
            ^

Adım 14:
  Durum : q9_cleanup
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q_finalize_result
  Bant: _10*0=_
             ^

Adım 15:
  Durum : q_finalize_result
  Okunan: _
  Yazılan: 0
  Hareket: L
  Yeni Durum: q_accept
  Bant: _10*0=0
            ^

==============================
Islem basariyla tamamlandi (Kabul Durumu).
==============================

--- SONUÇ ---
Girdi (Binary) : 10 * 0
Girdi (Decimal): 2 * 0
---------------
Sonuç (Binary) : 0
Sonuç (Decimal): 0

Dogrulama: Basarili.
```

## Test 5: 1 * 1111

```text
1. ikili sayiyi girin (ornek: 1011): 1
2. ikili sayiyi girin (ornek: 010): 1111
Adım 1:
  Durum : q0_scan_star
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _1*1111=_
        ^

Adım 2:
  Durum : q0_scan_star
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q0_scan_star
  Bant: _1*1111=_
         ^

Adım 3:
  Durum : q0_scan_star
  Okunan: *
  Yazılan: *
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _1*1111=_
          ^

Adım 4:
  Durum : q1_scan_equal
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _1*1111=_
           ^

Adım 5:
  Durum : q1_scan_equal
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _1*1111=_
            ^

Adım 6:
  Durum : q1_scan_equal
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _1*1111=_
             ^

Adım 7:
  Durum : q1_scan_equal
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q1_scan_equal
  Bant: _1*1111=_
              ^

Adım 8:
  Durum : q1_scan_equal
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*1111=_
             ^

Adım 9:
  Durum : q3_find_bit
  Okunan: 1
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _1*111Y=_
              ^

Adım 10:
  Durum : q4_move_to_equal
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*111Y=_
               ^

Adım 11:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*111Y=1
                ^

Adım 12:
  Durum : q6_write_result
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q7_clear_tail
  Bant: _1*111Y=1_
                 ^

Adım 13:
  Durum : q7_clear_tail
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*111Y=1__
                ^

Adım 14:
  Durum : q8_move_to_multiplier
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*111Y=1__
               ^

Adım 15:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*111Y=1__
              ^

Adım 16:
  Durum : q8_move_to_multiplier
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*111Y=1__
             ^

Adım 17:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*111Y=1__
            ^

Adım 18:
  Durum : q3_find_bit
  Okunan: 1
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _1*11YY=1__
             ^

Adım 19:
  Durum : q4_move_to_equal
  Okunan: Y
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _1*11YY=1__
              ^

Adım 20:
  Durum : q4_move_to_equal
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*11YY=1__
               ^

Adım 21:
  Durum : q6_write_result
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*11YY=1__
                ^

Adım 22:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*11YY=11_
                 ^

Adım 23:
  Durum : q6_write_result
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q7_clear_tail
  Bant: _1*11YY=11_
                  ^

Adım 24:
  Durum : q7_clear_tail
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*11YY=11__
                 ^

Adım 25:
  Durum : q8_move_to_multiplier
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*11YY=11__
                ^

Adım 26:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*11YY=11__
               ^

Adım 27:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*11YY=11__
              ^

Adım 28:
  Durum : q8_move_to_multiplier
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*11YY=11__
             ^

Adım 29:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*11YY=11__
            ^

Adım 30:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*11YY=11__
           ^

Adım 31:
  Durum : q3_find_bit
  Okunan: 1
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _1*1YYY=11__
            ^

Adım 32:
  Durum : q4_move_to_equal
  Okunan: Y
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _1*1YYY=11__
             ^

Adım 33:
  Durum : q4_move_to_equal
  Okunan: Y
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _1*1YYY=11__
              ^

Adım 34:
  Durum : q4_move_to_equal
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*1YYY=11__
               ^

Adım 35:
  Durum : q6_write_result
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*1YYY=11__
                ^

Adım 36:
  Durum : q6_write_result
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*1YYY=11__
                 ^

Adım 37:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*1YYY=111_
                  ^

Adım 38:
  Durum : q6_write_result
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q7_clear_tail
  Bant: _1*1YYY=111_
                   ^

Adım 39:
  Durum : q7_clear_tail
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*1YYY=111__
                  ^

Adım 40:
  Durum : q8_move_to_multiplier
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*1YYY=111__
                 ^

Adım 41:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*1YYY=111__
                ^

Adım 42:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*1YYY=111__
               ^

Adım 43:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*1YYY=111__
              ^

Adım 44:
  Durum : q8_move_to_multiplier
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*1YYY=111__
             ^

Adım 45:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*1YYY=111__
            ^

Adım 46:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*1YYY=111__
           ^

Adım 47:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*1YYY=111__
          ^

Adım 48:
  Durum : q3_find_bit
  Okunan: 1
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _1*YYYY=111__
           ^

Adım 49:
  Durum : q4_move_to_equal
  Okunan: Y
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _1*YYYY=111__
            ^

Adım 50:
  Durum : q4_move_to_equal
  Okunan: Y
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _1*YYYY=111__
             ^

Adım 51:
  Durum : q4_move_to_equal
  Okunan: Y
  Yazılan: Y
  Hareket: R
  Yeni Durum: q4_move_to_equal
  Bant: _1*YYYY=111__
              ^

Adım 52:
  Durum : q4_move_to_equal
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*YYYY=111__
               ^

Adım 53:
  Durum : q6_write_result
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*YYYY=111__
                ^

Adım 54:
  Durum : q6_write_result
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*YYYY=111__
                 ^

Adım 55:
  Durum : q6_write_result
  Okunan: 1
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*YYYY=111__
                  ^

Adım 56:
  Durum : q6_write_result
  Okunan: _
  Yazılan: 1
  Hareket: R
  Yeni Durum: q6_write_result
  Bant: _1*YYYY=1111_
                   ^

Adım 57:
  Durum : q6_write_result
  Okunan: _
  Yazılan: _
  Hareket: R
  Yeni Durum: q7_clear_tail
  Bant: _1*YYYY=1111_
                    ^

Adım 58:
  Durum : q7_clear_tail
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*YYYY=1111__
                   ^

Adım 59:
  Durum : q8_move_to_multiplier
  Okunan: _
  Yazılan: _
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*YYYY=1111__
                  ^

Adım 60:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*YYYY=1111__
                 ^

Adım 61:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*YYYY=1111__
                ^

Adım 62:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*YYYY=1111__
               ^

Adım 63:
  Durum : q8_move_to_multiplier
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q8_move_to_multiplier
  Bant: _1*YYYY=1111__
              ^

Adım 64:
  Durum : q8_move_to_multiplier
  Okunan: =
  Yazılan: =
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*YYYY=1111__
             ^

Adım 65:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*YYYY=1111__
            ^

Adım 66:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*YYYY=1111__
           ^

Adım 67:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*YYYY=1111__
          ^

Adım 68:
  Durum : q3_find_bit
  Okunan: Y
  Yazılan: Y
  Hareket: L
  Yeni Durum: q3_find_bit
  Bant: _1*YYYY=1111__
         ^

Adım 69:
  Durum : q3_find_bit
  Okunan: *
  Yazılan: *
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _1*YYYY=1111__
          ^

Adım 70:
  Durum : q9_cleanup
  Okunan: Y
  Yazılan: 1
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _1*1YYY=1111__
           ^

Adım 71:
  Durum : q9_cleanup
  Okunan: Y
  Yazılan: 1
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _1*11YY=1111__
            ^

Adım 72:
  Durum : q9_cleanup
  Okunan: Y
  Yazılan: 1
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _1*111Y=1111__
             ^

Adım 73:
  Durum : q9_cleanup
  Okunan: Y
  Yazılan: 1
  Hareket: R
  Yeni Durum: q9_cleanup
  Bant: _1*1111=1111__
              ^

Adım 74:
  Durum : q9_cleanup
  Okunan: =
  Yazılan: =
  Hareket: R
  Yeni Durum: q_finalize_result
  Bant: _1*1111=1111__
               ^

Adım 75:
  Durum : q_finalize_result
  Okunan: 1
  Yazılan: 1
  Hareket: L
  Yeni Durum: q_accept
  Bant: _1*1111=1111__
              ^

==============================
Islem basariyla tamamlandi (Kabul Durumu).
==============================

--- SONUÇ ---
Girdi (Binary) : 1 * 1111
Girdi (Decimal): 1 * 15
---------------
Sonuç (Binary) : 1111
Sonuç (Decimal): 15

Dogrulama: Basarili.
```
