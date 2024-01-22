import 'dart:io';

void startServer() async {
  ServerSocket? serverSocket;
  String host = '127.0.0.1';
  int port = 12346;

  try {
    serverSocket = await ServerSocket.bind(host, port);
    print('Server listening on $host:$port');
    await for (Socket clientSocket in serverSocket) {
      print(
          'Connection from ${clientSocket.remoteAddress}:${clientSocket.remotePort}');
      clientSocket.close();
    }
  } catch (e) {
    print('Error: $e');
  } finally {
    serverSocket?.close();
  }
}

void main() {
  startServer();
}
