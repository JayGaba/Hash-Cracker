from hashlib import md5, sha1, sha256
import sys, threading, queue
from time import time 

uncracked = True
correct_password = ''
threadsl = []

start_time = time()

def md5_crack():
    global uncracked, correct_password
    while uncracked and not q.empty():
        pwd = q.get()
        print(f"[+] Trying.. {pwd}")
        if md5(pwd.encode('utf-8')).hexdigest() == sample_hash:
            print(f"[+] Hashes matched for : {pwd}")
            uncracked = False
            correct_password = pwd
        q.task_done()
        
        
def sha1_crack():
    global uncracked, correct_password
    while uncracked and not q.empty():
        pwd = q.get()
        print(f"[+] Trying.. {pwd}")
        if sha1(pwd.encode('utf-8')).hexdigest() == sample_hash:
            print(f"[+] Hashes matched for : {pwd}")
            uncracked = False
            correct_password = pwd
        q.task_done()
        
        
def sha256_crack():
    global uncracked, correct_password
    while uncracked and not q.empty():
        pwd = q.get()
        print(f"[+] Trying.. {pwd}")
        if sha256(pwd.encode('utf-8')).hexdigest() == sample_hash:
            print(f"[+] Hashes matched for : {pwd}")
            uncracked = False
            correct_password = pwd
        q.task_done()
        
q = queue.Queue()     
   
sample_hash = sys.argv[1]        
hash_type = sys.argv[2]
threads = int(sys.argv[3])

func_type_map = {
    'md5': md5_crack,
    'sha1': sha1_crack,
    'sha256': sha256_crack
}

if hash_type not in func_type_map:
    print(f"Unsupported hash type: {hash_type}")
    sys.exit(1)

func_type = func_type_map[hash_type]

with open('passwordlist', 'r') as file:
    for password in file.read().splitlines():
        q.put(password)

for i in range(threads):
    t = threading.Thread(target=func_type, daemon=True)
    t.start()
    threadsl.append(t)
    
for t in threadsl:
    t.join()

if uncracked:
    print("[-] No matching password found.")
else:
    print(f"[+] Correct password: {correct_password}")


print(f"[+] Time taken : {time() - start_time:.2f}")