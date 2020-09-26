from collections import deque

price_per_bullet = int(input())
magazine_size = int(input())
bullets = input().split()
bullet_count = len(bullets)
locks = deque(input().split())
reward = int(input())

shots = 0

#main loop
while True:      

    if shots == magazine_size and len(bullets) > 0:
        shots = 0
        print("Reloading!")   
        #continue

    if len(locks) == 0:
        print(f"{len(bullets)} bullets left. Earned ${reward - ((bullet_count - len(bullets)) * price_per_bullet)}")
        break

    if len(bullets) == 0:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
    
    current_lock = int(locks[0])
    current_bullet = int(bullets[-1])

    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
        bullets.pop()

    else:
        print("Ping!")
        bullets.pop()

    shots += 1