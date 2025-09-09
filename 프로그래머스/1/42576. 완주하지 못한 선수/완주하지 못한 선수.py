import collections

def solution(participant, completion):
    answer = ''
    participant_counts = collections.Counter(participant)
    completion_counts = collections.Counter(completion)

    result = participant_counts - completion_counts
    answer = list(result.keys())[0]
    return answer