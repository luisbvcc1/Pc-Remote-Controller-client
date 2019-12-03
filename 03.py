import imaplib
from time import sleep
import os

while True:
    try:
        # 登入和取得
        mailserver = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        username = '收信信箱'
        password = '密碼'
        mailserver.login(username, password)
        status, count = mailserver.select('Inbox')
        status, data = mailserver.fetch(count[0], '(UID BODY[TEXT])')

        content = (str((data[0][1]).strip()).split("'"))[1]

        # 判斷
        sep_content = content.split('`')
        try:
            if sep_content[0] == 'cmd':
                command = str(sep_content[1])
                # 刪除郵件
                mailserver.store(count[0], '+FLAGS', r'(\Deleted)')
                mailserver.expunge()
                # 登出
                mailserver.close()
                mailserver.logout()
                # 執行指令
                os.system(command)
                print('執行完成')
                sleep(10)
            else:
                sleep(10)
        except:
            sleep(10)
    except:
        sleep(10)