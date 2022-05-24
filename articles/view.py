def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print('Input'.center(50, '='))
            output=func(*args, **kwargs)
            print('=' * 50)
            return output
        return wrap
    return wrapper





class UserInterface:
    @add_title('Vvod polzovatelskih dannih')
    def wait_user_answer(self):

        print('Work with articles:')
        print('1 - made article')
        print('2 - show articles')
        print('3 - show article')
        print('4 - delete article')
        print('q - exit out programm')
        user_answer=input('Variant: ')
        print('='*50)
        return user_answer
    @add_title("Made article:")
    def add_user_article(self):
        dict_article={
            'name':None,
            'author':None,
            'valscript':None,
            'artic':None
        }
        for key in dict_article:
            dict_article[key] = input(f'input {key} article: ')
        print('=' * 50)
        return dict_article

    @add_title('List articles')
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, start=1):
            print(f'{ind}. {article}')
        print('='*50)
    @add_title('Input articlename')
    def get_user_article(selfself):
        user_article=input('Article name: ')
        return user_article
    @add_title('Show article')
    def show_single_article(self, article):
        for key in article:
            print(f'{key} article - {article[key]}')

    @add_title('Error messange')
    def show_incorretc_title_error(self, user_title):
        print(f'This article {user_title} is not')

    @add_title('Delelte article')
    def remove_single_article(self, article):
        print(f'Article {article} was deleted')
    @add_title('Error messange')
    def show_incorrect_answer_error(self,answer):
        print(f'This variant {answer} is not')

