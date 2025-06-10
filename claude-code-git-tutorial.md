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

> **人間**: 今回のプロジェクトでは、gitおよびgithubを使っての開発実験を行いたいと思います。そのためにまずは簡単なプログラムを作成します。そしてそれをgitを使って修正や差分の管理、ブランチによる開発などをハンズオンでできるようにあなたに指導していただきたいのです。よろしいですか？

> **Claude Code**: はい、もちろんです！Git/GitHubを使った開発実験のハンズオン指導をさせていただきます。まず、簡単なプログラムを作成しましょう。どのような種類のプログラムがお好みですか？

> **人間**: pythonの簡単なプログラムでいきましょう。すすめてください

> **Claude Code**: Pythonの簡単なプログラムを作成して、Git/GitHubでの開発実験を始めましょう。

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

> **Claude Code**: では、変更をコミットしましょう：
> ```bash
> git add calculator.py
> ```

> **人間**: ステージングの前に変更後のテストが必要ではないですか？

> **Claude Code**: その通りです！コミットする前にテストするのは良い習慣ですね。

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

> **人間**: マージの前に一つ前に戻ってみるテストしない？

> **Claude Code**: 素晴らしいアイデアです！Gitで過去の状態に戻る練習をしましょう。

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

> **人間**: ここまでのハンズオンがすばらしいので、これまでの流れをもとにClaude Codeによるgitの学習というテーマで記事をつくってほしいです。

> **Claude Code**: 記事を作成しました！「claude-code-git-tutorial.md」として保存されています。

> **人間**: ではこの記事を修正していきたいのでブランチを切ってください

> **Claude Code**: では、記事を修正するための新しいブランチを作成しましょう！

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