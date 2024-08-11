# 리뷰

- 처음에 my_count() 함수를 작성할 때 COUNTS 배열의 크기를 max(lst)+1 로 해주어서 배열의 최댓값이 4보다 작을 경우 IndexError: list index out of range 가 떠서 17점을 받았다.
    - 아니 이제보니 my_max 함수라 적어놓고 변수 이름이랑 함수식은 min() 함수를 적어버렸네..? ㅋㅎㅎ ;;;
- 카운팅 배열을 사용할 때 주의점을 깨우칠 수 있었다

```python
def my_max(lst):
    my_min_v = lst[0]
    for x in lst:
        if my_min_v < x:
            my_min_v = x
    return my_min_v

def my_count(lst):
    COUNTS = [0] * (my_max(lst) + 1)
    for x in lst:
        COUNTS[x] += 1
    return COUNTS
```

<br>

# 참고자료

- 