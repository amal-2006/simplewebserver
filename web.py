from http.server import HTTPServer, BaseHTTPRequestHandler
content="""
<html>
	<head>
		<title>Software Companies</title>
	</head>
	<body bgcolor="lavender">
	<table border="9" cellspacing="10" cellpadding="10" height="150" width="300" align="center">
	<caption> <h3>Top Five Revenue Generating Sotware Companies </h3></caption>
		<tr>
			<th>Company</th>
			<th>Sales(USD)</th>
			<th>Nationality</th>
		</tr>
		<tr>
			<th>Microsoft</th>
			<th>57.9</th>
			<th>USA</th>
		</tr>
		<tr>
			<th>Oracle</th>
			<th>21.0</th>
			<th>USA</th>
		</tr>
		<tr>
			<th>SAP</th>
			<th>16.1</th>
			<th>Germany</th>
		</tr>
		<tr>
			<th>Computer Associates</th>
			<th>4.2</th>
			<th>USA</th>
		</tr>
		<tr>
			<th>Electronic Arts</th>
			<th>3.2</th>
			<th>USA</th>
		</tr>
	</table>
	</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address=('',8000)
httpd=HTTPServer(server_address,myhandler)
print("My Webserver is running...")
httpd.serve_forever()