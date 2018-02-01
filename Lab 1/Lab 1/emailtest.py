from gmail import GMail, Message

html_template = '''
<p><span style="color: #ff0000;"><strong>Xin nghi om</strong></span></p>
<p>Hom nay luc em thuc day thay dau oc quay cuong, biet la minh da bi trung <strong>{{sickness}}</strong>. Nay long the bat an, em xin phep duoc nghi hoc 1 buoi.&nbsp;</p>
<p><strong>Tao dua day, thich thi nghi thoi</strong>&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /></p>
'''

sickness_list = ['Kiet li', 'Tao bon', "Tieu chay", "Dich ta"]
sickness = choice(sickness_list)

html_content = html_template.replace("{{sickness}}", sickness)

gmail = GMail('dgtran1995@gmail.com', 'Gagaga1995')
msg = Message('Xin nghi om', to="dennis_1328@yahoo.com.vn", html=html_content)

gmail.send(msg)
