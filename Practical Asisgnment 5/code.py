
# Online Python - IDE, Editor, Compiler, Interpreter
import random

p = 308517851123965903797430863907
g = random.randint(1, p)

def calculate_power_modulo(num, power, mod):
    if power == 0:
        return 1;
    res = calculate_power_modulo(num, power // 2, mod)
    res *= res
    res %= mod
    if power % 2:
        res *= num
        res %= mod
    return res
    
class Person:
    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key
        print("generated private_key = ", self.private_key)
        print("generated public_key = ", self.public_key)
    
    def get_public_key(self):
        return self.public_key
        
    def send_message(self, message, recepient):
        recepient_public_key = recepient.get_public_key()
        key = calculate_power_modulo(recepient_public_key, self.private_key, p)
        encrypted_message = message * key
        return encrypted_message
        
    def receive_message(self, encrypted_message, sender):
        encrypted_message %= p
        sender_public_key = sender.get_public_key()
        temp = calculate_power_modulo(sender_public_key, self.private_key, p)
        temp = calculate_power_modulo(temp, p - 2, p)
        temp = temp * (encrypted_message % p)
        message = temp % p
        return message
        

person1_private_key = random.randint(1, p - 2)
person1_public_key = calculate_power_modulo(g, person1_private_key, p)

person2_private_key = random.randint(1, p - 2) 
person2_public_key = calculate_power_modulo(g, person2_private_key, p)

print("creating credentials for person1")
person1 = Person(person1_private_key, person1_public_key)

print("creating credentials for person2")
person2 = Person(person2_private_key, person2_public_key)

random_message = random.randint(1, p)
print("random message = ", random_message)

print("sending random_message from person1 to person2...")
encrypted_message = person1.send_message(random_message, person2)
print("encrypted message: ", encrypted_message)

print("decrypting message received from person1 to person2...")
decrypted_message = person2.receive_message(encrypted_message, person1)
print("decrypted_message: ", decrypted_message)

if(decrypted_message == random_message):
    print("decrypted_message and message sent matched!")




