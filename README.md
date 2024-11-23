## 環境作成手順
### Macの場合
```
git clone https://github.com/takasan1234/vote_app.git
cd vote_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```


### Windowsの場合
```
git clone https://github.com/takasan1234/vote_app.git
cd vote_app
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
```
## 動作例

https://github.com/user-attachments/assets/f4b2505e-aeb0-48ab-816b-7462ed2eba14

