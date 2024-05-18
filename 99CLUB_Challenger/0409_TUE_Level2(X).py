# 호텔 대실 
# https://school.programmers.co.kr/learn/courses/30/lessons/155651
# 입실, 퇴실 시간 비교를 통해 최소의 방을 통한 고객 입실 

def time_to_min(str1) : # str형으로 주어지는 시간에 대해 min 으로 바꿔 비교 
    return int(str1[:2]) * 60 + int(str1[3:])

def solution(book_time):
    rooms = [] # 방에 대한 확인 
    
    book_time_sort = sorted([time_to_min(a), time_to_min(b)+10] for a, b in book_time) # 입실시간 최소 => 퇴실 시간 + 10 최소로 비교, sorting 
    
    for book in book_time_sort : 
        if not rooms : # 방에 아무도 없을 때는 방에 그냥 입실, 이후 반복문 진행 
            rooms.append(book)
            continue
        
        for idx, room in enumerate(rooms) : # 방에 누군가 있을 때 
            if room[1] <= book[0] : # 퇴실시간이 들어오고자 하는 고객의 입실 시간보다 빠를 때
                rooms[idx] = book # 방 교체 
                break
                
        else : 
            rooms.append(book) # 들어갈 방이 없을 때 방 추가 
    
    return len(rooms)