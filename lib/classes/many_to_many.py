class Article:
    all=[]
    def __init__(self, author, magazine, title):
        self.author = author
        self._magazine = magazine
        self._title= None #Temp placeholder for self._title.Ensures it exists for validation later (line 17-18)
        self.title = title # Triggers the setter method(line 15-18). If the ._tiltle is None and title passes the validation,
                           # it assigns the value to None
        self._article=None# protected because it is not part of the constructor
        Article.all.append(self)

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,magazine):
        if not isinstance(magazine,Magazine):
            raise ValueError("Must be of type magazine")
        self._magazine=magazine

        
    @property
    def article(self):
        return self._article
    @article.setter
    def article(self,article):
        if not isinstance(article,Article):
            raise TypeError("Article must be an instance of Article class ")

    
    @property
    def title(self):
        return self._title

    
    @title.setter
    def title(self,title):
        
        if not isinstance(title,str) or not (5 <= len(title)<= 50):
            raise ValueError("must be string and characters between 5 and 50")
        if self._title is not None:
            raise AttributeError("The string has already been set.")
        self._title=title
   

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,author):
        if not isinstance(author,Author):
            raise ValueError("Must be of type Author")
        self._author=author
    
class Author:
    def __init__(self, name,magazine=None):
        self._name = None
        self.name = name
        self._magazine=None
        self.magazine=magazine
        
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        
        if not isinstance(name,str) or len(name) < 1:
            raise ValueError("Must be type str and longer than 0 characters")
        if self._name is not None:
            raise AttributeError("The string has already been set i.e immuttable") 
        self._name=name


    def articles(self):
        return [articled for articled in Article.all if articled.author==self]# collects the instances of the class Article

    def magazines(self):
        
        return {mag.magazine for mag in Article.all if mag.author==self and isinstance(mag.magazine,Magazine)} # collecting the magazine attribute hence .magazine

    def add_article(self, magazine, title):
        article=Article(self,magazine,title)
        return article

    def topic_areas(self):
        return{topic.magazine.category for topic in Article.all if topic.author==self}
        
from collections import Counter
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles=None
        self._contributor=set()

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not isinstance(name,str) or not (2 <= len(name)<= 16):
            raise ValueError("Must be string between 2 and 16 characters.")
        self._name=name
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self,category):
        if not isinstance(category,str) or  len(category) < 1:
            raise ValueError("Must be str and longer than 0 characters.")
        self._category=category
    def articles(self):
        return[article for article in Article.all if article.magazine==self]
    
    def contributors(self):
        return {contributor.author for contributor in Article.all if contributor.magazine==self}

    def article_titles(self):
        titles=[article.title for article in Article.all if article.magazine==self]
        return titles if titles else None
    def contributing_authors(self):
        authors = Counter(article.author for article in Article.all if article.magazine == self)
        authors_count=[author for author, count in authors.items() if count >2]
        return authors_count if authors_count else None
    @classmethod
    def top_publisher(cls):
        most_articles=Counter(article.articles for article in Article.all if article.magazine==cls)
        if not most_articles:
            return None
        winner_magazine=max(most_articles,key=most_articles.get)
        return winner_magazine