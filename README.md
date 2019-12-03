# Pc-Remote-Controller-client

這是一個使用line-bot遠端控制電腦的code(client)



### **使用方法**

 1. 把他載下來
 2. 打開03.py
 3. 先確認import的套件你都有安裝
 4. 修改下方資料
```python
mailserver = imaplib.IMAP4_SSL('imap.gmail.com', 993)
# 非gmail者,993需要更改，自己google
username = '收信信箱'
password = '密碼'
```
 5. 執行它
```python
python 03.py
```
6.如果還沒架設line伺服端，右轉到這~~
https://github.com/luisbvcc1/pc-controller-server
