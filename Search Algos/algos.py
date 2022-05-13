from functools import wraps

def warning(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            index = function(*args, **kwargs)

            return index

        except TypeError:
            print("Please provide a type target comparable with objects of a list")

            return None

        except Exception as ex:
            print("Exception Happened:")
            print(f"Exception type : {ex.__name__}")
            print(f"Exception message : {str(ex)}")

            return None
    
    return wrapper


class Algo:
    def __str__(self):
        return "Provides a few types of search algorithms. Separated to sorted and unsorted class respectively to symbolize to use either sorted or unsorted lists."

    def __repr__(self):
        return "Give sorted or unsorted objects that follows the iterator protocol\nTarget provided must be the an int."

    class Unsorted:
        @warning
        def linear_search(self, given_list: list, target):
            list_len = len(given_list)

            for i in range(list_len):
                if given_list[i] == target:
                    return i
            
            return None

    class Sorted:
        @warning
        def binary_serach(self, sorted_list: list, target):
            bottom = 0
            top = len(sorted_list) - 1

            while(top >= bottom):
                
                mid = (top + bottom) // 2

                # eliminate left
                if(sorted_list[mid] < target):
                    bottom = mid + 1

                # eliminate top
                elif(sorted_list[mid] > target):
                    top = mid - 1

                else:
                    return mid

            return None

        @warning
        def fibonacci_search(self, sorted_list: list, target):

            list_len = len(sorted_list)

            # Initilaise the 3 starting numbers in Fibonacci Series
            fib3 = 0
            fib2 = 1
            fib1 = 1

            # index start
            starting_index = -1
            
            # determine Fibonacci number bigger or equals to list length
            while(fib1 < list_len):
                fib3 = fib2
                fib2 = fib1
                fib1 = fib3 + fib2

            # while the largest fib number is bigger than the 3rd series number
            while(fib1 > 1):
                index = min(starting_index + fib3, list_len - 1)

                # move series number backwards 1; update starting_index 
                if sorted_list[index] < target:
                    fib1 = fib2
                    fib2 = fib3
                    fib3 = fib1 - fib2

                    starting_index = index

                elif sorted_list[index] > target:
                    fib1 = fib3
                    fib2 = fib2 - fib3
                    fib3 = fib1 - fib2

                else:
                    return index

            if fib2 and sorted_list[list_len - 1] == target:
                return list_len - 1
            
            return None

    class Uninformed:
        def depth_first_search(connected_graph):
            """
                Parameter connected_graph is an iteratable with a group element at index 0, followed
                by elements belonging to said group. Returns result where all nodes of a group is combined together
                for a clearer picture of a connected graph.
            """

            check = [False] * len(connected_graph)
            result = []

            def dfs(index, answer):
                if check[index]:
                    return
                    
                check[index] = True
                
                # get all node's neighbours
                for node_index in connected_graph[index][1:]:
                    answer.add(node_index)

                    dfs(node_index, answer)

            for index, node in enumerate(connected_graph):
                if check[index]:
                    continue

                group, answer = node[0], set()

                dfs(index, answer)

                result.append([group] + list(answer))

            return result

