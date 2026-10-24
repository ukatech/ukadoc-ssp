# その他の機能

ここでは、その他の雑多な機能や実験的機能について説明します。

## MCPサーバ対応機能

伺か関連で利用できるMCP (Model context protocol) サーバには、SSPに内蔵されているもののほか、仕様書やゴーストを検索するためのオンラインのものがあります。

### SSP内蔵のMCPサーバ

SSPはMCPサーバとしてふるまうことができ、AI(LLM)からのSakuraScript実行やプロパティシステムの読み取りなどが可能です。<br>
この機能を使用するためには、SSPを起動した状態で、[127.0.0.1:9801/api/mcp/help](http://127.0.0.1:9801/api/mcp/help)を開き、説明を読んで、`claude_desktop_config.json`などに適切に追加してみてください。<br>
今のところ以下の機能が利用可能です。

- `get_active_ghost_list` - アクティブなゴースト(キャラクター)のリストを取得する
- `get_status` - ゴーストごとの現在の状態(会話中・選択肢待ちなど)を取得する。SSTP EXECUTE GetStatus相当
- `get_expression_table` - 特定のゴースト(キャラクター)で使える表情リストを取得する
- `get_property` - プロパティシステムの値を取得する
- `get_log` - エラーログ・スクリプトログ・ネットワークログ・更新ログ・ステータスログを取得する。ゴースト名や前回取得分以降(`since_id`)での絞り込みが可能
- SakuraScript - SakuraScriptを実行する。strictを指定すると、SSTPのOption: strictと同様に存在しないサーフィス等の指定がエラーログに記録され、`get_log`で確認できる
- `raise_event` - SHIORIイベントを発生させ(SSTP NOTIFYのEvent相当)、ゴーストが返したスクリプトを再生する。返されたスクリプトは結果にも含まれる。strict指定可
- reload - ゴースト・SHIORI(辞書)・シェル・バルーンなどを再読み込みする。読み込み中のエラーは`get_log`で確認できる
- `dump_surface` - キャラクターの画像(透過PNG)を取得する。サーフィスIDを省略すると現在表示中の姿(拡大縮小・透明度の適用前)を、指定するとそのサーフィス単体を初期状態で描画したものを返す。`\![execute,dumpsurface]`相当で、1回1枚
- `dump_balloon` - バルーンの画像(透過PNG)を取得する。最後に描画された状態を返す。`\![execute,dumpballoon]`相当。hideにballoonmarker・balloonnumを指定すると、それを除いて描き直したものを返す(2.9.08以降)

MCPサーバはローカル専用の機能のため、SakuraScriptなどで送ったスクリプトは対象ゴースト自身の処理(Owned SSTP)と同様に扱われ、`\![reload,...]`なども実行できます。<br>
ゴーストを指定する引数(`ghost_name`)には、ゴースト名のほか、ゴーストのルートフォルダ(ghostとshellを含むフォルダ)のフルパスも指定できます。

### 伺かの仕様をMCPで探せるようにする

UKADOC・YAYA Wiki・里々Wiki・蒼空Wikiを検索できるMCPサーバがあります。<br>
オンライン版を使う場合は、以下のURLをリモートMCPサーバ(カスタムコネクタなど)として追加してください。<br>
<https://ssp.shillest.net/ukadoc/mcp><br>
手元で動かしたい場合は、オンライン版の元になっているukagaka-doc-mcpをインストールして、適切に設定してください。<br>
<https://github.com/finelagusaz/ukagaka-doc-mcp>

### ゴーストをMCPで探せるようにする

ゴースト検索サイト(<https://buynowforsale.shillest.net/ghosts/>)と同等の検索ができるMCPサーバがあります。以下のURLをリモートMCPサーバとして追加してください。公開情報のみを扱うため、認証の設定は不要です。<br>
<https://buynowforsale.shillest.net/ghosts/mcp><br>
詳しくは[こちら](https://buynowforsale.shillest.net/ghosts/about.html#mcp)を参照してください。

### AIエージェントに設定してもらう

Claude Code・Codex CLI・Cursorなど、手元のPCで動くAIエージェントを使っている場合は、SSPを起動した状態で、エージェントに次のように頼むと設定してもらえます。

```
SSPのMCPサーバを使えるようにしたい。http://127.0.0.1:9801/api/mcp/help を読んで、あなた自身のMCP設定に追加して。
```

ブラウザ上で動くAI(claude.aiなど)からは127.0.0.1に接続できないため、この方法は使えません。

#### AIエージェント向けの設定手順

1. `http://127.0.0.1:9801/api/mcp/help` を取得する。接続できない場合はSSPが起動していないため、ユーザーに起動を依頼する。
2. ページ内のJSONにあるmcp.exeのフルパスをcommandとし、引数なしのstdio形式MCPサーバとして、自身のMCP設定に追加する。JSONはClaude Desktop用の例なので、自身の設定形式に読み替えること。
3. ユーザーが望めば、上記のオンラインMCPサーバ(<https://ssp.shillest.net/ukadoc/mcp> と <https://buynowforsale.shillest.net/ghosts/mcp>)もリモートMCPサーバとして追加する。
4. 設定の反映に再起動や新しいセッションが必要な場合は、その旨をユーザーに伝える。

## AIエージェントでゴーストを作りたい(Vibe Coding)

YAYA用ゴーストテンプレート「紺野ややめ」に、AIコーディングエージェント向けの開発キット(Vibe Coding Toolkit)が含まれています。<br>
AIエージェント向けの指示書(AGENTS.md)や、辞書・surfaces.txtの検証手順などが一通りそろっています。<br>
<https://github.com/YAYA-shiori/konnoyayame><br>
リポジトリをzipで取得したものは不完全なため、Releasesからダウンロードしてください。<br>
キット内部で使用している、SSPの--dump-error-logによるシェルのチェックや、[デバッグツールtama](https://github.com/YAYA-shiori/tama/blob/master/docs/README_JP.md)のtamacによる辞書のチェックの手順は、[ゴーストの一括チェック(check.md)](https://github.com/YAYA-shiori/konnoyayame/blob/master/docs/agents/workflows/check.md)と[開発コマンド一覧(commands.md)](https://github.com/YAYA-shiori/konnoyayame/blob/master/docs/agents/commands.md)を参照してください。
