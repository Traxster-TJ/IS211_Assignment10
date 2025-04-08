import sqlite3

def get_person_info(cursor, person_id):
    """
    Retrieve information about a person by their ID
    
    Args:
        cursor: SQLite cursor object
        person_id: ID of the person to look up
        
    Returns:
        A tuple containing the person's data or None if not found
    """
    cursor.execute('''
    SELECT id, first_name, last_name, age 
    FROM person 
    WHERE id = ?
    ''', (person_id,))
    
    return cursor.fetchone()

def get_person_pets(cursor, person_id):
    """
    Retrieve information about a person's pets
    
    Args:
        cursor: SQLite cursor object
        person_id: ID of the person whose pets to look up
        
    Returns:
        A list of tuples containing pet data
    """
    cursor.execute('''
    SELECT p.name, p.breed, p.age, p.dead
    FROM pet p
    JOIN person_pet pp ON p.id = pp.pet_id
    WHERE pp.person_id = ?
    ''', (person_id,))
    
    return cursor.fetchall()

def main():
    """
    Main function to query the pets database based on user input
    """
    # Connect to the database
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    
    while True:
        try:
            user_input = input("\nEnter person ID (or -1 to exit): ")
            person_id = int(user_input)
            
            if person_id == -1:
                print("Exiting program...")
                break
            
            # Get person information
            person = get_person_info(cursor, person_id)
            
            if person:
                person_id, first_name, last_name, age = person
                print(f"{first_name} {last_name}, {age} years old")
                
                # Get their pets
                pets = get_person_pets(cursor, person_id)
                
                if pets:
                    for pet_name, pet_breed, pet_age, pet_dead in pets:
                        status = "was" if pet_dead else "is"
                        print(f"{first_name} {last_name} owned {pet_name}, a {pet_breed}, that {status} {pet_age} years old")
                else:
                    print(f"{first_name} {last_name} has no pets")
            else:
                print(f"Person with ID {person_id} does not exist")
                
        except ValueError:
            print("Please enter a valid ID number")
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
