import sys

sys.stdin = open("input/10_1989_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    str = input()
    palin = str[::-1]
    #print(palin)
    if str == palin:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')
    # ///////////////////////////////////////////////////////////////////////////////////
