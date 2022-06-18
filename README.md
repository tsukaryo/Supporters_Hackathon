### SupportersHackathon

##  取り組むテーマ：AI、機械学習、データ分析

# 題名：就活でのES作成支援アプリ
## 課題：研究と就活の両立が難しい修士学生にとってエントリーシートを書く手間が煩わしい
### 解決方法：あらかじめ入力しておいたES解答の文章を必要な文字数に合わせて要約してくれるアプリケーションを開発
### 提供できる価値：ただの要約機能ではなく、ESに使用した文章ごと保存しておくことができるため、振り返りが可能（仮）

<br>

### ペルソナ
#### ・筑波大学院 修士1年 数値計算系研究室所属
#### ・機械学習エンジニア志望

<br>

#### 初めてクローンする時(作業するディレクトリ配下で)
```python:docker.py
git clone https://github.com/tsukaryo/Supporters_Hackathon.git
cd Supporters_Hackathon
docker-compose build
docker-compose run web python3 manage.py migrate auth
docker-compose run web python3 manage.py migrate
```
dockerコンテナ起動
```python:docker.py
docker-compose up
```

ローカルで確認(URL)
```python:docker.py
http://localhost:8000/
```

#### 2回目以降
dockerコンテナ起動
```python:docker.py
docker-compose start
```
