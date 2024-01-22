import 'dart:io';

Future<Socket> connectToServer(String host, int port,
    {bool useSSL = false}) async {
  Socket clientSocket = await Socket.connect(host, port);

  if (useSSL) {
    SecurityContext context = SecurityContext.defaultContext;
    clientSocket = await SecureSocket.connect(host, port, context: context);
  }

  return clientSocket;
}

void sendRequest(Socket clientSocket, String request) {
  clientSocket.write(request);
}

void receiveResponse(Socket clientSocket, String serverHost) {
  print('Connection established to ${serverHost}');
  // clientSocket.listen(
  //   (List<int> data) {
  //     print(
  //       'Connection established to ${clientSocket.remoteAddress.host}:${clientSocket.remotePort}',
  //     );
  //     // String response = String.fromCharCodes(data);
  //     // print(response);
  //   },
  //   onDone: () {
  //     // Close the connection after receiving the response
  //     clientSocket.close();
  //   },
  //   onError: (error) {
  //     print('Error: $error');
  //   },
  // );
}

void closeConnection(Socket clientSocket) {
  // Close the connection
  clientSocket.close();
}

void main() async {
  String serverHost = "rt-portfolio.vercel.app";
  int serverPort = 443; // HTTPS default port
  String httpRequest =
      "GET / HTTP/1.1\r\nHost: rt-portfolio.vercel.app\r\n\r\n";
  Socket clientSocket =
      await connectToServer(serverHost, serverPort, useSSL: true);
  sendRequest(clientSocket, httpRequest);
  receiveResponse(clientSocket, serverHost);
}
