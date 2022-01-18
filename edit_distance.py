

def calDistance(str1, str2):

    m = len(str1)
    n =len(str2)

    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j    

            elif j == 0:
                dp[i][j] = i    
            
            #same char no action needed
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                #insert delete and replace
                dp[i][j] = 1 + min(dp[i][j-1],      
                                   dp[i-1][j],      
                                   dp[i-1][j-1])   

                #transposition
                if (i > 1 and j > 1 and (str1[i - 1] == str2[j - 2]) and (str1[i - 2] == str2[j - 1])):
                
                    dp[i][j] = min(dp[i][j], dp[i-2][j-2] + 1)
                
                
    return dp[m][n]

