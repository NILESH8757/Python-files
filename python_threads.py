import threading

cnt=0

def bang():
    global cnt
    print("Your are being watched!")
    if cnt < 5:
        cnt+=1
        threading.Timer(5.0, bang).start()
    else:
        print("Be careful!")
    
    
def main():
    bang()
    return 0

if __name__ == '__main__':
	main()
