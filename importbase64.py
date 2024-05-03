import base64

def encode_bigint_to_base64(bigint):
    bigint_bytes = bigint.to_bytes((bigint.bit_length() + 7) // 8, byteorder='big')
    return base64.b64encode(bigint_bytes).decode('utf-8')

def decode_base64_to_bigint(base64_string):
    bigint_bytes = base64.b64decode(base64_string)
    return int.from_bytes(bigint_bytes, byteorder='big')

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Кодировать BigInt в Base64")
        print("2. Декодировать Base64 в BigInt")
        print("3. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            bigint_str = input("Введите BigInt для кодирования: ")
            try:
                bigint = int(bigint_str)
                encoded_base64 = encode_bigint_to_base64(bigint)
                print("Закодированное в Base64:", encoded_base64)
            except ValueError:
                print("Ошибка: Введите целое число.")
        elif choice == "2":
            base64_str = input("Введите строку Base64 для декодирования: ")
            try:
                decoded_bigint = decode_base64_to_bigint(base64_str)
                print("Декодированное BigInt:", decoded_bigint)
            except:
                print("Ошибка: Неверный формат строки Base64.")
        elif choice == "3":
            print("Программа завершена.")
            break
        else:
            print("Ошибка: Введите число от 1 до 3.")

if __name__ == "__main__":
    main()
