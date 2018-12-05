Title: WebExtensions とブラウザ拡張機能、Slack への直接絵文字登録の仕組み
Date: 2018-12-23 00:00
Modified: 2018-12-23 00:00
Slug: web-extensions

<a href="{filename}/20181223_web-extensions.md" rel="bookmark">
  <img src="{static}/images/20181223/thumbnail.png" width="300" height="110" alt="ブラウザ拡張機能">
</a>

<small>このブログは、<a href="https://adventar.org/calendars/2959" target="_blank" rel="noopener">高知工科大学 Advent Calendar 2018</a> の13日目の記事です。</small>

<a href="https://emoji-gen.ninja/" target="_blank" rel="bookmark">絵文字ジェネレーター</a> では、<a href="https://www.google.co.jp/chrome/" target="_blank" rel="noopener">Google Chrome</a> や Firefox 向けにブラウザ拡張機能を提供しています。ブラウザ拡張機能を使うと、絵文字をダウンロードするだけではなく、所属する Slack チームのカスタム絵文字としてブラウザから直接登録することができます。

この記事では、絵文字ジェネレーターのブラウザ拡張機能を紹介した後、そのブラウザ拡張機能を作るのに使われている WebExtensions API について解説します。

WebExtensions API は特定のブラウザに縛られない拡張機能開発のための API で、Google Chrome や Firefox、Microsoft Edge でサポートされています。

次に、実際のブラウザ拡張機能の中で、どのようにして Slack へ直接絵文字を登録しているのかを解説します。絵文字ジェネレーターのブラウザ拡張機能は TypeScript で記述されています。記事中では具体的なコードを絡めて説明していこうと思います。

<!-- PELICAN_END_SUMMARY -->

## ブラウザ拡張機能の紹介
まずはじめに、絵文字ジェネレーターのブラウザ拡張機能について紹介します。

### 絵文字ジェネレーターと Slack
<a href="https://emoji-gen.ninja/" target="_blank" rel="bookmark">絵文字ジェネレーター</a> では、より便利にサービスを使ってもらうため、ブラウザ拡張機能を提供しています。絵文字ジェネレーターは、チャットなどのリアクションに使う画像の生成を想定して開発しています。チャットツールは複数ありますが、その中でも <a href="https://slack.com/" target="_blank" rel="noopener">Slack</a> がメインターゲットです。

Slack は IT 系の会社を中心に、幅広く使われているチャットサービスです。Slack は、チーム (組織) ごとにユーザーアカウントが独立しており、個人間よりも会社などの組織内で使われることを前提としています。

Slack のチャットツールとしての特徴は、発言に対するリアクションです。SNS の『 いいね 』のような気軽さで、よりレパートリーに富んだ感情を表すことができます。

標準では &#x1F44D; や &#x1F607; などの <a href="https://unicode.org/emoji/charts/full-emoji-list.html" target="_blank" rel="noopener">Unicode Emoji</a> をリアクションとして利用できます。さらに、任意の画像をカスタム絵文字として登録し、リアクションとして用いることもできます。

そのカスタム絵文字の画像生成を目的としたサービスが絵文字ジェネレーターであり、その登録作業を効率化するために開発したのが絵文字ジェネレーターのブラウザ拡張機能です。これよってカスタム絵文字がより気軽に作れるようになることにより、チャット上のコミュニケーションが活発になることを目指しています。

### ブラウザ拡張機能の機能
ブラウザ拡張機能を使うと、絵文字ジェネレーターで絵文字を生成した後、ブラウザから直接所属する Slack チームへ絵文字を登録することができます。今まで行っていた『 生成した PNG 画像をダウンロードしてから、Slack の絵文字登録画面を開き、登録する 』といった手順が不要となります。

説明するより使ったほうが早いと思いますので、ぜひインストールして使ってみてください。対応しているブラウザは、Google Chrome と Firefox です。

- <a href="https://chrome.google.com/webstore/detail/%E7%B5%B5%E6%96%87%E5%AD%97%E3%82%B8%E3%82%A7%E3%83%8D%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC/ghbhakkknnmocmiilhneahbkiaegdnmf?hl=ja&gl=JP" target="_blank" rel="noopener">Google Chrome 版 - Chrome ウェブストア</a>
- <a href="https://addons.mozilla.org/ja/firefox/addon/emoji-generator/" target="_blank" rel="noopener">Firefox 版 - Firefox Add-ons</a>

拡張機能をインストール後、絵文字ジェネレーターの『 登録する 』ボタンを押すと、そのブラウザからログインしている Slack チームが一覧表示されます。このブラウザ拡張機能自体は、既にログイン済みの Slack チームのセッションを流用しているので、特に認証情報の登録は不要です。

この状態で絵文字名を入力し『 登録する 』を押すと、自動的に絵文字が登録されます。

絵文字ジェネレーターのブラウザ拡張機能は、GitHub 上でオープンソースで開発されています。ご興味のある方は <a href="https://github.com/emoji-gen/browser-extension" target="_blank" rel="noopener">emoji-gen/browser-extension</a> からご覧ください。

## WebExtensions API について
次に、<a href="https://emoji-gen.ninja/" target="_blank" rel="bookmark">絵文字ジェネレーター</a> のブラウザ拡張機能で使われている WebExtensions API について説明します。

### WebExtensions API の成り立ちと概要
元々、ブラウザ拡張機能というのはブラウザごと別々の仕様に沿って作る必要がありました。

Firefox には遥か昔から拡張機能というものが存在し、XUL/XPCOM や Add-on SDK などの仕様に沿って JavaScript や C++ で開発してきました。これらの技術で作られた拡張機能は、他のブラウザでは動作しませんでした。

Google Chrome にも JavaScript でブラウザ拡張機能を作る API が存在していました。これらの API は Firefox の拡張機能 API との互換性は全くありませんでした。

そこで登場したのが WebExtensions API です。WebExtensions API は、ブラウザごとにバラバラだった API を統一し、一つの拡張機能で複数のブラウザに対応可能にしました。開発者にとってはありがたい限りです。

とはいっても、WebExtensions API は Google Chrome の拡張機能 API を元にしており、細かい違いはありますが基本的に同一です。Google Chrome の拡張機能が Firefox でも動くようになった、という言い方がより現実に即しているかもしれません。

### WebExtensions API のブラウザ対応状況
WebExtensions API は主要ブラウザでは Google Chrome、Firefox、Microsoft Edge が対応しています。また、Chromium ベースの Opera (バージョン 15 以降) などのブラウザでも利用できます。

現在、絵文字ジェネレーターの拡張機能は Microsoft Edge に対応していません。これは、対応を検討した時期の Microsoft Edge の WebExtensions API の対応が不十分であったためです。現在は改善しているかもしれません。

もしくは、<a href="https://www.windowscentral.com/microsoft-building-chromium-powered-web-browser-windows-10" target="_blank" rel="noopener">Microsoft Edge が Chromium ベースになる</a> などの事が本当に起きた場合、実装差異は気にしなくて良くなるかもしれません。

## TypeScript による拡張機能開発
絵文字ジェネレーターのブラウザ拡張機能は TypeScript を使って開発されています。

TypeScript を使って開発する際に気になるのが型定義ファイルです。Google Chrome の拡張機能向けの型定義ファイルはコミュニティ <a href="https://github.com/DefinitelyTyped/DefinitelyTyped" target="_blank" rel="noopener">DefinitelyTyped</a> で開発され npm 上に <a href="https://www.npmjs.com/package/@types/chrome" target="_blank" rel="noopener">@types/chrome</a> として公開されています。利用する際は `npm` または `yarn` コマンドを用い、プロジェクトの依存に加えます。

```
$ npm install --save-dev @types/chrome # for NPM users
$ yarn add --dev @types/chrome         # for Yarn users
```

TypeScript で書かれたソースコードは、最終的に Webpack と gulp を用いて JavaScript にビルドされます。もしあなたが Webpack などのモジュールバンドラを使って Firefox の拡張機能を作る場合、注意が必要な所があります。

Firefox の拡張機能を公開する際、Webpack などのモジュールバンドラーを使ったり minify したりした場合は、元のソースコードの提出が義務付けられています (<a href="https://developer.mozilla.org/ja/docs/Mozilla/Add-ons/Source_Code_Submission" target="_blank" rel="noopener">ソースコードの提出 - MDN</a>)。これは、Mozilla 側が拡張機能をレビューする際に必要なためです。

絵文字ジェネレーターでは、gulp のタスクを使って Firefox のストアへ提出する .zip とは別に、ソースコードのみ含まれた .zip を生成して、それを提出するようにしています。

```javascript
gulp.task('zip-archive', () =>
  gulp.src('dist/extension/**/*')
    .pipe(zip('archive.zip'))
    .pipe(gulp.dest('dist'))
)

 gulp.task('zip-source', () =>
   gulp.src([
     'assets/**/*',
     'src/**/*',
     'test/**/*',
     '.node-version',
     '.editorconfig',
     '.gitignore',
     '*.js',
     '*.json',
     '*.yml',
     '*.md',
     'yarn.lock',
     'LICENSE',
   ], { base: '.' })
     .pipe(zip('source.zip'))
     .pipe(gulp.dest('dist'))
)

gulp.task('zip', gulp.parallel('zip-archive', 'zip-source'))
```

## 絵文字の Slack 直接登録機能の実装
最後に、絵文字ジェネレーターの拡張機能がどのように実装されているか、説明します。

### Fetch API と cheerio によるスクレイピング
<a href="https://emoji-gen.ninja/">絵文字ジェネレーター</a> のブラウザ拡張機能は、Slack へのスクレイピングによって実現しています。絵文字登録の API は、現在 Slack 公式には提供されていません。

通常、ウェブページ上から他ドメインのコンテンツを取得することは Same-Origin Policy (<a href="https://developer.mozilla.org/ja/docs/Web/Security/Same-origin_policy" target="_blank" rel="noopener">同一オリジンポリシー - MDN</a> によって制限されています。回避するには <a href="https://developer.mozilla.org/ja/docs/Web/HTTP/CORS" target="_blank" rel="noopener">CORS</a> を利用する必要があります。CORS を使うにはリクエスト先のサーバーが対応している必要がありますが、ブラウザ拡張機能を使えばそもそも Same-Origin Policy を回避することができます。

絵文字ジェネレーターで Slack をスクレイピングしている箇所は、大きく2点あります。ログイン済みの Slack チーム一覧を取得する部分と、絵文字を実際に登録する所です。

以下は、ログイン済みの Slack チーム一覧を取得している部分です (一部省略しています)。

```typescript
export async function searchJoinedTeams(): Promise<ITeam[]> {
  const res = await fetch('https://slack.com/customize/emoji', {
    credentials: 'include',
  })
  const body = await res.text()

  const $ = cheerio.load(body)
  const teamAnchors = $('#header_team_nav li:not(#add_team_option) a').toArray()
  const teams: ITeam[] = teamAnchors
    .map(_anchor => {
      const anchor = $(_anchor)
      const href = anchor.attr('href')
      const matches = href.match(/\/\/([^\.]+)\.slack\.com/)

      if (matches) {
        return {
          name: v.trim(anchor.text()),
          teamdomain: matches[1],
        }
      }
    })
    .filter(team => !!team) as ITeam[]

  return teams
}
```

HTTPS リクエストの部分には生の <a href="https://developer.mozilla.org/ja/docs/Web/API/Fetch_API" target="_blank" rel="noopener">Fetch API</a> を利用しています。これは、ブラウザ拡張機能という特性上、サポート対象ブラウザを絞ることができるためです。Polyfill は使っていません。

HTML のパースと DOM 操作には <a href="https://github.com/cheeriojs/cheerio" target="_blank" rel="noopener">cheerio</a> を使っています。実は、ブラウザ拡張機能はそれ自体が一つのウェブページとして動作しているため、別にライブラリを使わずともドキュメントツリーに追加するだけで DOM 操作が可能です。

ただし、ドキュメントツリーに追加した HTML 中の画像は当然読み込まれますし、埋め込まれている JavaScript も意図せず実行されてしまいます。そのため、無駄なように思えますが、ブラウザ上であえて cheerio を使って HTML をパースしています。

絵文字の登録部分も、基本的に愚直にスクレイピングしているのみです。絵文字の登録は、Slack の非公開 API がありそれを叩いています。ブラウザから普通に登録する際にも、同様の API が呼ばれています。

### 拡張機能のアーキテクチャ
ブラウザ拡張機能は、ウェブページの JavaScript と同一の DOM ツリー上で動作させることができますが、隔離されています。相互に関数を呼びあうことはできません。これは、ブラウザ拡張機能開発特有の問題です。

ブラウザ拡張機能は、以下のような3レイヤー構成で作られています。レイヤー間は直接の変数参照や関数呼び出しができません。イベントベースの非同期通信によって、やりくりをする必要があります。

TODO

絵文字ジェネレーターの拡張機能は、特定のページのみで動作することを想定されています。そのため、ウェブページ自体のスクリプトと合わせ、3レイヤーすべてを相互に協調させて動くよう設計する必要があります。

それぞれのレイヤーでできることが異なります。Content scripts は、ウェブページの読み込みに連動して読み込まれます。複数のタブで開けば、タブの数だけ動作します。ウェブページのスクリプトでできることは基本すべて可能で、追加して拡張機能向けの API を一部呼び出すことができます。

Background scripts は、名前の通り裏側で動きます。拡張機能をインストールすると、多くの場合は裏側でウェブページが開かれ Background scripts が動作しています。拡張機能を入れすぎるとメモリを多く消費するのは、これが原因です。拡張機能ごとに1つだけ読み込まれ、表側の Content scripts と連携して一つの拡張機能を構成します。

Background scripts は、Content scripts とは動作してる URL が異なります (`chrome-extension://` という URL スキームで動作します)。当然、実際のウェブページの DOM も触ることができません。そのかわり、ブラウザの UI を変更したり、HTTPS リクエストに割り込んで書き換えたり、ウェブページからは不可能な操作ができます。Slack へのスクレイピングは、Background scripts で行っています。

### Content scripts とウェブページ間の通信
Content scripts とウェブページ間は、直接関数を呼び出したり、変数を共有したりできません。
その代りに DOM は共有されているので、それを利用して通信します。

ここで利用するのがカスタムイベントという仕組みです (<a href="https://developer.mozilla.org/ja/docs/Web/Guide/Events/Creating_and_triggering_events" target="_blank" rel="noopener">イベントの作成と発火 - MDN</a>)。カスタムイベントを使うと、任意の要素に対して、任意の名前のイベントを発火・待ち受けることができます。

何らかの通信を行いたい側は、予め決めておいた名前のイベントを下記のように発火させます。
`detail` はイベントに対する引数で、任意の値が渡せます。

```javascript
const event = new CustomEvent('helo', { detail: 'Hello, World!' })
window.dispatchEvent(event)
```

イベントを受け取りたい側は、通常のイベントと同じようにイベントリスナーを登録しておきます。

```javascript
window.addEventListener('helo', ({ detail }) => {
  console.log(detail)
})
```

これで、非同期ではありますが、双方向に任意タイミングで通信ができるようになります。
実際の絵文字ジェネレーターでは、カスタムイベントを軽くラップしたライブラリである <a href="https://www.npmjs.com/package/ptero" target="_blank" rel="noopener">ptero</a> を、ウェブ側とブラウザ拡張機能の双方から使っています。

### Background scripts と Contents scripts 間の通信
Background scripts と Contents scripts 間の通信は、公式の API がありそれを利用します。

- <a href="https://developer.chrome.com/apps/messaging" target="_blank" rel="noopener">Message Passing - Google Chrome</a>
- <a href="https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/sendMessage" target="_blank" rel="noopener">runtime.sendMessage() - MDN</a>

こちらの方法は、他のブログでも沢山書かれているため、サンプルコードは省きます。この API は、基本的には Background scripts と Contents scripts 間の通信を目的としていますが、他の拡張機能との通信も可能です。

## まとめ
この記事では、絵文字ジェネレーターの拡張機能の紹介や WebExtensions API、実際の拡張機能の実装について説明しました。

- 絵文字ジェネレーターのブラウザ拡張機能を使うと、Slack への登録が簡単になります
- WebExtensions はブラウザ非依存の拡張機能向け API で、Google Chrome や Firefox で動作します
- Slack への絵文字登録は、Slack をスクレイピングして実現しています
- ブラウザ拡張機能を作る際は、複数レイヤのアーキテクチャを考慮する必要があります

ブラウザ拡張機能以外にも、絵文字ジェネレーターを便利にする機能があれば、ぜひ作っていきたいと思っています。
何か案があれば、ぜひ教えてください。

今後とも、<a href="https://emoji-gen.ninja/">絵文字ジェネレーター</a> をどうぞ宜しくお願いします！
