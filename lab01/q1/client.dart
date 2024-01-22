import 'dart:io';

void startClient() async {
  Socket? socket;
  String host = '127.0.0.1';
  int port = 12346;

  try {
    socket = await Socket.connect(host, port);
    print('Connected to $host:$port');
  } catch (e) {
    print('Error: $e');
  } finally {
    socket?.close();
  }
}

void main() {
  startClient();
}
