import cProfile
import pstats
import io

def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

def fast_function():
    return sum(range(1000000))

def main():
    slow_function()
    fast_function()

if __name__ == "__main__":
    # Create a profile object
    pr = cProfile.Profile()
    pr.enable()  # Start profiling

    main()

    pr.disable()  # Stop profiling

    # Create a stream to hold the profiling results
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.TIME)
    ps.print_stats()

    # Print profiling results
    print(s.getvalue())
import timeit

def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

def fast_function():
    return sum(range(1000000))

# Measure execution time of slow_function
slow_time = timeit.timeit('slow_function()', globals=globals(), number=1)
print(f"slow_function() took {slow_time:.6f} seconds")

# Measure execution time of fast_function
fast_time = timeit.timeit('fast_function()', globals=globals(), number=1)
print(f"fast_function() took {fast_time:.6f} seconds")

from memory_profiler import profile

@profile
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

@profile
def fast_function():
    return sum(range(1000000))

def main():
    slow_function()
    fast_function()

if __name__ == "__main__":
    main()
