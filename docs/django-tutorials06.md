# Django REST Framework Tutorials 5
# Requirement
- Python > 3.6
- Mac or Linux (recommend)
- SQLite3

# ログイン処理周りの実装を行う
ログインを実装する簡単な方法は、そのためのライブラリを利用することです。下手に自分で実装しようとするとフレームワークを勉強しないといけないので、納期が短い場合なんかはこういう雑な方法で解決しないといけません。

```shell
pip install django-rest-auth
```

```python:settings.py
# ...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'livesync',
    'rest_framework',
    'drf_yasg',
    'draft_todo.apps.DraftTodoConfig',
    'rest_framework.authtoken'
]

#...
```

```python:urls.py
# ...
import rest_auth


# ...

urlpatterns = [
    # ...
    path('rest-auth', include('rest_auth.urls'))
]
```

```shell
python manage.py migrate
python manage.py runserver
```

# Swagger で確認してみる
作ってあるユーザでログインしてみましょう。

![](./img/django-rest-login-input.png)
![](./img/django-rest-auth-login.png)

ユーザの情報を参照しましょう。

![](./img/django-rest-login-input.png)

タスクを追加してみましょう。

![](./img/drf-input-auth-task-input.png)

ちなみにページをリロードすると、ログイン情報が更新されます。

![](./img/django-rest-authlogin.png)

# admin で確認してみる

admin から Tokens を確認してみましょう。

![](./img/django-admin-tokens.png)

タスクが追加されているのかを確認してみましょう。

![](./img/django-admin-tasks.png)

# Next Step？
とりあえずこれだけ動けば後は気持ちで解決できると思います。
なにか問題があればレポジトリの issue を立てて下さい。

# Tips
## 認証周りってどんな種類があるの？あとどれがおすすめ？
Django Rest Framework では [この一覧](https://www.django-rest-framework.org/api-guide/authentication/#basicauthentication) にある認証方法や、[django-rest-auth](https://django-rest-auth.readthedocs.io/en/latest/index.html) にあるような Social Authentication (Twitter 認証とか) があります。

個人的には Session Authentication が何も考えずに手に馴染んでいるので好きなんですが、クソジャイル開発とかしているとチームの火種となるので、Basic認証が楽なんじゃないっすかね。ただし当然のことながらHTTPS化が推奨なので、その点だけ気をつける必要がありそうですね。

(というか認証周り自体チーム開発の火種なのでは…?)

# backlog

この状態のデータは、このレポジトリの release v0.1.5 にあります。
