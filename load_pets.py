import sqlite3

def main():
    """
    Connect to the pets.sql database
    """
    # Connect to the database
    conn = sqlite3.connect('pets.sql')
    cursor = conn.cursor()
    
    # Define the data to be inserted
    people = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]
    
    pets = [
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ]
    
    person_pets = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6)
    ]
    
    # Insert data into the person table
    cursor.executemany('INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?)', people)
    
    # Insert data into the pet table
    cursor.executemany('INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?)', pets)
    
    # Insert data into the person_pet table
    cursor.executemany('INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)', person_pets)
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    print("Data successfully loaded into pets.sql")

if __name__ == "__main__":
    main()
