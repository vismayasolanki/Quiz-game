# Quiz-game

Project Report
How to run
1. First open 4 terminals
2. In the first terminal run server.py
1. Python3 server.py
3. In the other 3 terminals run client.py
2. Python3 client.py <IP address>
4. The rules of game will appear to clients
5. Enjoy the game
Assumptions
• Your port number – 12,000 is free. (as it is hardcoded).
Description of code
1. This game is coded in python3
2. The following inbuilt python modules are used
• Socket
• Time
• Sys
• Select
• Threading
• Random
3. The host will first wait for 3 players to join
4. Then it will start sending questions to all the players at same time
5. The question bank has simple addition questions in range [1,50] randomly arranged by the shuffle function of random library.
6. If buzzer is not pressed (until 10 seconds) then by timeout parameter of select function it will move forward.
7. The buzzer is implemented using select module on server side. It will show who is prompting and hence give him a chance.
8. If buzzer is pressed, then the person pressing buzzer will be given 10 seconds to answer by a threading function in client-side script
9. If person answers correct, then he is awarded one point otherwise deducted half point
10. In every iteration the script checks if any player has reached 5 points. If yes, he is declared winner
11. if 50 question happens still no one wins then game is called and nobody wins.
Rules of the game
1. After 3 players will join then the game will start
2. The question will appear
3. If any player knows the answer then he should press the buzzer by pressing “y” (without quotes).
4. The first player to press the buzzer will be given the chance to answer
5. After pressing buzzer, the player will be given 10 seconds to answer the questions. If he is not able to answer the question, then it will be considered as a wrong answer.
6. If nobody knows the answer and nobody presses the buzzer then the host will move forward to next question in 10 seconds.
PS : - There are screenshot attached of working script
They are in following order
1. When server.py is only run
2. When all 3 clients have connected
3. Some questions passing due to no pressing of buzzer
4. Player 1(top-right) pressed buzzer
5. Player 1(top-right) gives the correct answer within 10 seconds.
6. Player 1(top-right) pressed buzzer and did not give answer in 10 seconds.
7. Player 1 finishes the game by scoring 5 points.
8. All 50 questions are exhausted so nobody won.
