import time
import multiprocessing
import threading
import concurrent.futures



def do_something(seconds):
    print(f"Sleeping for {seconds} ,second....")
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"

#
# with concurrent.futures.ProcessPoolExecutor as executor:
#     secs=[5,4,3,2,1]
#     results=executor.map(do_something,secs)
#
#     for r in results:
#         print(r)


# with concurrent.futures.ProcessPoolExecutor as executor:
#     secs=[5,4,3,2,1]
#     results=[executor.submit(do_something,s) for s in secs]
#
#     for r in concurrent.futures.as_completed(results):
#         print(r.result())


# with concurrent.futures.ProcessPoolExecutor as executor:
#     f1=executor.submit(do_something,1)
#     print(f1.result())
#

# processes=[]
# for _ in range(10):
#     p=multiprocessing.Process(target=do_something,args=[1.5])
#     p.start()
#     processes.append(p)
#
# for p in processes:
#     p.join()

def demorun():
    start = time.perf_counter()

    # p1=multiprocessing.Process(target=do_something,args=[1])
    # p2=multiprocessing.Process(target=do_something,args=[1])
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()
    #
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs=[5,4,3,2,1]
        results=executor.map(do_something,secs)

        for r in results:
            print(r)

    stop=time.perf_counter()

    print(f"Finished in {round(stop-start,2)} seconds")

#
if __name__ == '__main__':
    demorun()