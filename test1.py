from time import sleep
from tqdm import tqdm
for i in tqdm(range(1,500)):
    sleep(0.01)
pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    pbar.set_description("Processing %s" % char)