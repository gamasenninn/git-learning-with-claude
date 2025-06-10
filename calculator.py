#!/usr/bin/env python3
"""
簡単な電卓プログラム
基本的な四則演算を行います
"""

def add(a, b):
    """二つの数を足す"""
    return a + b

def subtract(a, b):
    """二つの数を引く"""
    return a - b

def multiply(a, b):
    """二つの数を掛ける"""
    return a * b

def divide(a, b):
    """二つの数を割る"""
    if b == 0:
        raise ValueError("ゼロで除算することはできません")
    return a / b

def main():
    print("=== 簡単な電卓プログラム ===")
    print("操作を選択してください:")
    print("1. 足し算")
    print("2. 引き算")
    print("3. 掛け算")
    print("4. 割り算")
    print("5. 終了")
    
    while True:
        choice = input("\n選択 (1-5): ")
        
        if choice == '5':
            print("プログラムを終了します")
            break
            
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("最初の数を入力: "))
                num2 = float(input("次の数を入力: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"{num1} × {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"{num1} ÷ {num2} = {result}")
                    
            except ValueError as e:
                print(f"エラー: {e}")
            except Exception as e:
                print(f"予期しないエラー: {e}")
        else:
            print("無効な選択です。1-5の数字を入力してください")

if __name__ == "__main__":
    main()