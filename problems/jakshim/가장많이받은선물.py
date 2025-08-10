def solution(friends, gifts):
    friends_dict = {name: { x: 0 for x in friends} for name in friends}
    
    for gift in gifts:
        send_member, receive_member = gift.split()
        friends_dict[send_member][send_member] += 1
        friends_dict[send_member][receive_member] += 1
        friends_dict[receive_member][receive_member] -= 1
        friends_dict[receive_member][send_member] -= 1

    friends_answer = {name: 0 for name in friends}
    for name in friends:
        index = friends_dict[name][name]
        for friend, num in friends_dict[name].items():
            if friend == name:
                continue
            if num == 0:
                if friends_dict[friend][friend] < index:
                    friends_answer[name] += 1
            if num > 0:
                friends_answer[name] += 1

    return max(friends_answer.values())

if __name__ == '__main__':
    print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
    print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
    print(solution(["a", "b", "c"],["a b", "b a", "c a", "a c", "a c", "c a"]))