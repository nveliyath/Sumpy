from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
name = MPI.Get_processor_name()

N = 1000000
arr = []
brr = [size]
total = 0
roll = 0
master = 0
status = MPI.Status()

if (rank == master):
    for j in range(0, N):
        arr.append(random.randint(1, 10))

#arr = comm.bcast(arr, N, MPI.DOUBLE, master, comm)
arr = comm.bcast(arr, master)

self = (float(rank))/(float(size))
selfie = (float(rank) + 1)/(float(size))
self = self * N
selfie = selfie * N
self2 = int(self)
selfie2 = int(selfie)

selfTotal = 0
for i in range(self2, selfie2):
    selfTotal = selfTotal + arr[i]
print("\n")
print("Processor " + str(rank) + "'s sum is " + str(selfTotal))

if (rank != master):
    comm.send(selfTotal, dest=master)
else:
    total = selfTotal
    for i in range(1, size):
        selfTotal = comm.recv(selfTotal, MPI.ANY_SOURCE)
        total = total + selfTotal
if (rank == master):
    print("Final Sum is :" + str(total))
