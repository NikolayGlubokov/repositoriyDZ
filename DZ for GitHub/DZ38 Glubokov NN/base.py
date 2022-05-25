from display import DisplaySee
from operation import Operation



class Base:
    def __int__(self):
        self.display_movie=DisplaySee()
        self.operation_movie=Operation()

    def work(self):
        answer=None
        while answer !='q':
            answer=self.display_movie.menu_answer()
            self.variant_answer(answer)

        def variant_answer(self, answer):
            if answer =='1':
