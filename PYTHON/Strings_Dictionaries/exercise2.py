def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    list_doc=[article.replace(","," ").replace("."," ").lower() for article in doc_list]
    result = [list_doc.index(article) for article in list_doc if keyword in article.split()]
    return result

# Check your answer
#q2.check()