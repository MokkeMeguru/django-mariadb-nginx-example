# Django REST Framework Tutorials 2
# Requirement
- Python > 3.6
- Mac or Linux (recommend)

# 開発環境に復帰する
MacやLinuxをシャットダウンしたり、ターミナルなどを閉じてしまっている人のために開発環境の復帰方法について書いておきます。

```shell
cd <project-name>
source venv/bin/activate
python manage.py runserver
```

これで `localhost:8000/swagger`へアクセスすればおなじみの Swagger の画面を見ることができます。

# Ping Pong API を実装する。
クライアントから "ping" と問い合わせがあったら、何も考えずに "pong" と返すだけの簡単そうなAPIを作ります。

まず断っておきますが、恐らくこのAPIはDjango中では *屈指の難易度* になります。正気を保って頑張ってください。
## app を作る
かなりリソースを無駄遣いしてしまう工程ですが、[公式のチュートリアル](https://www.django-rest-framework.org/tutorial/quickstart/) に従いましょう。まずは ping_pong という app を作ります。

雑に言ってしまえばネームスペースみたいな感じです。この中 *だけ* で ping_pong のAPIを作ろう、というわけです。

```shell
django-admin startapp ping_pong
```

ディレクトリ構成は以下のようになります。

```
. example_django_rest_api
├── db.sqlite3
├── example_django_rest_api
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── ping_pong
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── requirement.txt

```

## model を作る
`ping_pong/models.py` を見てください。

```python
from django.db import models
```

と書いてありますね。

以上です。たかだか ping-pong ごときにこんなものいらないんですよ。

## serializer を作る
serializer は 例えば Python の辞書オブジェクトや配列とJSONやXMLとの変換をスムーズに行うために必要になってしまっている必須機能です。次回で model と serializer 両方を「はじめまして」だと説明する量が多くなるのでここで紹介します。

`ping_pong/serializer.py` を作って下さい。(Django はこちらを用意してくれません)


```python
from rest_framework import serializers


class PingPongSerializer(serializers.Serializer):
    ping = serializers.CharField(allow_blank=True,
                                 default="ping",
                                 max_length=20,
                                 help_text="please input 'ping'")

# example_ping = PingPongSerializer({"ping": "hoge"})
# => {'ping' : 'hoge'}
# example_ping = PingPongSerializer({})
# print(example_ping.data)
# => {'ping' : 'hoge'}
```

一行目で提供されている serializer をインポートしています。これを基準にしてクラスを作るわけですね。

class PingPongSerializer は serializers.Serializer を継承しており、そこにある変数は ping という serializers.CharField 型のインスタンスです。

CharField 型のインスタンスとは、つまりは短めのテキストの入力を期待しています。これに対して、長めのテキストについては TextField 型のインスタンスが適当とされています。一覧は Tipsの [Serializers 一覧](#serializers-一覧)

初期化引数にいろいろ書いてありますが、これの説明は省略します。なぜならばこの部分の詳しい話はセキュリティなどで割と重要になる部分なので、できる人にお願いしたほうが良いからです。

適当な実行環境で上のコードを読み込んで下のコメント部分を実行することで、このSerializerが何をするのかがわかると思います。入力に 'ping' キーがあればその値を、そうでなければ "ping" が含まれていますね。

## view を作る
`ping_pong/view.py` を編集します。

```
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from ping_pong.serializers import PingPongSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class PingPongView(APIView):
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('ping',
                          openapi.IN_QUERY,
                          description="please input ping",
                          type=openapi.TYPE_STRING)
    ])
    def get(self, request, format=None):
        serializer = PingPongSerializer(data=request.GET)
        if serializer.is_valid():
            if serializer.data['ping'] == 'ping':
                return Response({'result': 'pong'})
            else:
                return Response({'result': "What's in your head?"})
        else:
            return Response({'error': serializer.errors})
```

PingPongView という APIView (rest_framework の API ように設計された基礎の View)を継承したクラスに get method を追加しています。

@swagger なんとかはSwaggerでうまいことパラメータを表示するためのデコレータ（修飾）です。これがないとSwaggerからAPIをテストすることができません。

処理の流れとしては次のようになります。
 - get の引数である request に対して値が降ってくる
 - serializer を通して型にはめる（もしここで条件（例えば10文字以上の ping がやってきた）に違反したら...?）
 - serializer の型に突っ込んだデータから必要なデータを持ってくる
 - 持ってきたデータが期待するデータであるかどうかを条件判定して Response を返す。
 
## router を作る
Django特有の *知らない間にたくさんのAPIを生やしてくれる機能* は今回は遠慮させていただいて、シンプルなルーティングをしたいと思います。

```python
# ...
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# add below lines
from rest_framework import routers
from ping_pong import views
from django.conf.urls import include

# schema_view = get_schema_view(
# ...
# ...

# ...
urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # add a below element
    url(r'ping', views.PingPongView.as_view(), name='ping'),
]
```
## Swagger に繋げる
`http://localhost:8000/swagger` へアクセスしたら、あとはお楽しみください。

なお最終的なフォルダ構成は次のようになっています。
```python
.
├── db.sqlite3
├── example_django_rest_api
│   ├── __init__.py
│   ├── __pycache__
│   │   └── ...
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── ping_pong
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── __pycache__
│   │   └── ...
│   ├── routers.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
└── requirement.txt
```
# Tips
## Django が得意なこと
Django の設計思想は MTV (Model-Template-View) というものです。
- Modelはデータベースとの連携を取る部分
- Template はHTMLのようないわゆる表側の部分
- View は Model <-> Template をつなぐ部分です。

特にViewは MVC (Model-View-Controller) とは考え方が異なるため注意が必要です。
MTVにおける View は Model のデータ（DBのテーブルを想像してもらったほうがDjango的かもしれません）へ関数を適用して、Templateの必要な部分へつなげるパイプとなる部分となります。

つまり逆に言うと、この形に沿わないようなクライアントサイドのない RESTful API や ping-pong などの *簡単な* API を扱う際には、比較的に難易度が上がってしまう可能性があります。

何が言いたいかって言うと、*フレームワーク選定は人気や流行りで選ぶな*

## Serializers 一覧

django 2.2.4 における serializer field mapping の一覧(rest_framework/serializers.py line.854)

```python
serializer_field_mapping = {
        models.AutoField: IntegerField,
        models.BigIntegerField: IntegerField,
        models.BooleanField: BooleanField,
        models.CharField: CharField,
        models.CommaSeparatedIntegerField: CharField,
        models.DateField: DateField,
        models.DateTimeField: DateTimeField,
        models.DecimalField: DecimalField,
        models.EmailField: EmailField,
        models.Field: ModelField,
        models.FileField: FileField,
        models.FloatField: FloatField,
        models.ImageField: ImageField,
        models.IntegerField: IntegerField,
        models.NullBooleanField: NullBooleanField,
        models.PositiveIntegerField: IntegerField,
        models.PositiveSmallIntegerField: IntegerField,
        models.SlugField: SlugField,
        models.SmallIntegerField: IntegerField,
        models.TextField: CharField,
        models.TimeField: TimeField,
        models.URLField: URLField,
        models.GenericIPAddressField: IPAddressField,
        models.FilePathField: FilePathField,
    }
```
