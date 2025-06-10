# Claude CodeでGitを学ぶ：実践的ハンズオンガイド

## はじめに

プログラミングを学ぶ上で、バージョン管理システムのGitは避けて通れない重要なツールです。しかし、初心者にとってGitは概念が抽象的で、実際の動作をイメージしにくいという課題があります。

この記事では、Claude Codeを使ってGitの基本操作を実践的に学ぶ方法を紹介します。Claude Codeの対話的な指導により、単なるコマンドの暗記ではなく、実際のプロジェクトを通じてGitの概念を体験的に理解できます。

## なぜClaude CodeでGitを学ぶのか？

### 1. リアルタイムフィードバック
コマンドを実行するたびに、その結果と意味を即座に説明してもらえます。

### 2. 失敗を恐れない学習環境
間違えても、Claude Codeが適切な修正方法を教えてくれるため、安心して実験できます。

### 3. 実践的なプロジェクトベース学習
実際に動作するプログラムを作りながら学ぶため、Gitの必要性を実感できます。

## 学習の流れ

### ステップ1：プロジェクトの準備

まず、簡単なPythonプログラムを作成します。今回は電卓プログラムを例に進めました。

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

### ステップ3：ブランチを使った機能開発

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

Claude Codeの素晴らしい点は、コミット前にテストの重要性を教えてくれることです。

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

Gitの強力な機能の一つは、過去の状態を自由に確認できることです。

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

### ステップ7：ブランチのマージ

```bash
# masterブランチに切り替え
git checkout master

# featureブランチをマージ
git merge feature/sqrt-function

# 不要になったブランチを削除
git branch -d feature/sqrt-function
```

## Claude Codeならではの学習体験

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

## まとめ

Claude CodeでGitを学ぶことで、以下のメリットがあります：

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

この記事が、あなたのGit学習の第一歩となることを願っています。Happy Coding with Claude Code! 🚀