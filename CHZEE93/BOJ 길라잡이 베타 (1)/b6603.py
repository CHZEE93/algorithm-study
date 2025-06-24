#백준 6603번(로또)

from itertools import combinations

while True:
    nums = list(map(int, input().split()))

    if len(nums) == 1 and nums[0] == 0:
        break
    else:
        length = nums[0]
        aList = nums[1:length+1]

        # 6개 조합을 만들고 출력
        for comb in combinations(aList, 6):
            print(' '.join(map(str, comb)))
    
    print()  # 각 테스트 케이스 사이에 빈 줄
