Title: WebExtensions とブラウザ拡張機能、Slack への直接絵文字登録の仕組み
Date: 2018-12-23 00:00
Modified: 2018-12-23 00:00
Slug: web-extensions

<!--
<a href="{filename}/20181127_ignited.md">
  <img src="{static}/images/20181127/thumbnail.png" width="300" height="130" alt="Pelican x Firebase Hosting">
</a>
-->

<small>このブログは、<a href="https://adventar.org/calendars/2959" target="_blank">高知工科大学 Advent Calendar 2018</a> の13日目の記事です。</small>

絵文字ジェネレーターでは、Google Chrome や Firefox 向けにブラウザ拡張機能を提供しています。ブラウザ拡張機能を使うと、絵文字をダウンロードするだけではなく、所属する Slack チームのカスタム絵文字として直接登録することができます。

この記事では、ブラウザ拡張機能を作るのに使われている WebExtensions API についてまず解説します。WebExtensions API は特定のブラウザに縛られない API で、Google Chrome や Firefox、Microsoft Edge でサポートされています。

次に、ブラウザ拡張機能の中で、具体的にどのような API も用いて Slack へ直接絵文字を登録しているのかを解説します。絵文字ジェネレーターのブラウザ拡張機能は TypeScript で記述されています。記事中では具体的なコードを絡めて説明していこうと思います。

<!-- PELICAN_END_SUMMARY -->

## 絵文字ジェネレーターのブラウザ拡張機能とは?
### 機能紹介
### 今すぐダウンロード!

## WebExtensions API とは?
### 成り立ちと概要
### ブラウザの対応状況

## TypeScript による拡張機能開発

## 絵文字の Slack 直接登録機能の実装
### cheerio によるスクレイピング
### Contents scripts とウェブページ間の通信
### Background scripts と Contents scripts 間の通信
