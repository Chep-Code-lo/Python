import numpy as np
def combine_rooms(room_1, room_2):
    ans = []
    for a, b in zip(room_1, room_2):
        if a > 0:
            ans.append(a)
        elif b > 0:
            ans.append(b)
        else:
            ans.append(None)
    return np.array(ans)
room_1 = np.array([1, 2, -3, 4, 5, 6, -7])
room_2 = np.array([8, 9, 10, 11, 12, -13, -14])

print(combine_rooms(room_1, room_2))
