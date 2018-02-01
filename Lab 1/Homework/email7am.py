from gmail import GMail, Message
from datetime import datetime
from threading import Timer


x=datetime.today()
y=x.replace(day=x.day+7, hour=7, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

gmail = GMail('dgtran1995@gmail.com', 'Gagaga1995')
msg = Message('Xin nghi om', to="dennis_1328@yahoo.com.vn", text="Thich thi nghi thoi")

gmail.send(msg)
