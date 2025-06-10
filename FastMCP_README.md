# FastMCP版 MCPサーバーサンプル

## 概要
Issue #4で要望されたFastMCPを使ったMCPサーバーのバージョンです。
元の`mcp_calculator_server.py`をFastMCPフレームワークを使ってリファクタリングしました。

## FastMCPの利点

### 元のバージョンとの比較

| 項目 | 元のバージョン | FastMCP版 |
|------|--------------|-----------|
| **コード量** | ~180行 | ~120行 |
| **可読性** | 手動JSON-RPC処理 | デコレーターベース |
| **ツール定義** | 手動でスキーマ定義 | 自動生成 |
| **エラーハンドリング** | 手動実装 | フレームワークが処理 |
| **型安全性** | 低い | 高い（型ヒント活用） |

### FastMCPの特徴
- **シンプルな構文**: `@app.tool()`デコレーターでツールを定義
- **自動スキーマ生成**: 関数の型ヒントから自動でJSONスキーマを生成
- **組み込みエラーハンドリング**: JSON-RPCエラーを自動処理
- **開発効率**: ボイラープレートコードを大幅削減

## 新機能

FastMCP版では以下の新しいツールが追加されています：

1. **calculate_advanced**: 高精度計算（小数点桁数指定可能）
2. **get_math_constants**: 利用可能な数学定数一覧
3. **get_available_functions**: 利用可能な数学関数一覧

## インストールと実行

### 依存関係のインストール
```bash
# FastMCPをインストール
pip install fastmcp

# または、uvを使用
uv add fastmcp
```

### 実行方法
```bash
# 直接実行
python fastmcp_calculator_server.py

# uvを使って実行
uv run python fastmcp_calculator_server.py

# パッケージとして実行
uv run mcp-calculator-fast
```

## 利用可能なツール

### 1. calculate
基本的な数学計算を実行します。

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "calculate",
    "arguments": {
      "expression": "2 + 3 * 4"
    }
  }
}
```

### 2. calculate_advanced
高精度な数学計算を実行します。

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "calculate_advanced",
    "arguments": {
      "expression": "pi",
      "precision": 10
    }
  }
}
```

### 3. get_math_constants
利用可能な数学定数の一覧を返します。

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "get_math_constants",
    "arguments": {}
  }
}
```

### 4. get_available_functions
利用可能な数学関数の一覧を返します。

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "tools/call",
  "params": {
    "name": "get_available_functions",
    "arguments": {}
  }
}
```

## サポートされている計算

### 基本演算
- `+`, `-`, `*`, `/`, `**`, `%`

### 数学関数
- `sqrt()`, `abs()`, `round()`, `pow()`
- `sin()`, `cos()`, `tan()`
- `log()`, `floor()`, `ceil()`, `factorial()`

### 数学定数
- `pi`, `e`, `tau`, `inf`

## テスト

```bash
# FastMCP版のテスト実行
python test_fastmcp_server.py
```

## セキュリティ

元のバージョンと同様のセキュリティ機能を維持：
- 危険な操作の検出と拒否
- 制限された関数セットのみ使用可能
- 安全な式評価

## 開発者向け情報

### FastMCPフレームワークの活用

```python
from fastmcp import FastMCP

app = FastMCP("My MCP Server")

@app.tool()
def my_function(param: str) -> str:
    """
    ツールの説明
    
    Args:
        param: パラメータの説明
    
    Returns:
        戻り値の説明
    """
    return f"結果: {param}"
```

### 型ヒントの重要性
FastMCPは型ヒントを使ってJSONスキーマを自動生成するため、適切な型注釈が重要です。

## 次のステップ

1. より多くの数学関数の追加
2. 複素数計算のサポート
3. グラフ描画機能の追加
4. 数式の可視化

## 関連ファイル

- `mcp_calculator_server.py` - 元のバージョン
- `fastmcp_calculator_server.py` - FastMCP版（このファイル）
- `test_fastmcp_server.py` - FastMCP版テストスクリプト