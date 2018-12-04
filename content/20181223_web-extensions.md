Title: WebExtensions とブラウザ拡張機能、Slack への直接絵文字登録の仕組み
Date: 2018-12-23 00:00
Modified: 2018-12-23 00:00
Slug: web-extensions

<a href="{filename}/20181223_web-extensions.md" rel="bookmark">
  <img src="{static}/images/20181223/thumbnail.png" width="300" height="130" alt="ブラウザ拡張機能">
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
次に、<a href="https://emoji-gen.ninja/" rel="bookmark">絵文字ジェネレーター</a> のブラウザ拡張機能で使われている WebExtensions API について説明します。

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

Firefox の拡張機能を公開する際、Webpack などのモジュールバンドラーを使ったり minify したりした場合は、元のソースコードの提出が義務付けられています (<a href="https://developer.mozilla.org/ja/docs/Mozilla/Add-ons/Source_Code_Submission" target="_blank" rel="noopener">ソースコードの提出 - Mozilla</a>)。これは、Mozilla 側が拡張機能をレビューする際に必要なためです。

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
### cheerio によるスクレイピング
### Contents scripts とウェブページ間の通信
### Background scripts と Contents scripts 間の通信

## まとめ
