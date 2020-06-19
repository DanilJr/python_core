class Ball(object):
    
    def __init__(self, type='regular'):
        self.ball_type = type

    def ball_type(self):
        return self.ball_type



ball1=Ball('super')

ball2=Ball('super-puper')  

ball3=Ball()

print(ball1.ball_type)
print(ball2.ball_type)
print(ball3.ball_type)