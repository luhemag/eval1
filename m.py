class MovieRentalService:
    def __init__(self):
        self.available_movies = {
            'stree 2': True,
            'mehul': True,
            'luka chupi': True,
            'rab na bana di jodi': True,
            'The God': True
        }
        
    
        self.customers = {}
        
        
        self.rentals = []

    def rent_movie(self, customer_name, movie_title):

        if self.available_movies.get(movie_title) == True:
        
            if customer_name not in self.customers:
                self.customers[customer_name] = []
        
            self.customers[customer_name].append(movie_title)
            self.available_movies[movie_title] = False
            self.rentals.append({'customer': customer_name, 'movie': movie_title, 'action': 'rented'})
            print(f"Movie '{movie_title}' rented to customer '{customer_name}'.")
        else:
            print(f"Sorry, the movie '{movie_title}' is not available.")

    def return_movie(self, customer_name, movie_title):
    
        if customer_name in self.customers and movie_title in self.customers[customer_name]:

            self.customers[customer_name].remove(movie_title)
            self.available_movies[movie_title] = True
            self.rentals.append({'customer': customer_name, 'movie': movie_title, 'action': 'returned'})
            print(f"Movie '{movie_title}' returned by customer '{customer_name}'.")
        else:
            print(f"Error: Movie '{movie_title}' was not rented by customer '{customer_name}'.")

    def generate_rental_report(self):
        print("\nRental Report:")
        for transaction in self.rentals:
            print(f"Customer: {transaction['customer']}, Movie: {transaction['movie']}, Action: {transaction['action']}")

    def display_available_movies(self):
        print("\nAvailable Movies:")
        for movie, available in self.available_movies.items():
            status = 'Available' if available else 'Not Available'
            print(f"{movie}: {status}")
if __name__ == "__main__":
    service = MovieRentalService()

    service.display_available_movies()

    service.rent_movie('gurkirt', 'mehul')
    service.rent_movie('garv', 'The God')

    
    service.display_available_movies()


    service.return_movie('gurkirt', 'mehul')

    service.display_available_movies()

 
    service.generate_rental_report()
