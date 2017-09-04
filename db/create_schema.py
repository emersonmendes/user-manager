import sqlite3

conn = sqlite3.connect('user-manager.db')

cursor = conn.cursor()

cursor.execute("""
    create table usergroup (
        id integer not null primary key autoincrement,
        name varchar not null
    );
""")

cursor.execute("""
    create table user (
        id integer not null primary key autoincrement,
        name varchar not null,
        username varchar not null,
        password varchar not null,
        fk_usergroup integer,
        foreign key (fk_usergroup) references usergroup(id)
    );
""")

print('Tabelas criadas com sucesso.')

conn.close()