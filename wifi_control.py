def web_page():
    html = """<html><head><meta name="viewport"
content="width=device-width, initial-scale=1"></head>
<style>
.button {
  border: 3px black;
  color: 3px black;
  padding: 30px 32px;
  text-align: center;
  font-size: 16px;
  margin: 10px 80px;
  cursor: pointer;
}
.on {background-color: lime;} 
.off {background-color: red;} 
</style>
<body>
<a href =\"?led=on\"><button class="on"><b>on</b></button></a>&nbsp;
<a href =\"?led=off\"><button class="off"><b>off</b></button></a>
</body></html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')
    print('index found is ', led_on) 
    if led_on == 6:
        led.value(1)
    if led_off == 6:
        led.value(0)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()