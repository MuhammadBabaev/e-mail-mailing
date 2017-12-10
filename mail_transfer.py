import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('exmorefferal@gmail.com','exmo1234')


msg = """From: From Exmo <from@fromdomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Exmo 

<tbody style="width: 100%">
    <div style="width: 100%; border-radius: 3px 0 0 3px">
        <h1 style="font-size: 40px">Международная биржа криптовалют</h1>
        <img style="width: 65%; padding: 10px 17% 10px 17%" src='https://pbs.twimg.com/media/DIopae8XYAABb1y.jpg:large'>
        <p>Уже более 700k человек выбрали нас</p>



        <h1 style="text-align: center">Создайте бесплатную учетную запись<br>
				чтобы начать торговать криптовалютами</h1>

        <div align="center">
            <a href="https://exmo.me/?ref=591478"><button align="center" style="width: 250px; height: 55px; background: #347FFB; color: #fff; font-size: 19px; border: none; border-radius: 3px; cursor: pointer;">Создать учетную запись</button></a>
        </div>
    </div>
    
</tbody>
"""

smtpObj.sendmail("exmorefferal@gmail.com","exmorefferal@gmail.com",msg.encode('utf-8'))

smtpObj.quit()



