# Write a Python program to demonstrate automatic and manual garbage collection using the gc module and analyze memory usage and performance.
import gc
import time
import tracemalloc
gc.enable()
tracemalloc.start()
class Test:
    def __init__(self):
        self.data = [0] * 1000
objects = []
for i in range(10000):
    objects.append(Test())
print("Objects created:", len(objects))
current, peak = tracemalloc.get_traced_memory()
print("Memory before deletion:", current)
del objects

start = time.time()
collected = gc.collect()
end = time.time()
current, peak = tracemalloc.get_traced_memory()
print("Garbage collected:", collected)
print("Memory after collection:", current)
print("Time taken:", end - start, "seconds")
tracemalloc.stop()
