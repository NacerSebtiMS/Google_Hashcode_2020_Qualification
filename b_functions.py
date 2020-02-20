def scorify_library(library):
    """
    The aim is to give the libraries a score, that will enable to order them later on
    """
    NB = library[0]
    BD = library[2]
    SB = library_total_book_score(library)
    DR = library[1]
    library_scoring = (D - DR) * BD * (SB/NB)
    return library_scoring



def library_total_book_score(library):
    book_ids = library[3]
    total_library_book_score = 0
    for id in book_ids:
        total_library_book_score += BL[id]
    return total_library_book_score
