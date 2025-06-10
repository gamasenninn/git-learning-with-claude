# Claude CodeでGitを学ぶ：実践的ハンズオンガイド

## はじめに

プログラミングを学ぶ上で、バージョン管理システムのGitは避けて通れない重要なツールです。しかし、初心者にとってGitは概念が抽象的で、実際の動作をイメージしにくいという課題があります。

**でも大丈夫です！** この記事では、Claude Codeを使ってGitの基本操作を実践的に学ぶ方法を紹介します。Claude Codeの対話的な指導により、単なるコマンドの暗記ではなく、実際のプロジェクトを通じてGitの概念を体験的に理解できます。

> 💡 **初心者の方へ**：この記事では専門用語が出てきますが、その都度説明しますので安心してください。わからないことがあれば、Claude Codeに質問すれば丁寧に教えてくれます。

## なぜClaude CodeでGitを学ぶのか？

### 1. リアルタイムフィードバック
コマンドを実行するたびに、その結果と意味を即座に説明してもらえます。

### 2. 失敗を恐れない学習環境
間違えても、Claude Codeが適切な修正方法を教えてくれるため、安心して実験できます。**失敗は学習の一部です！**

### 3. 実践的なプロジェクトベース学習
実際に動作するプログラムを作りながら学ぶため、Gitの必要性を実感できます。

## 実際の対話で学ぶGit

### はじめの一歩：Claude Codeとの対話

実際の学習は、このような対話から始まります：

> 🙋 **人間**: 今回のプロジェクトでは、gitおよびgithubを使っての開発実験を行いたいと思います。そのためにまずは簡単なプログラムを作成します。そしてそれをgitを使って修正や差分の管理、ブランチによる開発などをハンズオンでできるようにあなたに指導していただきたいのです。よろしいですか？

> 🤖 **Claude Code**: はい、もちろんです！Git/GitHubを使った開発実験のハンズオン指導をさせていただきます。まず、簡単なプログラムを作成しましょう。どのような種類のプログラムがお好みですか？

> 🙋 **人間**: pythonの簡単なプログラムでいきましょう。すすめてください

> 🤖 **Claude Code**: Pythonの簡単なプログラムを作成して、Git/GitHubでの開発実験を始めましょう。

このように、自然な会話でGit学習を進められるのがClaude Codeの特徴です。

## 学習の流れ

### ステップ1：プロジェクトの準備

Claude Codeは、まず簡単なPythonプログラムを作成してくれます。今回は電卓プログラムを例に進めました。

> 💡 **初心者の方へ**：プログラムの内容を完全に理解する必要はありません。重要なのは「実際に動くプログラム」を使ってGitを学ぶことです。

```python
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
```

### ステップ2：Gitリポジトリの初期化

> 💡 **用語解説**：「リポジトリ」とは、プロジェクトのファイルと変更履歴を保存する場所のことです。簡単に言えば「プロジェクトの保管庫」です。

```bash
# Gitリポジトリを初期化
git init

# Gitの設定（リポジトリごと）
git config user.email "test@example.com"
git config user.name "Test User"

# ファイルをステージングエリアに追加
git add calculator.py README.md .gitignore

# 最初のコミット
git commit -m "初期コミット: 電卓プログラムを追加"
```

**ポイント**：Claude Codeは、Gitの設定が必要な場合も適切に案内してくれます。

実際、最初のコミットで以下のようなエラーが出ることがあります：

```
Author identity unknown
*** Please tell me who you are.
```

**でも慌てないでください！** Claude Codeがすぐに解決方法を教えてくれます：

```bash
git config user.email "test@example.com"
git config user.name "Test User"
```

### ステップ3：ブランチを使った機能開発

> 💡 **用語解説**：「ブランチ」とは、メインのコードから分岐した独立した作業スペースです。新機能を試したり、実験したりするための「安全な遊び場」だと考えてください。

新機能（平方根計算）を追加する際、ブランチを使って開発します。

```bash
# 新しいブランチを作成
git branch feature/sqrt-function

# ブランチを切り替え
git checkout feature/sqrt-function
```

**学習ポイント**：
- ブランチを使うことで、安全に新機能を開発できる
- masterブランチは常に動作する状態を保てる

### ステップ4：変更の確認とテスト

ここで重要な対話がありました：

> 🤖 **Claude Code**: では、変更をコミットしましょう：
> ```bash
> git add calculator.py
> ```

> 🙋 **人間**: ステージングの前に変更後のテストが必要ではないですか？

> 🤖 **Claude Code**: その通りです！コミットする前にテストするのは良い習慣ですね。

**初心者の方へ**：このように、Claude Codeに質問や提案をすることで、より良い開発習慣を身につけられます。遠慮なく質問してください！

```python
# test_calculator.py
#!/usr/bin/env python3
"""
電卓プログラムのテストスクリプト
"""
from calculator import add, subtract, multiply, divide, sqrt

print("=== 電卓機能のテスト ===")

# 平方根のテスト（新機能）
print("\n5. 平方根のテスト（新機能）")
print(f"  √16 = {sqrt(16)}")
print(f"  √25 = {sqrt(25)}")
print(f"  √2 = {sqrt(2):.4f}")

# エラーケースのテスト
print("\n6. エラーケースのテスト")
try:
    sqrt(-4)
except ValueError as e:
    print(f"  負の数の平方根: {e}")
```

### ステップ5：差分の確認とコミット

```bash
# 変更内容を確認
git diff

# 変更をステージング
git add calculator.py test_calculator.py

# 意味のあるコミットメッセージで記録
git commit -m "feat: 平方根計算機能を追加

- sqrt()関数を実装
- メニューに平方根オプションを追加
- エラーハンドリング（負の数）を実装
- テストスクリプトを追加"
```

### ステップ6：過去の状態への移動（実験的学習）

実際の対話例：

> 🙋 **人間**: マージの前に一つ前に戻ってみるテストしない？

> 🤖 **Claude Code**: 素晴らしいアイデアです！Gitで過去の状態に戻る練習をしましょう。

Gitの強力な機能の一つは、過去の状態を自由に確認できることです。**失敗しても元に戻せる**ので、安心して実験できます！

```bash
# 過去のコミットを確認
git log --oneline

# 特定のコミットに移動（一時的）
git checkout a48b4ec

# 元のブランチに戻る
git checkout feature/sqrt-function

# コミットを取り消す（変更は保持）
git reset --soft HEAD~1
```

**注意点**：Claude Codeは各コマンドの危険性も適切に説明してくれます。

> ⚠️ **重要**：`git reset --hard`は変更を完全に削除するので危険です。Claude Codeは常にこのような危険なコマンドについて警告してくれます。

### ステップ7：ブランチのマージ

> 💡 **用語解説**：「マージ」とは、ブランチで行った変更をメインのコードに統合することです。「実験が成功したので本番に反映する」イメージです。

```bash
# masterブランチに切り替え
git checkout master

# featureブランチをマージ
git merge feature/sqrt-function

# 不要になったブランチを削除
git branch -d feature/sqrt-function
```

## Claude Codeならではの学習体験

### 実際の対話から学ぶ

学習の最後には、このような対話もありました：

> 🙋 **人間**: ここまでのハンズオンがすばらしいので、これまでの流れをもとにClaude Codeによるgitの学習というテーマで記事をつくってほしいです。

> 🤖 **Claude Code**: 記事を作成しました！「claude-code-git-tutorial.md」として保存されています。

> 🙋 **人間**: ではこの記事を修正していきたいのでブランチを切ってください

> 🤖 **Claude Code**: では、記事を修正するための新しいブランチを作成しましょう！

このように、**学んだことをすぐに実践**できるのもClaude Codeの魅力です。

### 1. TodoListによる体系的な学習
Claude Codeは内部でTodoListを管理し、学習の進捗を把握しながら指導してくれます。

### 2. エラーからの学び
例えば、Gitの設定忘れなどのエラーが発生しても、その解決方法を即座に教えてくれます。

### 3. ベストプラクティスの自然な習得
- コミット前のテスト
- 意味のあるコミットメッセージ
- ブランチ戦略

これらが自然に身につきます。

## 実践的な学習のコツ

### 1. 実際のプロジェクトで学ぶ
抽象的なファイルではなく、実際に動作するプログラムを使うことで、Gitの価値を実感できます。

### 2. 失敗を恐れない
Claude Codeがサポートしてくれるので、様々なコマンドを試してみましょう。

> 💡 **初心者の方へ**：間違ったコマンドを実行しても、Claude Codeが優しく修正方法を教えてくれます。失敗は成功への第一歩です！

### 3. 「なぜ」を理解する
Claude Codeに「なぜこのコマンドを使うのか」を質問することで、深い理解が得られます。

## 次のステップ

この基本的な学習を終えたら、以下のトピックに挑戦してみましょう：

1. **コンフリクトの解決**
   - 複数のブランチで同じファイルを編集
   - マージコンフリクトの解決方法

2. **GitHubとの連携**
   - リモートリポジトリの設定
   - push/pullの実践
   - プルリクエストの作成

3. **高度なGit操作**
   - `git rebase`によるコミット履歴の整理
   - `git stash`による一時的な変更の保存
   - `git cherry-pick`による特定コミットの取り込み

---

# 実践編：本格的な開発ワークフローを体験する

基本的なGit操作を覚えたら、次は**実際の開発現場で使われているワークフロー**に挑戦してみましょう。ここからは、より実践的で本格的な内容になります。

## Issue駆動開発：プロフェッショナルなワークフロー

### なぜIssue駆動開発なのか？

実際の開発現場では、以下のような流れで開発が進みます：

1. **問題・要望の発見** → Issue作成
2. **解決方法の検討** → ブランチ作成
3. **実装・テスト** → コミット
4. **レビューと統合** → プルリクエスト
5. **完了** → Issue自動クローズ

この流れを「**Issue駆動開発**」と呼び、多くのプロジェクトで採用されています。

### 実際の体験：MCPサーバーの開発

では、実際に体験した例を見てみましょう：

#### Issue #2：MCPサーバーサンプルの要望

> 🙋 **人間**: では次のISSUEをお願いします。

> 🤖 **Claude Code**: 素晴らしい！次のIssueを作成しましょう。

**Issue #2の内容：**
```
タイトル: MCPサーバーを学習するための簡単なサンプルを作成
・計算する機能
・uvでGitHubを指定して実行できること
```

#### ワークフローの実践

1. **Issue確認と理解**
   ```bash
   # Issue #2の内容を正確に把握
   # 要件：MCPサーバー + 計算機能 + uv対応
   ```

2. **専用ブランチの作成**
   ```bash
   git checkout -b feature/2-simple-mcp-server
   ```

3. **実装とテスト**
   - MCPサーバーの実装
   - 包括的なテストスクリプト作成
   - ドキュメント作成

4. **コミット（重要なポイント）**
   ```bash
   git commit -m "feat: Issue #2 - 簡単なMCPサーバーサンプルを追加

   - 計算機能を持つMCPサーバーを実装
   - JSON-RPC 2.0プロトコルに準拠
   - uvで実行可能なpyproject.toml設定
   - 安全な計算式評価機能
   - 包括的なテストスクリプト付き

   Closes #2"
   ```

   **注目**：`Closes #2`により、マージ時にIssueが自動クローズされます！

5. **プルリクエスト作成とマージ**
   - 詳細な説明文
   - テスト結果の報告
   - Issue #2の自動クローズ確認

### 学んだプロフェッショナルスキル

- **Issue番号をブランチ名に含める**：`feature/2-simple-mcp-server`
- **意味のあるコミットメッセージ**：何を、なぜ、どのように
- **自動Issue管理**：`Closes #2`でワークフロー自動化
- **包括的なドキュメント**：README、テスト、使用例

## GitHub連携：チーム開発の基盤

### GitHubとの初回接続

実際の開発では、ローカルで作ったプロジェクトをGitHubで共有します。

#### Personal Access Tokenの設定

> 🙋 **人間**: Password

> 🤖 **Claude Code**: GitHubのユーザー名とPersonal Access Token（PAT）を入力する必要があります。

**重要**：2021年8月以降、GitHubはパスワード認証を廃止。Personal Access Tokenが必須です。

```bash
# リモートリポジトリの設定
git remote add origin https://github.com/ユーザー名/リポジトリ名.git

# 認証情報付きURL（セキュリティに注意）
git remote set-url origin https://ユーザー名:トークン@github.com/ユーザー名/リポジトリ名.git

# 初回プッシュ
git push -u origin master
```

#### 認証トラブルシューティング

実際に遭遇したエラーと解決法：

```bash
# エラー例
fatal: could not read Username for 'https://github.com': No such device or address

# 解決法
# 1. Personal Access Tokenの作成
# 2. リモートURLの更新
# 3. 再プッシュ
```

### プルリクエストのベストプラクティス

#### 効果的なプルリクエストの書き方

```markdown
## 概要
Issue #4で要望された「FastMCPを使ったバージョン」を実装しました。

## 🚀 主な改善点
- コード量30%削減（180行→120行）
- 機能4倍増（1ツール→4ツール）

## ✅ テスト結果
- 9つの基本計算テストが成功
- 4つのエラーハンドリングテストが成功

Closes #4
```

### 複数Issueの管理

実際に体験した流れ：

```bash
# Issue #2 → PR #3 → マージ → Issue #2クローズ
# Issue #4 → PR #5 → マージ → Issue #4クローズ
```

## FastMCPフレームワーク：技術選択と移行

### Issue #4：フレームワーク移行の体験

#### 技術的挑戦

> 🙋 **人間**: 簡単なMCPサーバー FastMCPを使ったバージョン #4

**課題**：既存のMCPサーバー（180行）をFastMCPを使ってリファクタリング

#### リファクタリングの成果

| 項目 | 元のバージョン | FastMCP版 |
|------|--------------|-----------|
| **コード量** | ~180行 | ~120行 |
| **可読性** | 手動JSON-RPC処理 | デコレーターベース |
| **ツール数** | 1個 | 4個 |
| **型安全性** | 低い | 高い |

#### 実装の比較

**元のバージョン（手動実装）：**
```python
async def handle_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
    if message.get("method") == "tools/call":
        params = message.get("params", {})
        # 手動でJSONスキーマを処理...
```

**FastMCP版（フレームワーク活用）：**
```python
@app.tool()
def calculate(expression: str) -> str:
    """数学的な計算を実行します"""
    # 自動でJSONスキーマ生成、エラーハンドリング
```

### 新機能の追加

FastMCP版では以下の機能を追加：

1. **calculate_advanced**: 高精度計算
2. **get_math_constants**: 数学定数一覧
3. **get_available_functions**: 利用可能関数一覧
4. **複素数計算サポート**

### テスト戦略の進化

```python
# 模擬テスト（FastMCP不要環境対応）
def mock_safe_calculate(expression: str):
    # FastMCPが利用できない環境でもテスト可能
```

## プロジェクトの成長過程

### コミット履歴から見る進化

```bash
git log --oneline --graph -8
```

```
*   1cdc3b6 Merge pull request #5 (FastMCP版)
|\  
| * 0cdd660 feat: Issue #4 - FastMCP版追加
|/  
*   362ff9e Merge pull request #3 (MCP版)  
|\  
| * 2a3f949 feat: Issue #2 - MCP版追加
|/  
*   e64c613 Merge pull request #1 (累乗機能)
|\  
| * 85cfb1d feat: 累乗計算機能を追加
|/  
* 349e7fc style: 対話アイコン追加
* 5999744 improve: 記事に対話例追加
```

### プロジェクト構成の進化

**最終的なファイル構成：**
```
├── calculator.py              # 基本電卓
├── mcp_calculator_server.py   # MCP版
├── fastmcp_calculator_server.py # FastMCP版
├── test_*.py                  # 各種テスト
├── *_README.md               # ドキュメント
├── claude-code-git-tutorial.md # この記事
└── pyproject.toml            # パッケージ設定
```

## 学習の成果と次へのステップ

### 習得したプロフェッショナルスキル

1. **Issue駆動開発**
   - 要求分析からクローズまでの完全なサイクル
   - 自動Issue管理（`Closes #N`）

2. **GitHub連携**
   - Personal Access Token認証
   - プルリクエストのベストプラクティス
   - リモートリポジトリ管理

3. **技術的挑戦**
   - フレームワーク移行
   - リファクタリング
   - 包括的テスト戦略

4. **プロジェクト管理**
   - ドキュメント管理
   - バージョン管理
   - 継続的改善

### 実際の開発現場との対比

今回体験したワークフローは、実際の企業やOSSプロジェクトで日常的に使われているものです：

- **スタートアップ企業**: Issue駆動で迅速な機能開発
- **大企業**: 厳格なレビュープロセス
- **OSSプロジェクト**: コミュニティ主導の開発

### 次の挑戦に向けて

この実践編を通じて、あなたは単なるGit初心者から、**実際の開発現場で通用するスキル**を身につけました。

**次のレベル：**
- CI/CDパイプライン
- コードレビュー文化
- アジャイル開発手法
- オープンソース貢献

## まとめ

### 初心者の方へのメッセージ

Gitは最初は難しく感じるかもしれません。でも、**それは誰もが通る道**です。私も最初は「コミット」「ブランチ」「マージ」といった用語に戸惑いました。

しかし、Claude Codeと一緒なら：
- わからないことは何度でも質問できます
- 間違えても優しく教えてもらえます  
- 自分のペースで学習できます
- 実際に手を動かしながら理解できます

**あなたも必ずGitを使いこなせるようになります！**

### Claude CodeでGitを学ぶことで得られるもの

- **実践的**：実際のプロジェクトを通じて学べる
- **安全**：失敗しても適切なサポートが得られる
- **体系的**：段階的に概念を理解できる
- **インタラクティブ**：疑問をすぐに解決できる

Gitは最初は難しく感じるかもしれませんが、Claude Codeと一緒に学ぶことで、楽しく効率的にマスターできます。ぜひ、自分のプロジェクトでも試してみてください！

---

## 付録：今回使用した主なGitコマンド

| コマンド | 説明 | 使用例 |
|---------|------|--------|
| `git init` | リポジトリを初期化 | `git init` |
| `git add` | ファイルをステージング | `git add calculator.py` |
| `git commit` | 変更を記録 | `git commit -m "メッセージ"` |
| `git branch` | ブランチ操作 | `git branch feature/new` |
| `git checkout` | ブランチ切り替え | `git checkout master` |
| `git diff` | 差分表示 | `git diff` |
| `git log` | 履歴表示 | `git log --oneline` |
| `git merge` | ブランチ統合 | `git merge feature/new` |
| `git reset` | コミット取り消し | `git reset --soft HEAD~1` |

## 最後に：あなたへのエール

「Gitは難しそう...」と思っているあなたへ。

大丈夫です。この記事で紹介した方法なら、きっと楽しくGitを学べます。Claude Codeは、あなたの「わからない」に寄り添い、「できた！」の瞬間まで一緒に歩んでくれる頼もしいパートナーです。

**今すぐClaude Codeを開いて、「Gitを教えて」と話しかけてみてください。**

あなたのプログラミング人生が、より豊かになることを心から願っています。

Happy Coding with Claude Code! 🚀