#!/usr/bin/env python3
"""
FastMCPが利用できない環境での模擬テスト
"""
import json
import math

def mock_safe_calculate(expression: str):
    """FastMCP版の計算関数をテスト"""
    try:
        # 安全な計算のため、制限された関数のみ許可
        allowed_names = {
            'abs': abs,
            'round': round,
            'pow': pow,
            'sqrt': lambda x: x ** 0.5,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log,
            'pi': math.pi,
            'e': math.e,
            'floor': math.floor,
            'ceil': math.ceil,
            'factorial': math.factorial
        }
        
        # 危険な文字列をチェック
        dangerous = ['import', '__', 'exec', 'eval', 'open', 'file', 'input', 'raw_input']
        if any(word in expression.lower() for word in dangerous):
            return {
                "success": False,
                "error": "危険な操作が検出されました",
                "expression": expression
            }
        
        # 計算実行
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        
        # 複素数をJSON対応形式に変換
        if isinstance(result, complex):
            result_value = f"{result.real}+{result.imag}j" if result.imag >= 0 else f"{result.real}{result.imag}j"
        else:
            result_value = result
        
        return {
            "success": True,
            "expression": expression,
            "result": result_value,
            "type": type(result).__name__
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "expression": expression
        }

def test_fastmcp_functions():
    """FastMCP版の関数をテスト"""
    print("=== FastMCP版計算機能テスト ===\n")
    
    # テストケース
    test_cases = [
        "2 + 3 * 4",
        "sqrt(16)",
        "sin(pi/2)",
        "log(e)",
        "factorial(5)",
        "floor(3.7)",
        "ceil(3.2)",
        "abs(-5)",
        "round(3.14159, 2)"
    ]
    
    for i, expression in enumerate(test_cases, 1):
        print(f"{i}. {expression}")
        result = mock_safe_calculate(expression)
        print(f"   結果: {json.dumps(result, ensure_ascii=False, indent=4)}")
        print()
    
    # エラーテストケース
    print("=== エラーハンドリングテスト ===\n")
    error_cases = [
        "1/0",  # ゼロ除算
        "import os",  # 危険な操作
        "sqrt(-1)",  # 数学エラー
        "undefined_function(1)"  # 未定義関数
    ]
    
    for i, expression in enumerate(error_cases, 1):
        print(f"{i}. {expression}")
        result = mock_safe_calculate(expression)
        print(f"   結果: {json.dumps(result, ensure_ascii=False, indent=4)}")
        print()
    
    # 高精度計算のテスト
    print("=== 高精度計算テスト ===\n")
    precision_tests = [
        ("pi", 10),
        ("e", 8),
        ("sqrt(2)", 12)
    ]
    
    for i, (expr, precision) in enumerate(precision_tests, 1):
        print(f"{i}. {expr} (精度: {precision}桁)")
        result = mock_safe_calculate(expr)
        if result["success"] and isinstance(result["result"], float):
            result["result"] = round(result["result"], precision)
            result["precision"] = precision
        print(f"   結果: {json.dumps(result, ensure_ascii=False, indent=4)}")
        print()

def test_constants_and_functions():
    """数学定数と関数一覧のテスト"""
    print("=== 数学定数テスト ===\n")
    constants = {
        "pi": math.pi,
        "e": math.e,
        "tau": math.tau if hasattr(math, 'tau') else 2 * math.pi,
        "inf": math.inf,
        "nan": "NaN (Not a Number)"
    }
    
    print(json.dumps({
        "constants": constants,
        "description": "利用可能な数学定数一覧"
    }, ensure_ascii=False, indent=2))
    
    print("\n=== 利用可能関数テスト ===\n")
    functions = {
        "basic": ["abs", "round", "pow"],
        "trigonometric": ["sin", "cos", "tan"],
        "logarithmic": ["log"],
        "roots": ["sqrt"],
        "rounding": ["floor", "ceil"],
        "special": ["factorial"]
    }
    
    examples = {
        "abs(-5)": "絶対値: 5",
        "round(3.14159, 2)": "丸め: 3.14",
        "pow(2, 3)": "累乗: 8",
        "sin(pi/2)": "正弦: 1.0",
        "sqrt(16)": "平方根: 4.0",
        "factorial(5)": "階乗: 120"
    }
    
    print(json.dumps({
        "functions": functions,
        "examples": examples,
        "description": "利用可能な数学関数一覧と使用例"
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    test_fastmcp_functions()
    test_constants_and_functions()
    
    print("\n✅ FastMCP版の模擬テストが完了しました！")
    print("💡 実際の実行にはFastMCPのインストールが必要です：")
    print("   pip install fastmcp")