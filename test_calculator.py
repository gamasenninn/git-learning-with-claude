#!/usr/bin/env python3
"""
電卓プログラムのテストスクリプト
"""
from calculator import add, subtract, multiply, divide, sqrt

print("=== 電卓機能のテスト ===")

# 足し算のテスト
print("\n1. 足し算のテスト")
print(f"  10 + 5 = {add(10, 5)}")
print(f"  -3 + 7 = {add(-3, 7)}")

# 引き算のテスト
print("\n2. 引き算のテスト")
print(f"  10 - 5 = {subtract(10, 5)}")
print(f"  3 - 7 = {subtract(3, 7)}")

# 掛け算のテスト
print("\n3. 掛け算のテスト")
print(f"  4 × 5 = {multiply(4, 5)}")
print(f"  -3 × 6 = {multiply(-3, 6)}")

# 割り算のテスト
print("\n4. 割り算のテスト")
print(f"  20 ÷ 4 = {divide(20, 4)}")
print(f"  7 ÷ 2 = {divide(7, 2)}")

# 平方根のテスト（新機能）
print("\n5. 平方根のテスト（新機能）")
print(f"  √16 = {sqrt(16)}")
print(f"  √25 = {sqrt(25)}")
print(f"  √2 = {sqrt(2):.4f}")

# エラーケースのテスト
print("\n6. エラーケースのテスト")
try:
    divide(10, 0)
except ValueError as e:
    print(f"  ゼロ除算: {e}")

try:
    sqrt(-4)
except ValueError as e:
    print(f"  負の数の平方根: {e}")

print("\n✅ すべてのテストが完了しました！")