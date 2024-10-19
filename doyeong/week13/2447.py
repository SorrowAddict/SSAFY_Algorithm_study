# 2447. 별 찍기 - 10 (재귀)

N = int(input())

def draw_stars(num):
    # 재귀 함수의 제일 낮은 깊이의 기본값 설정
    if num == 1:
       return '*'

    # 재귀함수를 바로 호출하여 말단 깊이 (1일 때)까지 들어감
    stars = draw_stars(num//3)
    output = []

    # 말단 깊이 (1일 때)부터 정해진 규칙으로 output배열에 늘려가면서 저장한 값을 리턴
    # -> 리턴받은 함수값을 stars 변수에 담아서 for문으로 순회하면서 다시 패턴대로 3의 배수로 복제
    # --> 위 과정을 초기 num//3 까지 진행
    for star in stars:
        output.append(star*3)
    for star in stars:
        output.append(star+' '*(num//3)+star)
    for star in stars:
        output.append(star*3)

    return output

print('\n'.join(draw_stars(N)))