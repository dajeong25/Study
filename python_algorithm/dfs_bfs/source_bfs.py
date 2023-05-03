# 출처 [저서] : 이것이 취업을 위한 코딩테스트다 with 파이썬

# 개수 = N개, 시간복잡도 = O(N) : 일반적인 경우 dfs보다 수행시간이 짧음

#BFS 예제
## >> 시작 노드와 연결된 노드를 모두 탐색 후 점차 깊게 탐색

from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True #현재 노드 방문처리
    
    #큐가 빌 때까지 반복
    while queue:
        v = queue.popleft() #큐에서 하나를 뽑아 출력
        print(v, end=' ')
        
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [[]
         , [2,3,8] #1번노드에 연결된 노드들
         , [1,7]   #2번노드에 연결된 노드들
         , [1,4,7] #3번노드
         , [3,5]   #4번노드
         , [3,4]   #5번노드
         , [7]     #6번노드
         , [2,6,8] #7번노드
         , [1,7]]  #8번노드

#각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] *9

bfs(graph, 1, visited) #출력: 1 2 3 8 7 4 6 5  
