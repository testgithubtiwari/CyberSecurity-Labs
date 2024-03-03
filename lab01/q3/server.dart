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
      
      // Simulate abnormal behavior: Send a large amount of data to the client
      for (int i = 0; i < 1000; i++) {
        clientSocket.write('Abnormal data $i\n');
      }
      
      // Close the connection after sending abnormal data
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
