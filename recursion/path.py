def get_path(start: int) -> list:
    """
    G
    """
    results = []
    getPathHelper(start, results)
    return results
    # 10 5 16 8 4 2 1

def getPathHelper(start, result):
    result.append(start)
    if start == 1:
        return
    else:
        if start %2 == 0:
            getPathHelper(start // 2, result)
        else:
            getPathHelper(start * 3 + 1, result)

        
        

value = 10
print(f"The path from {value} to 1 is: {get_path(value)}")