## Usage:

!!! No validation and tests !!!

decode:

```
python3 stegachanbrain.py -e -m "Hello" -op "./origin_picture.png" -rp "./result_picture.png"
```

encode:

```
python3 stegachanbrain.py -d -op "./result_picture.png"
```

## Algorithm

Eng.
Some theoretical information:
The length is written ONLY in the first pixel, so the maximum message length is 1020 bits (255 * 3).
Thus, a user can encrypt only 145 characters.

Least Significant Bit Algorithm:
Our task is to embed secret bits into the red channel's values in the pixels.
To achieve this, if the current secret bit is 0, a conjunction with the number 254 (11111110) is applied.
As a result, the last bit of the red channel's number becomes 0, regardless of whether it was originally 0 or 1.
If the current secret bit is 1, a disjunction with the number 1 (00000001) is applied.
As a result, the last bit of the red channel's number becomes 1, regardless of whether it was originally 0 or 1.

***

Рус.
Немного теоритических сведений:
длинна записывается ТОЛЬКО в первый пиксель, поэтому максимальная длинна сообщения: 1020 бит (255 * 3)
таким образом, пользователь может зашифровать всего 145 символов.

Алгоритм Least Significant Bit
Наша задача: зашить секретные биты в число красного канала в пикселях.
Для этого, если текущий секретный бит 0, то применяется конъюкция с числом 254 (11111110).
Таким образом, последний бит цифры красного канала станет 0 вне зависимости 0 это или 1.
Если текущий секретный бит 1, то применяется дезъюнкция с числом 1 (00000001).
Таким образом, последний бит цифры красного канала станет 1 вне зависимости 0 это или 1.
