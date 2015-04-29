#-----Aligning-----    

                #while not wallOnRight and not wallInFront:
                #                print("-----tr-----")
                #                turnRight(0.3, 100)
                #                forward(0.5, 100)
                #		 wallInFront = frontWallCheck()
                #                wallOnRight = rightWallCheck()

                #-----Turning-----                   
                                    
                if wallOnRight:# and wallInFront:
                    print("-----tlb-----")
                    backward(1)
                    turnLeft(0.9)
                    forward(0.3)
                    turnLeft(1.5)
                    forward(1)
                    turnLeft(1)

                    #wallInFront = frontWallCheck()
                    #wallOnRight = rightWallCheck()
                                            
                    #while wallInFront or not wallOnRight:
                    #        print("-----tl-----")
                    #        turnLeft(0.3, 100)
                    #        forward(0.3, 100)
                    #        turnLeft(0.3, 100)
                    #        backward(0.3, 100)
                    #        wallInFront = frontWallCheck()
                    #        wallOnRight = rightWallCheck()
                
                elif not wallOnRight:# and wallInFront:
                    print("-----trb-----")
                    myStop()
                    sleep(2)
                    turnRight()

                    #backward(0.6)
                    #turnRight(2)
                    #backward(0.6)
                    #turnRight(2.1 + 0.3)
                    #forward(3.3)

                    #wallInFront = frontWallCheck()
                    #wallOnRight = rightWallCheck()			
                                           
                    #while not wallOnRight and not wallInFront:
                    #        print("-----tr-----")
                    #        turnRight(0.3, 100)
                    #        forward(0.5, 100)
                    #	 wallInFront = frontWallCheck()
                    #        wallOnRight = rightWallCheck()
