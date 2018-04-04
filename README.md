# Find Books

The format of the input files are:
- pipe: First name | Last name | Book Title | Book Publication Date
- slash: Book Publication Date/First name/Last name/Book Title
- csv: Book Title, Last Name, First name, Book Publication Date


```
$ python3 books.py --help

usage: books.py [-h] [--filter FILTER] [--year] [--reverse] [--version]

Tool which shows a list of books in alphabetical ascending by author's last
name

optional arguments:  
  -h, --help       show this help message and exit  
  --filter FILTER  Show a subset of books, looks for the argument as a
                   substring of any of the fields  
  --year           sort the books by year, ascending instead of default sort  
  --reverse        reverse sort  
  --version        show program's version number and exit  
```

Some sample outputs of the program:  

```
$ python3 books.py --filter 199 --reverse
McConnell, Steve, Code Complete, 1993  
Fowler, Martin, Refactoring, 1999  
```

```
$ python3 books.py --filter er --year

Fowler, Martin, Refactoring, 1999  
Fowler, Martin, Patterns of Enterprise Application Architecture, 2002  
Beck, Kent, Implementation Patterns, 2007  
Martin, Robert, Clean Code, 2008  
```

```
$ python3 books.py

Beck, Kent, Test-Driven Development, 2002  
Beck, Kent, Implementation Patterns, 2007  
Brooks, Fred, The Mythical Man-Month, 1975  
Crockford, Douglas, Javascript: The Good Parts, 2008  
Fowler, Martin, Refactoring, 1999  
Fowler, Martin, Patterns of Enterprise Application Architecture, 2002  
Martin, Robert, Clean Code, 2008  
McConnell, Steve, Code Complete, 1993  
Shore, James, The Art of Agile Development, 2008
```

```
$ python3 books.py --filter Fo --year --reverse

Fowler, Martin, Patterns of Enterprise Application Architecture, 2002
Fowler, Martin, Refactoring, 1999
```

```
$ python3 books.py --year --reverse

Martin, Robert, Clean Code, 2008
Shore, James, The Art of Agile Development, 2008
Crockford, Douglas, Javascript: The Good Parts, 2008
Beck, Kent, Implementation Patterns, 2007
Beck, Kent, Test-Driven Development, 2002
Fowler, Martin, Patterns of Enterprise Application Architecture, 2002
Fowler, Martin, Refactoring, 1999
McConnell, Steve, Code Complete, 1993
Brooks, Fred, The Mythical Man-Month, 1975
```

```
$ python3 books.py --filter 00  --year --reverse

Martin, Robert, Clean Code, 2008
Shore, James, The Art of Agile Development, 2008
Crockford, Douglas, Javascript: The Good Parts, 2008
Beck, Kent, Implementation Patterns, 2007
Beck, Kent, Test-Driven Development, 2002
Fowler, Martin, Patterns of Enterprise Application Architecture, 2002
```

```
$ python3 books.py --version

v.1.0.0
```