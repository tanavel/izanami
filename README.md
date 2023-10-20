
<div align="center">
  <a href="https://github.com/tanavel/izanami">
    <img src="images/mochi1.jpeg" alt="logo" width="500">
  </a>
  <p>たなべるのMacの設定あれこれ。ロゴは「もち」だよ。</p>
</div>

## Built With
- [Ansible](https://github.com/ansible/ansible)

## Getting Started
### Prerequisites
- Homebrew
    - インストール方法は[公式ドキュメント](https://brew.sh/index_ja)参照
- Ansible
    ```sh
    brew install ansible
    ```

### Installation
1. リポジトリをclone
    ```sh
    git clone git@github.com:tanavel/izanami.git
    ```
1. カレントディレクトリを移動
    ```sh
    cd izanami
    ```

## Usage
### 自動化できている系
- 全部実行
    ```sh
    ansible-playbook playbook.yml --ask-become-pass
    ```

- 一部だけ実行 (タグを指定)
    ```sh
    ansible-playbook playbook.yml -t package
    ```

- 使えるタグ
    | 名前 | 説明 |
    |---|---|
    | package  | CLIアプリ、GUIアプリ、フォント |
    | homebrew |packageと一緒 |
    | terminal | ターミナル環境全般[^1] |
    | zsh | zshの設定[^1] |
    | vim | vimの設定 |
    | iterm | iTermの設定 |

[^1]: デフォルトshellの変更をするため`--ask-become-pass`オプションをつけること

### VSCodeの設定
#### Import
- VSCodeを開く
- コマンドパレットに`>profiles: import profile`と入力し、[profiles: import profile...]をクリック
- [Select File...]をクリック
- [editor/general.code-profile]をクリック
- [Create Profile]をクリック
- [Create]をクリック
- VSCodeを再起動
- 完了🎉🎉🎉

#### Export
- VSCodeを開く
- コマンドパレットに`>profiles: export profile`と入力し、[Profiles: Export Profile...]をクリック
- [設定]と[拡張機能]だけにチェックが入った状態にし、[エクスポート]をクリックする
- [ローカル]をクリックする
- 保存先を[editor/]に指定し保存する
- 完了🎉🎉🎉

## Roadmap
- [ ] Macの設定もdefaultsコマンドで自動化したいよ
- [ ] 自動化できないけど新しいMacを手に入れたらやっておきたいことリストも作りたいよ
- [ ] Chromeの拡張機能もインストールできるようにしたいよ
- [ ] Apple Storeからのインストールも自動化したいよ
- [ ] zsh環境をもうちょいリッチにしたいよ
    - [ ] lsコマンドをおしゃれにしたり
    - [ ] コマンドの予測を賢くしたり
- [ ] gitの設定
- [ ] 変数ファイルの場所のネストが深いのでhost_varsみたいな感じで浅いところで一括で設定したい

## Contact
tanavel - [@t4n4v3l_work](https://twitter.com/t4n4v3l_work)
