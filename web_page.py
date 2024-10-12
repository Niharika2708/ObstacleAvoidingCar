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
<a href =\"?car=on\"><button class="on"><b>on</b></button></a>&nbsp;
<a href =\"?car=off\"><button class="off"><b>off</b></button></a>
</body></html>"""
    return html