class Solution9:
    def apple_question(self, n, array):

        array.sort()
        if len(array) == 1:
            return "1"
        ans = sys.maxsize
        k1 = array[0] + array[-1] # remove middle
        k2 = array[0] + array[-2] # remove -1
        k3 = array[1] + array[-1] # remove N

        left, right = 0, len(array) - 1
        skip = 0
        c = array[left]

        while(left <= right):
            s = array[left] + array[right]
            if left == right:
                c = array[left]
                skip += 1
                break
            if s == k1:
                left += 1
                right -= 1
            elif s < k1:
                if left == right - 1:
                    skip = 2
                    break
                skip += 1
                c = array[left]
                left += 1
            elif s > k1:
                if left == right - 1:
                    skip = 2
                    break
                skip += 1
                c = array[right]
                right -= 1
            if skip > 1:
                break
        if skip <= 1 and k1 - c > 0:
            ans = min(ans, k1 - c)


        left, right = 0, len(array) - 2
        skip = 0
        candid = array[-1]
        while (left < right):
            s = array[left] + array[right]
            if left == right:
                skip += 1
                break
            if s == k2:
                left += 1
                right -= 1
            elif s < k2:
                if left == right - 1:
                    skip = 2
                    break
                skip += 1
                left += 1
            elif s > k2:
                if left == right - 1:
                    skip = 2
                    break
                skip += 1
                right -= 1
            if skip > 1:
                break
        if skip <= 1 and k2 - candid > 0:
            ans = min(ans, k2 - candid)


        left, right = 1, len(array) - 1
        skip = 0
        candid = array[0]
        while (left < right):
            s = array[left] + array[right]
            if left == right:
                skip += 1
                break
            if s == k3:
                left += 1
                right -= 1
            elif s < k3:
                if left == right - 1:
                    skip = 2
                    break
                skip += 1
                left += 1
            elif s > k3:
                if left == right - 1:
                    skip = 2
                    break
                skip += 1
                right -= 1
            if skip > 1:
                break
        if skip <= 1 and k3 - candid > 0:
            ans = min(ans, k3 - candid)

        return str(ans) if ans < sys.maxsize else "-1"


if __name__ == '__main__':
    s = Solution9()
    print("Case #1: " + s.apple_question(3, [6, 3, 1, 2, 5]) + " vs  4")
    print("Case #2: " + s.apple_question(2, [7, 7, 7]) + " vs  7")
    print("Case #3: " + s.apple_question(1, [1]) + " vs  1")
    print("Case #4: " + s.apple_question(3, [1, 9, 1, 1, 4]) + " vs  -1")
    print("Case #5: " + s.apple_question(4, [1, 9, 1, 1, 4, 9, 9]) + " vs  6")
    print("Case #6: " + s.apple_question(4, [1, 9, 10, 1, 4, 6, 9]) + " vs  -1")
    print("Case #7: " + s.apple_question(3, [1000000000, 2, 10, 4, 999999994]) + " vs  1000000002")
