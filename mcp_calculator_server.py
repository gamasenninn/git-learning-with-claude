#!/usr/bin/env python3
"""
簡単なMCPサーバーのサンプル - 計算機能付き
"""
import asyncio
import json
import sys
from typing import Any, Dict, List, Optional

class MCPCalculatorServer:
    """計算機能を持つシンプルなMCPサーバー"""
    
    def __init__(self):
        self.tools = {
            "calculate": {
                "description": "数学的な計算を実行します",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "計算式 (例: 2 + 3, 10 * 5, sqrt(16))"
                        }
                    },
                    "required": ["expression"]
                }
            }
        }
    
    def calculate(self, expression: str) -> Dict[str, Any]:
        """安全な計算実行"""
        try:
            # 安全な計算のため、制限された関数のみ許可
            allowed_names = {
                'abs': abs,
                'round': round,
                'pow': pow,
                'sqrt': lambda x: x ** 0.5,
                'sin': lambda x: __import__('math').sin(x),
                'cos': lambda x: __import__('math').cos(x),
                'tan': lambda x: __import__('math').tan(x),
                'log': lambda x: __import__('math').log(x),
                'pi': __import__('math').pi,
                'e': __import__('math').e
            }
            
            # 危険な文字列をチェック
            dangerous = ['import', '__', 'exec', 'eval', 'open', 'file']
            if any(word in expression.lower() for word in dangerous):
                return {
                    "success": False,
                    "error": "危険な操作が検出されました"
                }
            
            # 計算実行
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            
            return {
                "success": True,
                "expression": expression,
                "result": result
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "expression": expression
            }
    
    async def handle_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """MCPメッセージを処理"""
        
        if message.get("method") == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": message.get("id"),
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {}
                    },
                    "serverInfo": {
                        "name": "simple-calculator-mcp",
                        "version": "1.0.0"
                    }
                }
            }
        
        elif message.get("method") == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": message.get("id"),
                "result": {
                    "tools": [
                        {
                            "name": "calculate",
                            "description": self.tools["calculate"]["description"],
                            "inputSchema": self.tools["calculate"]["inputSchema"]
                        }
                    ]
                }
            }
        
        elif message.get("method") == "tools/call":
            params = message.get("params", {})
            tool_name = params.get("name")
            arguments = params.get("arguments", {})
            
            if tool_name == "calculate":
                expression = arguments.get("expression", "")
                result = self.calculate(expression)
                
                return {
                    "jsonrpc": "2.0",
                    "id": message.get("id"),
                    "result": {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps(result, ensure_ascii=False, indent=2)
                            }
                        ]
                    }
                }
        
        # 未対応のメソッド
        return {
            "jsonrpc": "2.0",
            "id": message.get("id"),
            "error": {
                "code": -32601,
                "message": f"Method not found: {message.get('method')}"
            }
        }
    
    async def run(self):
        """サーバーを実行"""
        print("MCP Calculator Server starting...", file=sys.stderr)
        print("サポートされている計算:", file=sys.stderr)
        print("- 基本演算: +, -, *, /, **, %", file=sys.stderr)
        print("- 関数: sqrt(), abs(), round(), pow()", file=sys.stderr)
        print("- 三角関数: sin(), cos(), tan()", file=sys.stderr)
        print("- 定数: pi, e", file=sys.stderr)
        print("", file=sys.stderr)
        
        try:
            while True:
                line = await asyncio.get_event_loop().run_in_executor(
                    None, sys.stdin.readline
                )
                
                if not line:
                    break
                
                try:
                    message = json.loads(line.strip())
                    response = await self.handle_message(message)
                    print(json.dumps(response, ensure_ascii=False))
                    sys.stdout.flush()
                    
                except json.JSONDecodeError:
                    print(json.dumps({
                        "jsonrpc": "2.0",
                        "error": {
                            "code": -32700,
                            "message": "Parse error"
                        }
                    }))
                    sys.stdout.flush()
                    
        except KeyboardInterrupt:
            print("Server shutting down...", file=sys.stderr)

async def main():
    """メイン関数"""
    server = MCPCalculatorServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())