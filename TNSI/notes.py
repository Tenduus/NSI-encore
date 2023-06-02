def demander_entier_V2(message : str) -> int :
    """ ==================================================================================================================
    
        * Description : 
            Je demande à l'utilisateur un nombre correspondant à la question du message et renvoie le résultat au format entier ;
                > avec une gestion de vérification de la validité de la saisie utilisateur.
                        
        * Exemple :
            >>> demander_entier("Combien de notes sont à saisir ? ")
            Combien de notes sont à saisir ? 5
            5
                                           
        * Préconditions :
            message (str) : question définissant le nombre à saisir ;
                    
        * Postconditions :
            (int) : la valeur saisie convertie en entier.       
        
        ==================================================================================================================
    """
    # Assertions de vérification des préconditions :
    assert type(message) == str  , "Le message doit être une chaine de caractères."
            
    # bloc d'instructions :
    try :
        nombre = int(input(message))
        return nombre
    except ValueError :
        print("La valeur saisie doit être convertible en un nombre entier exprimé en base 10 : \n    -> la saisie ne doit pas contenir d'autres caractères que 0, 1, 2, 3, 4, 5, 6, 7, 8, 9")



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def saisir_note() -> float :
    """ ==================================================================================================================   

        * Description : 
            Je demande à l'utilisateur un nombre float compris entre 0 et 20 et renvoie le résultat au format float ;
                > avec une gestion de vérification de la validité de la saisie utilisateur.
                        
        * Exemple :
            >>> saisir_note()
            Votre note :15
            15.0
                                           
        * Préconditions :
            /
                    
        * Postconditions :
            float : la valeur saisie par l'utilisateur       
        
        ==================================================================================================================
    """
    # Instructions A CODER
    try:
        note = float(input("Votre note :"))
        assert 0 <= note <= 20, "Votre note n'es pas comprise entre 0 et 20 !"
        return note
    except AssertionError:
        print("La valeur saisie doit être un nombre entier ou décimal compris entre en 0 et 20")
        saisir_note()



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def minimum_table(valeurs:list) -> float :
    """ ==================================================================================================================
    
        * Description : 
            Je demande à l'utilisateur une liste et je renvois la valeur la plus faible de celle-ci.
                        
        * Exemple :
            >>> minimum_table([3, 7, 6, 9])
            3
                                           
        * Préconditions :
            valeurs:list : liste dans laquelle on cherche le minimum ;
                    
        * Postconditions :
            (int) : la valeur minimum de la liste.       
        
        ==================================================================================================================
    """
    # Instructions A CODER
    minimum = valeurs[0]
    for i in valeurs:
        if i < minimum:
            minimum = i
    return minimum



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def maximum_table(valeurs:list) -> float :
    """ ==================================================================================================================
    
        * Description : 
            Je demande à l'utilisateur une liste et je renvois la valeur la plus élevée de celle-ci.
                        
        * Exemple :
            >>> maximum_table([3, 7, 6, 9])
            9
                                           
        * Préconditions :
            valeurs:list : liste dans laquelle on cherche le maximum ;
                    
        * Postconditions :
            (int) : la valeur maximum de la liste.       
        
        ==================================================================================================================
    """
    # Instructions A CODER
    maximum = valeurs[0]
    for i in valeurs:
        if i > maximum:
            maximum = i
    return maximum



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def moyenne_table(valeurs:list) -> float :
    """ ==================================================================================================================
    
        * Description : 
            Je demande à l'utilisateur une liste et je renvois la moyenne des valeurs comrpises dans celle-ci.
                        
        * Exemple :
            >>> moyenne_table([3, 7, 6, 9])
            6.0
                                           
        * Préconditions :
            valeurs:list : liste dont on veut la moyenne ;
                    
        * Postconditions :
            (float) : moyenne de la liste.       
        
        ==================================================================================================================
    """
    # Instructions A CODER
    moyenne = 0
    for i in valeurs:
        moyenne += i
    return moyenne/len(valeurs)