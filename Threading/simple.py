import time
import threading
import concurrent.futures

start=time.perf_counter()

def do_something(seconds):
    print(f"Sleeping for {seconds} second....")
    #print(f"Sleeping for 1 second....")
    time.sleep(seconds)
    #print(f"Done Sleeping... for {seconds} second")
    return(f"Done Sleeping....for {seconds} second")


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[5,4,3,2,1]
    results=executor.map(do_something,secs)

for r in results:
    print(r)

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs=[9,5,4,3,2,1]
#     results=[executor.submit(do_something,s) for s in secs]
#
# for f in concurrent.futures.as_completed(results):
#     print(f.result())
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something, 1)
#     print(f1.result())
#
# threads=[]
# for _ in range(10):
#     t=threading.Thread(target=do_something,args=[1.5])
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()


# t1=threading.Thread(target=do_something)
# t2=threading.Thread(target=do_something)
# t1.start()
# t2.start()
# #
# t1.join()
# t2.join()
# do_something()
# do_something()

stop=time.perf_counter()

print(f"Finished in {round(stop-start,2)} seoconds")