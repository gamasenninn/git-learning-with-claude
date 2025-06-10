#!/usr/bin/env python3
"""
FastMCPを使ったMCPサーバーのサンプル - 計算機能付き
元のmcp_calculator_server.pyをFastMCPを使ってリファクタリング
"""
import math
from typing import Any, Dict

try:
    from fastmcp import FastMCP
except ImportError:
    print("FastMCPがインストールされていません。pip install fastmcp を実行してください。")
    exit(1)

# FastMCPアプリケーションを作成
app = FastMCP("Simple Calculator MCP Server")

def safe_calculate(expression: str) -> Dict[str, Any]:
    """安全な計算実行（元のmcp_calculator_server.pyと同じロジック）"""
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
        
        return {
            "success": True,
            "expression": expression,
            "result": result,
            "type": type(result).__name__
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "expression": expression
        }

@app.tool()
def calculate(expression: str) -> str:
    """
    数学的な計算を実行します
    
    Args:
        expression: 計算式 (例: "2 + 3", "sqrt(16)", "sin(pi/2)")
    
    Returns:
        計算結果のJSON文字列
    
    Examples:
        - calculate("2 + 3 * 4") -> "14"
        - calculate("sqrt(16)") -> "4.0"
        - calculate("sin(pi/2)") -> "1.0"
    """
    import json
    result = safe_calculate(expression)
    return json.dumps(result, ensure_ascii=False, indent=2)

@app.tool()
def calculate_advanced(expression: str, precision: int = 6) -> str:
    """
    高精度な数学計算を実行します
    
    Args:
        expression: 計算式
        precision: 小数点以下の桁数 (デフォルト: 6)
    
    Returns:
        高精度計算結果のJSON文字列
    """
    import json
    result = safe_calculate(expression)
    
    if result["success"] and isinstance(result["result"], float):
        result["result"] = round(result["result"], precision)
        result["precision"] = precision
    
    return json.dumps(result, ensure_ascii=False, indent=2)

@app.tool()
def get_math_constants() -> str:
    """
    利用可能な数学定数の一覧を返します
    
    Returns:
        数学定数のJSON文字列
    """
    import json
    constants = {
        "pi": math.pi,
        "e": math.e,
        "tau": math.tau if hasattr(math, 'tau') else 2 * math.pi,
        "inf": math.inf,
        "nan": "NaN (Not a Number)"
    }
    
    return json.dumps({
        "constants": constants,
        "description": "利用可能な数学定数一覧"
    }, ensure_ascii=False, indent=2)

@app.tool()
def get_available_functions() -> str:
    """
    利用可能な数学関数の一覧を返します
    
    Returns:
        数学関数のJSON文字列
    """
    import json
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
    
    return json.dumps({
        "functions": functions,
        "examples": examples,
        "description": "利用可能な数学関数一覧と使用例"
    }, ensure_ascii=False, indent=2)

def main():
    """FastMCPサーバーを起動"""
    import sys
    print("FastMCP Calculator Server starting...", file=sys.stderr)
    print("利用可能なツール:", file=sys.stderr)
    print("- calculate: 基本的な数学計算", file=sys.stderr)
    print("- calculate_advanced: 高精度計算", file=sys.stderr)
    print("- get_math_constants: 数学定数一覧", file=sys.stderr)
    print("- get_available_functions: 利用可能関数一覧", file=sys.stderr)
    print("", file=sys.stderr)
    
    # FastMCPサーバーを実行
    app.run()

if __name__ == "__main__":
    main()