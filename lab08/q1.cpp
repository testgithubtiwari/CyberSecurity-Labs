#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int privateKeyGen(int p, int q, int publicKey) {
    int phi = (p - 1) * (q - 1);
    int privateKey = -1;
    for (int i = 2; i < phi; i++) {
        if (gcd(i, phi) == 1 && (publicKey * i) % phi == 1) {
            privateKey = i;
            break;
        }
    }
    return privateKey;
}


int signTheMessage(int publicKey,int message,int p,int q){
    int n=p*q;
    int encryptedmessage;
    // do encryption using publick key in rsa
    int var;
    var=pow(message,publicKey);
    encryptedmessage=var%n;
    return encryptedmessage;
}


int decryptMessage(int privateKey,int encryptedmessage,int p,int q){
    int n=p*q;
    int decryptMessage;
    int var;
    var=pow(encryptedmessage,privateKey);
    decryptMessage=var%n;
    return decryptMessage;
}

int main() {
    cout << "Please enter two prime numbers: ";
    int p, q;
    cin >> p >> q;
    if (!isPrime(p) || !isPrime(q)) {
        cout << "Both numbers should be prime." << endl;
        return 1;
    }
    cout << "Enter the public key: ";
    int publicKey;
    cin >> publicKey;
    int privateKey = privateKeyGen(p, q, publicKey);
    if (privateKey == -1) {
        cout << "Private key cannot be generated with the given public key." << endl;
    } else {
        cout << "Private key: " << privateKey << endl;
    }
    cout<<"Enter the message you want to encrypt: ";
    int message;cin>>message;
    int signmessage=signTheMessage(publicKey,message,p,q);
    cout<<"The encrypted message is: ";
    cout<<signmessage<<endl;
    int decryptmessage=decryptMessage(privateKey,signmessage,p,q);
    if(decryptmessage==message){
        cout<<"verified done"<<endl;
    }else{
        cout<<"not verified"<<endl;
    }
    return 0;
}
