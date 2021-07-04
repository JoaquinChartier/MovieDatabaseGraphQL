# This script will migrate all movies in the dataset to SQLiteDB
# Movies Dataset can be found here "https://data.world/jamesgaskin/movies"

from openpyxl import load_workbook
import sqlite3
wb = load_workbook('./movie_dataset.xlsx')

#Connecting
conn = sqlite3.connect('../db.sqlite3')

#Iterating movies
sheet = wb['Movies']
id = 2
while sheet['B'+str(id)].value != None:
    title = sheet['B'+str(id)].value
    MPAA_rating = sheet['C'+str(id)].value
    budget = sheet['D'+str(id)].value
    gross = sheet['E'+str(id)].value
    try:
        release_date = sheet['F'+str(id)].value.date()
    except:
        release_date = None
    genre = sheet['G'+str(id)].value
    runtime = sheet['H'+str(id)].value
    rating = sheet['I'+str(id)].value
    rating_count = sheet['J'+str(id)].value
    summary = sheet['K'+str(id)].value

    sql = f''' INSERT INTO MovieDatabase_movie(title,MPAA_rating,budget,gross,release_date,genre,runtime,rating,rating_count,summary)
              VALUES(?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (title,MPAA_rating,budget,gross,release_date,genre,runtime,rating,rating_count,summary))
    conn.commit()

    id += 1
print('movies ready')

#Iterating actors
sheet = wb['Actor']
id = 2
while sheet['B'+str(id)].value != None:
    name = sheet['B'+str(id)].value
    try:
        date_of_birth = sheet['C'+str(id)].value.date()
    except:
        date_of_birth = None
    birth_city = sheet['D'+str(id)].value
    birth_country = sheet['E'+str(id)].value
    height = sheet['F'+str(id)].value
    biography = sheet['G'+str(id)].value
    gender = sheet['H'+str(id)].value
    ethnicity = sheet['I'+str(id)].value

    sql = f''' INSERT INTO MovieDatabase_actor(name,date_of_birth,birth_city,birth_country,height,biography,gender,ethnicity)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (name,date_of_birth,birth_city,birth_country,height,biography,gender,ethnicity))
    conn.commit()

    id += 1
print('actors ready')

#Iterating characters
sheet = wb['Characters']
id = 2
while sheet['C'+str(id)].value != None:
    movie_id = sheet['A'+str(id)].value
    actor_id = sheet['B'+str(id)].value
    character_name = sheet['C'+str(id)].value
    credit_order = sheet['D'+str(id)].value

    sql = f''' INSERT INTO MovieDatabase_character(movie_id,actor_id,character_name,credit_order)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (movie_id,actor_id,character_name,credit_order))
    conn.commit()

    id += 1
print('characters ready')

print('load successful')