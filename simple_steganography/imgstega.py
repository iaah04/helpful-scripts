#!/usr/bin/env python

import argparse
from PIL import Image

parser = argparse.ArgumentParser(description="Encode or decode message from png file.")
parser.add_argument("-e", "--encode", action='store_true', help="Encode operation.")
parser.add_argument("-d", "--decode", action='store_true', help="Decode operation.")
parser.add_argument("-op", "--original_path", type=str, help="Origin path to image.")
parser.add_argument("-rp", "--result_path", type=str, help="Result path to image.")
parser.add_argument("-m", "--message", type=str, help="Secret message.")
args = parser.parse_args()

# С переводом из символов в биты есть одна проблема:
# некоторые символы (от 32 до 64) умещаются в 6 бит, другие (от 64 до 129) - в 7.
# 63 - это 111111, 128 - это 1111111.
# Поэтому для цифр и знакомов припенания приходиться добавлять по нулю в начало.

def return_bits(message):
    bits = ""
    length = len(message)
    for i in range(length):
        code = ord(message[i])
        binary_code = bin(code)[2:]
        if code <= 63:
            binary_code = "0" + binary_code
        bits += binary_code
    return bits


# Алгоритм декодирования:
# 1. Прочитать изображение
# 2. Прочитать длину секретного сообщения
# 3. Прочитать биты секретного сообщения
# 4. Преобразовать биты в массив
# 5. Преобразовать массив битов в исходное сообщение

def decode(path):
    image = Image.open(path)

    secret_message_length = 0
    pixel = image.getpixel((0, 0))
    for value in pixel:
        secret_message_length += value

    secret_bits = ""
    iteration = 0
    width, height = image.size
    for y in range(height):
        for x in range(1, width):
            if iteration < secret_message_length:
                pixel = image.getpixel((x, y))
                red_channel_value = bin(pixel[0])[2:]
                secret_bits += red_channel_value[-1]
                iteration += 1
            else:
                break

    secret_array = [secret_bits[i:i+7] for i in range(0, secret_message_length, 7)]

    secret_message = ""
    for symbol in secret_array:
        value = int(symbol[1:], 2) if symbol[0] == '0' else int(symbol, 2)
        secret_message += chr(value)

    print(secret_message)

# Алгоритм кодирования:
# 1. Преобразовать секретное сообщение в биты
# 2. Закодировать в первый пиксель длину сообщения
# 3. Волшебный алгоритм кодирования
# 4. Создать изображение с секретным cобщением

def encode(original_path, result_path, message):
    bits = return_bits(message)
    secret_length = len(bits)

    image = Image.open(original_path)
    pixel = list(image.getpixel((0, 0)))
    for i in range(3):
        if secret_length >= 255:
            pixel[i] = 255
            secret_length -= 255
        else:
            pixel[i] = secret_length
            secret_length -= secret_length
    image.putpixel((0, 0), tuple(pixel))

    index = 0
    width, height = image.size
    for y in range(height):
        for x in range(1, width):
            pixel = list(image.getpixel((x, y)))
            if index < len(bits):
                if bits[index] == '0':
                    pixel[0] &= 254
                else:
                    pixel[0] |= 1
                index += 1
                image.putpixel((x, y), tuple(pixel))
            else:
                break

    image.save(result_path)


if args.decode and args.original_path:
    decode(args.original_path)

if args.encode and args.message and args.original_path and args.result_path:
    encode(args.original_path, args.result_path, args.message)

args = parser.parse_args()
