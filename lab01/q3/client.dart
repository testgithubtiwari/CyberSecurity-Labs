import 'dart:io';

void startClient() async {
  Socket clientSocket = await Socket.connect('127.0.0.1', 12346);
  print('Connected to 127.0.0.1:12346');

  stdout.write('Enter the message from client to server: ');
  String clientMessage = stdin.readLineSync()!;

  clientSocket.write(clientMessage);

  clientSocket.listen(
    (List<int> event) {
      String responseMessage = String.fromCharCodes(event);
      print('Server response: $responseMessage');
    },
    onDone: () {
      print('Connection closed');
      clientSocket.destroy();
    },
    onError: (error) {
      print('Error: $error');
      clientSocket.destroy();
    },
  );
}

void main() {
  startClient();
}
