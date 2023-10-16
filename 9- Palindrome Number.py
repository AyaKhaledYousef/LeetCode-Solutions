def isPalindrome( x ):

    number_str = str(x)
    
    # Reverse the number string
    reversed_str = number_str[::-1]

    if number_str == reversed_str :
        return True
    else :
        return False



if __name__ == '__main__':

    print(isPalindrome(321))

    
        
