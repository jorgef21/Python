""" 
The input is a list of bits called “seats”. This list has a 1 if the seat is taken and a 0 if it is empty. For example,
if the first, fourth, and seventh seats are occupied, the input will be [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]. 
Your goal is to find the seat index that is the farthest away from the next closest occupied seat, 
and return that seat’s index. The input list is always ordered numerically. It is possible, given some inputs,
 to HAVE 2 seats both be the farthest from any occupied seat. In this case, return the lower index

1 = In use
0 = Free Seat
"""
seats_1 = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0] #should return 9    --from example
seats_2 = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0] #should return 4    -- from example
seats_3 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0] #should return 0  -- from example
seats_4 = [1,1,0,1,1] # shuld return 2
seats_5 = [0,0,1,0,1,1] #should return 0
seats_6 = [0,1,0,1,1]   #should return 0
seats_7 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
seats_8 = [1,0,1]
seats_9 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0]
seats_10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,1]

def findBestSeat(seats):
    pairs = []
    current_first = None
    first_free = None
    for index, num in enumerate(seats):
        if num == 1:
            if current_first is None:
                first_free = index
                current_first = index
            else:
                pairs.append((current_first, index))
                current_first = index
    last_free = current_first 
    max_distance = 0
    current_max = None
    for pair in pairs:
        distance = pair[1] - pair[0] - 1
        if distance > max_distance:
            max_distance = distance
            current_max = pair
    
    if max_distance <= first_free and seats[0] != 1:
        return 0
    if max_distance < len(seats) - last_free:
        return len(seats) - 1
    return current_max[0] + (current_max[1] - current_max[0]) // 2
def main():   
  print('Seats: '+str(seats_1)+'  BEST SEAT IS: '+str(findBestSeat(seats_1)))
  print('Seats: '+str(seats_2)+'  BEST SEAT IS: '+str(findBestSeat(seats_2)))
  print('Seats: '+str(seats_3)+'  BEST SEAT IS: '+str(findBestSeat(seats_3)))
  print('Seats: '+str(seats_4)+'  BEST SEAT IS: '+str(findBestSeat(seats_4)))
  print('Seats: '+str(seats_5)+'  BEST SEAT IS: '+str(findBestSeat(seats_5)))
  print('Seats: '+str(seats_6)+'  BEST SEAT IS: '+str(findBestSeat(seats_6)))
  print('Seats: '+str(seats_7)+'  BEST SEAT IS: '+str(findBestSeat(seats_7)))
  print('Seats: '+str(seats_8)+'  BEST SEAT IS: '+str(findBestSeat(seats_8)))
  print('Seats: '+str(seats_9)+'  BEST SEAT IS: '+str(findBestSeat(seats_9)))
  print('Seats: '+str(seats_10)+'  BEST SEAT IS: '+str(findBestSeat(seats_10)))

if __name__ == "__main__":
    main()