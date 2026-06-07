#Basic Linear Search Function
def linear_search(arr,target):
    for index, item in enumerate(arr):
        if item == target:
            return index
  return - 1
  #Verbose Linear Search Function
  def linear_search_verbose(arr,target):
    print(f"\n searching for: {target}")
    print(f" list: {arr}")
