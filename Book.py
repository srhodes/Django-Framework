class Book:
    def __init__(self, name):
        self.name = name
        



the_art_of_compute_programming = Book('The Art of Computer Program')
learning_python = Book('Learning Python in 100 Steps')
learning_restful_services = Book('Learning RestFu; Service in 50 Steps')

print(the_art_of_compute_programming.name)
print(learning_python.name)
print(learning_restful_services.name)


