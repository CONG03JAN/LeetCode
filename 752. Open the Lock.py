from typing import List
import queue

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        locks = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        q = queue.Queue()
        count = 0
        q.put("0000")
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0

        cnt = 0
        while not q.empty():
            count += 1
            tmp = q.get()
            for i in range(4):
                new_tmp = tmp[:i] + locks[int(tmp[i])] + tmp[i+1:]
                if new_tmp in deadends:
                    return -1
                elif new_tmp == target:
                    return count
                else:
                    q.put(new_tmp)


        return -1
        
