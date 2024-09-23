# ELYZA gRPC local Server Sample

## これは何？

CPU上でgRPC経由でELYZAを触るためのサンプルコードです。
なお、ELYZAのモデル本体はこのリポジトリには含まれていません。

## 使い方

### 必要なツール・モデルの準備

#### ELYZA

<https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF/tree/main>からGGUF形式のモデルをダウンロードし、src/guide配下に配置してください。

#### uv

`uv`はRust製のPythonのパッケージマネージャーです。
<https://docs.astral.sh/uv/getting-started/installation/#standalone-installer>からインストールしてください。

### 必要なパッケージのインストール

```shell
uv sync
```

### 実行

#### server側

```shell
uv run src/main.py
```

#### client側

```shell
uv run debug/debug_client.py
```
