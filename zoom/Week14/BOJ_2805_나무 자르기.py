def cut_trees(trees, target):
    max_height = 0
    
    # 가능한 모든 높이에 대해 반복 (0부터 가장 높은 나무까지)
    for h in range(max(trees) + 1):
        total_cut = 0
        
        # 각 나무에 대해 자른 길이 계산
        for tree in trees:
            if tree > h:
                total_cut += tree - h
        
        # 자른 총 길이가 목표 길이 이상인지 확인
        if total_cut >= target:
            max_height = h
        else:
            # 목표 길이에 도달하지 못하면 반복 중단
            break
    
    return max_height

# 입력 받기
N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 결과 계산 및 출력
result = cut_trees(trees, M)
print(result)

('---------------------------------------------------')

def cut_trees(trees, target):
    max_height = 0
    tree_count = len(trees)  # 나무의 개수 저장
    
    # 가장 높은 나무부터 시작해서 0까지 내려오며 확인
    for h in range(max(trees), -1, -1):
        total_cut = 0
        trees_cut = 0  # 잘린 나무의 개수를 세기 위한 변수
        
        # 각 나무에 대해 자른 길이 계산
        for i in range(tree_count):  # 인덱스를 사용하여 반복
            tree = trees[i]  # 현재 나무의 높이
            if tree > h:
                cut_length = tree - h  # 잘린 길이 계산
                total_cut += cut_length
                trees_cut += 1  # 잘린 나무 개수 증가
            
            # 이미 목표를 달성했다면 더 이상 계산할 필요 없음
            if total_cut >= target:
                break
        
        # # 자른 총 길이가 목표 길이 이상인지 확인
        # if total_cut >= target:
        #     max_height = h
        #     # 디버깅을 위한 출력
        #     print(f"높이 {h}m에서 {trees_cut}개의 나무를 잘라 {total_cut}m")
        #     break  # 최대 높이를 찾았으므로 종료
        # else:
        #     # 목표에 도달하지 못한 경우의 정보 출력
        #     print(f"높이 {h}m에서는 목표 {target}m에 도달하지 못함 (현재: {total_cut}m)")
    
    return max_height

# 입력 받기
N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 입력값 검증
if len(trees) != N:
    print("입력된 나무의 개수가 올바르지 않습니다.")
else:
    # 결과 계산 및 출력
    result = cut_trees(trees, M)
    print(f"절단기의 최대 높이: {result}m")

# 추가적인 정보 출력
print(f"총 나무의 수: {N}")
print(f"필요한 나무의 길이: {M}m")
print(f"가장 높은 나무의 높이: {max(trees)}m")
print(f"가장 낮은 나무의 높이: {min(trees)}m")