#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#
# Written by Ryan Dunton on March 25th, 2016

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    query1 = "UPDATE swiss_tournament.participants SET wins = 0"
    query2 = "UPDATE swiss_tournament.participants SET matches = 0"
    cur.execute(query1)
    cur.execute(query2)
    DB.commit()
    data = cur.fetchall
    DB.close()
    return data


def deletePlayers():
    """Remove all the player records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    # Delete all data from the participants table
    query1 = "DELETE FROM swiss_tournament.participants"
    cur.execute(query1)
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    # Finds the number of players in the participants table
    query1 = "SELECT * FROM swiss_tournament.participants"
    cur.execute(query1)
    data = cur.rowcount
    DB.close()
    return data


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
     name: the player's full name (need not be unique).
     """
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    # Adds a player into the participants table starting with 0 wins, 0 losses
    query1 = '''INSERT INTO swiss_tournament.participants (full_name, wins, matches)
                VALUES (%s, %s, %s)'''
    param = (name, 0, 0)
    cur.execute(query1, param)
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    cur.execute("SELECT * FROM swiss_tournament.participants ORDER BY wins")
    # Returns all results from the participants table
    rows = cur.fetchall()
    DB.close()
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    # Defines queries to add matches to both players and a win to the winner
    query1 = '''UPDATE swiss_tournament.participants SET matches = matches + 1
                WHERE %s = id'''
    param1 = (winner,)
    query2 = '''UPDATE swiss_tournament.participants SET matches = matches + 1
                WHERE %s = id'''
    param2 = (loser,)
    query3 = '''UPDATE swiss_tournament.participants SET wins = wins + 1
                WHERE %s = id'''
    param3 = (winner,)
    # Executes queries with paramenters
    cur.execute(query1, param1)
    cur.execute(query2, param2)
    cur.execute(query3, param3)
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    query = cur.execute('''SELECT id, full_name
                        FROM swiss_tournament.participants ORDER BY wins''')
    # Change query results to a list
    data = list(cur.fetchall())
    i = 0
    while i < len(data):
        # Combine every two rows of results and deleting already merged data
        data[i] = data[i] + data[i+1]
        data.remove(data[i+1])
        i += 1

    DB.close()
    return data
