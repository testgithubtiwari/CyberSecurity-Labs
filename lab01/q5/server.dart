import 'dart:io';
import 'dart:convert';

void startServer() async {
  ServerSocket serverSocket = await ServerSocket.bind('127.0.0.1', 12346);
  print('Server listening on 127.0.0.1:12346');

  await for (Socket clientSocket in serverSocket) {
    print(
        'Connection from ${clientSocket.remoteAddress}:${clientSocket.remotePort}');
    List<int> data = await clientSocket.first;
    String clientMessage = utf8.decode(data);
    String messageUppercase = reverseString(clientMessage);
    clientSocket.write(messageUppercase);

    clientSocket.close();
    serverSocket.close();
  }
}

String reverseString(String clientMessage) {
  List<String> characters = clientMessage.split('');
  List<String> reversedCharacters = characters.reversed.toList();
  return reversedCharacters.join('');
}

void main() {
  startServer();
}
