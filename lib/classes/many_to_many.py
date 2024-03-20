class Article:
    # Class variable to keep track of all articles
    all = []

    # Constructor method to initialize an article with an author, magazine, and title
    def __init__(self, author, magazine, title):
        self.author = author  # Assign the author
        self.magazine = magazine  # Assign the magazine
        self.title = title  # Assign the title
        Article.all.append(self)  # Add this article to the list of all articles
        
    # Getter method for the title property
    def get_title(self):
        return self._title
    
    # Setter method for the title property
    def set_title(self, new_title):
        # Check if the new title is a string and its length is between 5 and 50 characters
        if isinstance(new_title, str) and len(new_title) >= 5 and len(new_title) <= 50 and not hasattr(self, "_title"):
            self._title = new_title  # Set the title
        
    # Define the title property using the getter and setter methods
    title = property(get_title, set_title)
        

class Author:
    # Constructor method to initialize an author with a name
    def __init__(self, name):
        self.name = name  # Assign the name
        self.set_name(name)  # Set the name

    # Getter method for the name property
    def get_name(self):
        return self._name
    
    # Setter method for the name property
    def set_name(self, new_name):
        # Check if the new name is a string and its length is greater than 0
        if isinstance(new_name, str) and len(new_name) > 0 and not hasattr(self, '_name'):
            self._name = new_name  # Set the name
        else:
            print(f'invalid name: {new_name}')  # Print error message if the name is invalid

    # Define the name property using the getter and setter methods
    name = property(get_name, set_name)

    # Method to get all articles written by this author
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # Method to get all magazines contributed by this author
    def magazines(self):
        magazine_set = set()  # Create an empty set to store unique magazines
        for article in self.articles():  # Loop through all articles by this author
            magazine_set.add(article.magazine)  # Add the magazine of each article to the set
        return list(magazine_set)  # Convert the set to a list and return it

    # Method to add a new article associated with this author
    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)  # Create a new article instance
        return new_article  # Return the new article

    # Method to get unique topic areas for all articles written by this author
    def topic_areas(self):
        if not self.articles():  # If the author has no articles
            return None
        # Create a list of unique topic areas by extracting categories from articles
        return list(set([article.magazine.category for article in self.articles()]))


class Magazine:
    # Constructor method to initialize a magazine with a name and category
    def __init__(self, name, category):
        self.name = name  # Assign the name
        self.set_name(name)  # Set the name
        self.category = category  # Assign the category
        self.set_category(category)  # Set the category
        
    # Getter method for the name property
    def get_name(self):
        return self._name

    # Setter method for the name property
    def set_name(self, new_name):
        # Check if the new name is a string and its length is between 2 and 16 characters
        if isinstance(new_name, str) and len(new_name) <= 16 and len(new_name) >= 2:  
            self._name = new_name  # Set the name
        else:
            print(f'invalid name: {new_name}')  # Print error message if the name is invalid

    # Define the name property using the getter and setter methods
    name = property(get_name, set_name)

    # Getter method for the category property
    def get_category(self):
        return self._category
    
    # Setter method for the category property
    def set_category(self, new_category):
        # Check if the new category is a string and its length is greater than 0
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category  # Set the category
        else:
            print(f'invalid category: {new_category}')  # Print error message if the category is invalid
            
    # Define the category property using the getter and setter methods
    category = property(get_category, set_category)

    # Method to get all articles published by this magazine
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # Method to get unique contributors (authors) for this magazine
    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine == self]))

    # Method to get titles of all articles published by this magazine
    def article_titles(self):
        if not self.articles():  # If the magazine has no articles
            return None
        # Create a list of article titles published by this magazine
        return [article.title for article in self.articles()]

    # Method to get authors who have written more than 2 articles for this magazine
    def contributing_authors(self):
        d = {}  # Create an empty dictionary to count articles by each author
        for article in self.articles():  # Loop through all articles published by this magazine
            if article.author in d:  # If the author is already in the dictionary
                d[article.author] += 1  # Increment the article count
            else:
                d[article.author] = 1  # Add the author to the dictionary
        contributors = []  # Create an empty list to store contributing authors
        for author in d:  # Loop through authors in the dictionary
            article_count = d[author]  # Get the article count for the author
            if article_count >= 2:  # If the author has written more than 2 articles
                contributors.append(author)  # Add the author to the list of contributors
        if not contributors:  # If there are no contributing authors
            return None
        return contributors  # Return the list of contributing authors










   


