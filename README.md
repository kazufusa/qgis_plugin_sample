Created:  2014-05-11

1. QGIS 2.2 をインストール, port でpyqt4をインストール
2. プラグイン > プラグインの管理 ダイアログを開きplugin-builderを検索しインストール
3. plugin-builderを実行
4. 項目をampleで埋めて作成
5. qrcとuiをpyファイルにコンパイル
    - `ipyrcc4 -o resources.py resources.qrc`
    - `pyuic4 -o ui_sample.py ui_sample.ui`
6. ~/.qgis2/python/pluginsにディレクトリをコピー
7. プラグインマネージャでsampleを検索, チェックを入れる
8. pluginメニューから実行


<!-- vim:set ft=markdown: -->
