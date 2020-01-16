n, m = [int(i) for i in input().split()]
kub_alice_set = set()
kub_bob_set = set()

for i in range(n):
    num_alice_cub = int(input())
    kub_alice_set.add(num_alice_cub) 

for j in range(m):
    num_bob_cub = int(input())
    kub_bob_set.add(num_bob_cub)

print(len(kub_alice_set & kub_bob_set))

for elem in sorted(kub_alice_set & kub_bob_set):
    print(elem)
print(len(kub_alice_set - kub_bob_set))    

for elem in sorted(kub_alice_set - kub_bob_set):
    print(elem)
print(len(kub_bob_set - kub_alice_set))     

for elem in sorted(kub_bob_set - kub_alice_set):
    print(elem)
	

