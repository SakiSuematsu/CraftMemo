# こどもの工作を写真、動画、3Dデータで保存、閲覧できる

## DEMO

  - https://craftlog2023.com/

## 紹介と使い方

  - ユーザー登録してログインしたら、画像を保存できるサイト
  - 更新・削除機能を追加
  - 3DデータはglTF/GLB形式を保存できる

## 工夫した点

 - Djangoにチャレンジ！Bootstrapにもチャレンジ！！
 - 3D表示にmodel-viewerというWebコンポーネントを使ってみた
 - 保存したファイルの種類ごとに横に並ぶようにした

## 苦戦した点

 - ファイルの種類ごとに並べる処理の実装に時間がかかった
 - ファイルの種類ごとに表示に使うタグが違ったため、詳細画面をそれぞれ作ることになった（もっといいやり方があったかも？）
 - 実装よりデプロイが大変だった

## やりたいこと
  - 見た目がダサいので、かっこよくしたい。無限スクロールにチャレンジしてAみるか？
  - ユーザー名ではなくメールアドレスでログインするようにする

## 参考にした web サイトなど
 - Webブラウザでの３D表示　https://www.noboyu.com/how-to-embed-3d-models-website/
 - フィルターの掛け方　https://qiita.com/sr2460/items/ec864cb6457016ec8c14
 - SSL証明書入れるのに参考にしたサイト　https://qiita.com/shin4488/items/8738e13b92143c88aab6
 - SSL証明書入れるのに参考にしたサイトその２　https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04-ja
