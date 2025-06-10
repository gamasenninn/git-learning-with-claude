# 簡単なMCPサーバーサンプル - 計算機能付き

## 概要
Model Context Protocol (MCP) の学習用サンプルサーバーです。基本的な計算機能を提供します。

## 機能
- 基本的な数学計算
- 安全な式評価
- MCP標準に準拠したJSON-RPC通信

## サポートされている計算
- **基本演算**: `+`, `-`, `*`, `/`, `**`, `%`
- **関数**: `sqrt()`, `abs()`, `round()`, `pow()`
- **三角関数**: `sin()`, `cos()`, `tan()`
- **定数**: `pi`, `e`

## インストールと実行

### uvを使用して直接実行
```bash
# GitHubから直接実行
uv run --from git+https://github.com/gamasenninn/git-learning-with-claude.git mcp-calculator

# ローカルで実行
uv run python mcp_calculator_server.py
```

### 手動実行
```bash
python mcp_calculator_server.py
```

## 使用例

### JSON-RPCメッセージの例

#### 初期化
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {}
}
```

#### ツール一覧の取得
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/list"
}
```

#### 計算の実行
```json
{
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
```

## テスト用スクリプト
```bash
# 基本計算のテスト
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}' | python mcp_calculator_server.py

echo '{"jsonrpc": "2.0", "id": 2, "method": "tools/list"}' | python mcp_calculator_server.py

echo '{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "calculate", "arguments": {"expression": "sqrt(16) + 2 * 3"}}}' | python mcp_calculator_server.py
```

## セキュリティ
- 危険な操作（import、exec等）は禁止
- 制限された関数セットのみ使用可能
- 入力検証を実装

## MCP仕様への準拠
- JSON-RPC 2.0プロトコル
- initialize/tools/list/tools/callメソッドをサポート
- エラーハンドリング実装