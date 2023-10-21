class player:
  def play(self):
    print ("the player is playing cricket ")
class Batsman (player):
  def play(self):
    print ("the batsman is batting ")
class bowler(player):
      def play(self):
        print("the bowler is bowling")
batsman=Batsman()
bowler=bowler()
batsman.play()
bowler.play()

