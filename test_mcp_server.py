#!/usr/bin/env python3
"""
MCPサーバーの簡単なテストスクリプト
"""
import json
import subprocess
import sys

def test_mcp_server():
    """MCPサーバーをテストする"""
    
    print("=== MCPサーバーテスト開始 ===")
    
    # テストケース
    test_cases = [
        {
            "name": "初期化テスト",
            "message": {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {}
            }
        },
        {
            "name": "ツール一覧テスト",
            "message": {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/list"
            }
        },
        {
            "name": "基本計算テスト",
            "message": {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {
                    "name": "calculate",
                    "arguments": {
                        "expression": "2 + 3 * 4"
                    }
                }
            }
        },
        {
            "name": "平方根テスト",
            "message": {
                "jsonrpc": "2.0",
                "id": 4,
                "method": "tools/call",
                "params": {
                    "name": "calculate",
                    "arguments": {
                        "expression": "sqrt(16)"
                    }
                }
            }
        },
        {
            "name": "三角関数テスト",
            "message": {
                "jsonrpc": "2.0",
                "id": 5,
                "method": "tools/call",
                "params": {
                    "name": "calculate",
                    "arguments": {
                        "expression": "sin(pi/2)"
                    }
                }
            }
        },
        {
            "name": "エラーハンドリングテスト",
            "message": {
                "jsonrpc": "2.0",
                "id": 6,
                "method": "tools/call",
                "params": {
                    "name": "calculate",
                    "arguments": {
                        "expression": "1/0"
                    }
                }
            }
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{i}. {test_case['name']}")
        print(f"送信: {json.dumps(test_case['message'], ensure_ascii=False)}")
        
        try:
            # MCPサーバーにメッセージを送信
            process = subprocess.Popen(
                [sys.executable, 'mcp_calculator_server.py'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # メッセージを送信して即座に終了
            stdout, stderr = process.communicate(
                input=json.dumps(test_case['message']) + '\n',
                timeout=5
            )
            
            if stdout.strip():
                try:
                    response = json.loads(stdout.strip())
                    print(f"応答: {json.dumps(response, ensure_ascii=False, indent=2)}")
                except json.JSONDecodeError:
                    print(f"応答 (raw): {stdout.strip()}")
            
            if stderr.strip():
                print(f"ログ: {stderr.strip()}")
                
        except subprocess.TimeoutExpired:
            process.kill()
            print("タイムアウトしました")
        except Exception as e:
            print(f"エラー: {e}")
    
    print("\n=== テスト完了 ===")

if __name__ == "__main__":
    test_mcp_server()