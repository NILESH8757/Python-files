import threading

cnt=0

def warning():
    global cnt
    print("Your are being watched!")
    if cnt < 5:
        cnt+=1
        threading.Timer(5.0, warning).start()
    else:
        print("Be careful!")
    
    
def main():
    warning()
    return 0

if __name__ == '__main__':
	main()
