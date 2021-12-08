from time import sleep
import random
from tqdm import tqdm
from multiprocessing import Pool, freeze_support, RLock
from multiprocessing import current_process


def progresser(n):
    text = f'#{n}'
    sampling_counts = 10
    current = current_process()
    pos = current._identity[0]-1

    with tqdm(total=sampling_counts, desc=text, position=pos) as pbar:
        for i in range(sampling_counts):
            sleep(random.uniform(0, 1))
            pbar.update(1)

if __name__ == '__main__':
    freeze_support()
    L = list(range(30)) # works until 23, breaks starting at 24
    # p = Pool(processes=None,
    #         initargs=(RLock(),), initializer=tqdm.set_lock
    #         )
    with Pool(initializer=tqdm.set_lock, initargs=(tqdm.get_lock(),)) as p: 
        p.map(progresser, L)
        print('\n' * (len(L) + 1))