import socket

HOST, PORT = '', 9000

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port', PORT, '...')
while True:
    client_connection, client_address = listen_socket.accept()
    request = str(client_connection.recv(1024), 'utf-8')
    print(request)

    http_response = """\
HTTP/1.1 200 OK

<html>
<title>KHU GOODS</title>
<head><meta charset="utf-8"></head>

<body>
<h1><font size="7" color="skyblue">
<center>경희대 굿즈 구매</center>
</h1>
<hr style=" border: 1px solid skyblue">

<center><div style="border: 2px solid; width:600px; height:800px">
<form action="">
<font size="5" color="skyblue">
<p>1. 이름
<br><input type="text" name="name"></p>
<p>2. 학번
<br><input type="text" name="id"></p>
<p>3. 연락처
<br><input type="text" name="phone"></p>

<p>4. 구매할 상품
<br>
<label>
<input type="checkbox" name="number"> 인형 27,000원
</label>
<br>
<label>
<input type="checkbox" name="number"> 파우치 22,500원
</label>
<br>
<label>
<input type="checkbox" name="number"> 그립톡 6,000원
</label>
</p>

<p>5. 주소
<br><textarea cols="25" rows="2"></textarea></p>
<p>6. 문의사항은 010-0000-0000으로 연락주세요. </p>
<input type="button" value="구매하기" onclick="alert('다음 계좌로 입금하시면 주문이 완료됩니다. 우리은행 000-0000-000-000-00')">
</form>
</div></center>

</body>

</html>

"""
    client_connection.sendall(bytes(http_response, 'utf-8'))
    client_connection.close()