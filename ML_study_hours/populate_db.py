import sqlite3

#connect to database
connection = sqlite3.connect('study_data.db')
cursor = connection.cursor()


#Manually defining data for all weeks
study_data = [
    #week 1
    (1, 'monday', 0),
    (1, 'tuesday', 4),
    (1, 'wednesday', 4),
    (1, 'thursday', 7),
    (1, 'friday', 6),
    (1, 'saturday', 0),
    (1, 'sunday', 0),

    #week 2
    (2, 'monday', 3),
    (2, 'tuesday', 3),
    (2, 'wednesday', 3),
    (2, 'thursday', 2),
    (2, 'friday', 2),
    (2, 'saturday', 0),
    (2, 'sunday', 1),

    #week 3
    (3, 'monday', 5),
    (3, 'tuesday', 4),
    (3, 'wednesday', 0),
    (3, 'thursday', 7),
    (3, 'friday', 1),
    (3, 'saturday', 0),
    (3, 'sunday', 0),

    #week 4
    (4, 'monday', 0),
    (4, 'tuesday', 3),
    (4, 'wednesday', 6),
    (4, 'thursday', 4),
    (4, 'friday', 0),
    (4, 'saturday', 0),
    (4, 'sunday', 5),

    #week 5
    (5, 'monday', 2),
    (5, 'tuesday', 5),
    (5, 'wednesday', 4),
    (5, 'thursday', 0),
    (5, 'friday', 0),
    (5, 'saturday', 0),
    (5, 'sunday', 0),

    #week 6
    (6, 'monday', 5),
    (6, 'tuesday', 0),
    (6, 'wednesday', 2),
    (6, 'thursday', 7),
    (6, 'friday', 4),
    (6, 'saturday', 3),
    (6, 'sunday', 2),

    #week 7
    (7, 'monday', 4),
    (7, 'tuesday', 3),
    (7, 'wednesday', 5),
    (7, 'thursday', 1),
    (7, 'friday', 0),
    (7, 'saturday', 1),
    (7, 'sunday', 0),

    #week 8
    (8, 'monday', 6),
    (8, 'tuesday', 3),
    (8, 'wednesday', 5),
    (8, 'thursday', 0),
    (8, 'friday', 0),
    (8, 'saturday', 5),
    (8, 'sunday', 0),

    #week 9
    (9, 'monday', 4),
    (9, 'tuesday', 8),
    (9, 'wednesday', 0),
    (9, 'thursday', 5),
    (9, 'friday', 4),
    (9, 'saturday', 0),
    (9, 'sunday', 0),

    #week 10
    (10, 'monday', 0),
    (10, 'tuesday', 0),
    (10, 'wednesday', 0),
    (10, 'thursday', 0),
    (10, 'friday', 2),
    (10, 'saturday', 0),
    (10, 'sunday', 0),

    #week 11
    (11, 'monday', 0),
    (11, 'tuesday', 4),
    (11, 'wednesday', 0),
    (11, 'thursday', 2),
    (11, 'friday', 0),
    (11, 'saturday', 0),
    (11, 'sunday', 0),

    #week 12
    (12, 'monday', 0),
    (12, 'tuesday', 0),
    (12, 'wednesday', 0),
    (12, 'thursday', 0),
    (12, 'friday', 1),
    (12, 'saturday', 0),
    (12, 'sunday', 0),

    #week 14
    (14, 'monday', 2),
    (14, 'tuesday', 7),
    (14, 'wednesday', 2),
    (14, 'thursday', 5),
    (14, 'friday', 2),
    (14, 'saturday', 0),
    (14, 'sunday', 0),

    #week 15
    (15, 'monday', 0),
    (15, 'tuesday', 3),
    (15, 'wednesday', 6),
    (15, 'thursday', 3),
    (15, 'friday', 7),
    (15, 'saturday', 0),
    (15, 'sunday', 7),

    #week 16
    (16, 'monday', 7),
    (16, 'tuesday', 7),
    (16, 'wednesday', 0),
    (16, 'thursday', 0),
    (16, 'friday', 4),
    (16, 'saturday', 1),
    (16, 'sunday', 6),

    #week 17
    (17, 'monday', 0),
    (17, 'tuesday', 2),
    (17, 'wednesday', 0),
    (17, 'thursday', 4),
    (17, 'friday', 0),
    (17, 'saturday', 0),
    (17, 'sunday', 0),

    #week 20
    (20, 'monday', 0),
    (20, 'tuesday', 0),
    (20, 'wednesday', 0),
    (20, 'thursday', 0),
    (20, 'friday', 0),
    (20, 'saturday', 1),
    (20, 'sunday', 4),

    #week 21
    (21, 'monday', 2),
    (21, 'tuesday', 3),
    (21, 'wednesday', 3),
    (21, 'thursday', 2),
    (21, 'friday', 0),
    (21, 'saturday', 0),
    (21, 'sunday', 0),

    #week 22
    (22, 'monday', 4),
    (22, 'tuesday', 4),
    (22, 'wednesday', 2),
    (22, 'thursday', 4),
    (22, 'friday', 0),
    (22, 'saturday', 0),
    (22, 'sunday', 0),

    #week 23
    (23, 'monday', 0),
    (23, 'tuesday', 4),
    (23, 'wednesday', 0),
    (23, 'thursday', 0),
    (23, 'friday', 9),
    (23, 'saturday', 2),
    (23, 'sunday', 2),

    #week 34
    (34, 'monday', 0),
    (34, 'tuesday', 2),
    (34, 'wednesday', 0),
    (34, 'thursday', 3),
    (34, 'friday', 3),
    (34, 'saturday', 0),
    (34, 'sunday', 0),

    #week 35
    (35, 'monday', 3),
    (35, 'tuesday', 2),
    (35, 'wednesday', 0),
    (35, 'thursday', 0),
    (35, 'friday', 3),
    (35, 'saturday', 0),
    (35, 'sunday', 0),

    #week 36
    (36, 'monday', 6),
    (36, 'tuesday', 0),
    (36, 'wednesday', 0),
    (36, 'thursday', 0),
    (36, 'friday', 3),
    (36, 'saturday', 0),
    (36, 'sunday', 5),

    #week 37
    (37, 'monday', 0),
    (37, 'tuesday', 5),
    (37, 'wednesday', 7),
    (37, 'thursday', 1),
    (37, 'friday', 1),
    (37, 'saturday', 0),
    (37, 'sunday', 0),

    #week 38
    (38, 'monday', 5),
    (38, 'tuesday', 5),
    (38, 'wednesday', 3),
    (38, 'thursday', 0),
    (38, 'friday', 0),
    (38, 'saturday', 1),
    (38, 'sunday', 0),

    #week 39
    (39, 'monday', 4),
    (39, 'tuesday', 6),
    (39, 'wednesday', 0),
    (39, 'thursday', 7),
    (39, 'friday', 3),
    (39, 'saturday', 0),
    (39, 'sunday', 0),

    #week 40
    (40, 'monday', 4),
    (40, 'tuesday', 4),
    (40, 'wednesday', 4),
    (40, 'thursday', 4),
    (40, 'friday', 2),
    (40, 'saturday', 0),
    (40, 'sunday', 0),

    #week 43
    (43, 'monday', 0),
    (43, 'tuesday', 3),
    (43, 'wednesday', 0),
    (43, 'thursday', 4),
    (43, 'friday', 0),
    (43, 'saturday', 0),
    (43, 'sunday', 0),

    #week 44
    (44, 'monday', 3),
    (44, 'tuesday', 0),
    (44, 'wednesday', 0),
    (44, 'thursday', 5),
    (44, 'friday', 0),
    (44, 'saturday', 2),
    (44, 'sunday', 4),

    #week 45
    (45, 'monday', 4),
    (45, 'tuesday', 0),
    (45, 'wednesday', 6),
    (45, 'thursday', 3),
    (45, 'friday', 0),
    (45, 'saturday', 4),
    (45, 'sunday', 0),

    #week 46
    (46, 'monday', 0),
    (46, 'tuesday', 2),
    (46, 'wednesday', 0),
    (46, 'thursday', 0),
    (46, 'friday', 0),
    (46, 'saturday', 0),
    (46, 'sunday', 0),

    #week 47
    (47, 'monday', 2),
    (47, 'tuesday', 2),
    (47, 'wednesday', 2),
    (47, 'thursday', 2),
    (47, 'friday', 2),
    (47, 'saturday', 0),
    (47, 'sunday', 0),

    #week 48
    (48, 'monday', 3),
    (48, 'tuesday', 3),
    (48, 'wednesday', 3),
    (48, 'thursday', 4),
    (48, 'friday', 0),
    (48, 'saturday', 0),
    (48, 'sunday', 5),

    #week 49
    (49, 'monday', 3),
    (49, 'tuesday', 3),
    (49, 'wednesday', 3),
    (49, 'thursday', 4),
    (49, 'friday', 0),
    (49, 'saturday', 0),
    (49, 'sunday', 0),

    #week 50
    (50, 'monday', 7),
    (50, 'tuesday', 4),
    (50, 'wednesday', 1),
    (50, 'thursday', 5),
    (50, 'friday', 0),
    (50, 'saturday', 0),
    (50, 'sunday', 0),

]

#inserting data into table
cursor.executemany('''
    INSERT INTO study_hours (week, day, hours)
    VALUES (?, ?, ?)
''', study_data)

#commit and close connection
connection.commit()
connection.close()

print("Data inserted successfully")