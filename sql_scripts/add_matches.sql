INSERT INTO api_server_country (name) VALUES (
   'Międzynarodowy'
);

INSERT INTO api_server_league (name, country_of_origin_id) VALUES (
   'FIFA U20 World Cup',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Międzynarodowy'
   )
);

INSERT INTO api_server_leagueseason (name, league_id) VALUES (
   '1979',
   (
       SELECT league.id FROM api_server_league AS league
       WHERE league.name = 'FIFA U20 World Cup'
   )
);

INSERT INTO api_server_match (game_date, league_season_id) VALUES (
   '1979-09-07',
   (
       SELECT season.id FROM api_server_leagueseason AS season
       WHERE season.name = '1979' AND
       season.league_id = (
           SELECT l.id FROM api_server_league AS l WHERE l.name = 'FIFA U20 World Cup'
       )
   )
);

INSERT INTO api_server_country (name) VALUES (
   'Rosja'
);

INSERT INTO api_server_team (name, country_of_origin_id) VALUES (
   'Związek Radziecki U20',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Rosja'
   )
);

INSERT INTO api_server_country (name) VALUES (
   'Argentyna'
);

INSERT INTO api_server_team (name, country_of_origin_id) VALUES (
   'Argentyna U20',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);

INSERT INTO api_server_country (name) VALUES (
   'Ukraina'
);

INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Viktor',
   'Chanov',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Ukraina'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Viktor' AND
       player.surname = 'Chanov'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Viktor',
   'Yanushevskiy',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Rosja'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Viktor' AND
       player.surname = 'Yanushevskiy'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   61.4
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Aleksandr',
   'Polukarov',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Rosja'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Aleksandr' AND
       player.surname = 'Polukarov'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Sergiy',
   'Ovchinnikov',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Ukraina'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Sergiy' AND
       player.surname = 'Ovchinnikov'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   90.0
);
INSERT INTO api_server_country (name) VALUES (
   'Armenia'
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Ashot',
   'Khachatryan',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Armenia'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Ashot' AND
       player.surname = 'Khachatryan'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Yaroslav',
   'Dumanskiy',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Ukraina'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Yaroslav' AND
       player.surname = 'Dumanskiy'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   65.38333333333334
);
INSERT INTO api_server_country (name) VALUES (
   'Azerbejdżan'
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Igor',
   'Ponomarev',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Azerbejdżan'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Igor' AND
       player.surname = 'Ponomarev'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Anatoliy',
   'Radenko',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Ukraina'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Anatoliy' AND
       player.surname = 'Radenko'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Oleg',
   'Taran',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Ukraina'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Oleg' AND
       player.surname = 'Taran'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   90.0
);
INSERT INTO api_server_country (name) VALUES (
   'Białoruś'
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Igor',
   'Gurinovich',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Białoruś'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Igor' AND
       player.surname = 'Gurinovich'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Sergey',
   'Stukashov',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Rosja'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Sergey' AND
       player.surname = 'Stukashov'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Sergiy',
   'Krakovskyi',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Ukraina'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Sergiy' AND
       player.surname = 'Krakovskyi'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   0.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Aleksandr',
   'Golovnya',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Białoruś'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Aleksandr' AND
       player.surname = 'Golovnya'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   0.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Gennadiy',
   'Salov',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Rosja'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Gennadiy' AND
       player.surname = 'Salov'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   0.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Mykhaylo',
   'Olefirenko',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Ukraina'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Mykhaylo' AND
       player.surname = 'Olefirenko'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   28.6
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Vladimir',
   'Mikhalevsky',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Azerbejdżan'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Vladimir' AND
       player.surname = 'Mikhalevsky'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   24.61666666666666
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Oleksandr',
   'Zavarov',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Ukraina'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Oleksandr' AND
       player.surname = 'Zavarov'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   0.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Valeri',
   'Zubenko',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Ukraina'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Valeri' AND
       player.surname = 'Zubenko'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Związek Radziecki U20'
   ),
   0.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Diego Armando',
   'Maradona',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Diego Armando' AND
       player.surname = 'Maradona'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Juan Ernesto',
   'Simón',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Juan Ernesto' AND
       player.surname = 'Simón'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Gabriel Humberto',
   'Calderón',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Gabriel Humberto' AND
       player.surname = 'Calderón'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Osvaldo Salvador',
   'Escudero',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Osvaldo Salvador' AND
       player.surname = 'Escudero'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   54.666666666666664
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Ramón Ángel',
   'Díaz',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Ramón Ángel' AND
       player.surname = 'Díaz'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Sergio Rubén',
   'García',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Sergio Rubén' AND
       player.surname = 'García'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Hugo',
   'Alvez',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Hugo' AND
       player.surname = 'Alvez'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Abelardo',
   'Carabelli',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Abelardo' AND
       player.surname = 'Carabelli'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Rubén',
   'Rossi',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Rubén' AND
       player.surname = 'Rossi'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Osvaldo',
   'Rinaldi',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Osvaldo' AND
       player.surname = 'Rinaldi'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   54.516666666666666
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Juan Alberto Barbas',
   'Martínez',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Juan Alberto Barbas' AND
       player.surname = 'Martínez'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   90.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Rafael',
   'Seria',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Rafael' AND
       player.surname = 'Seria'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   0.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Jorge',
   'Piaggio',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Jorge' AND
       player.surname = 'Piaggio'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   0.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Marcelo',
   'Bachino',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Marcelo' AND
       player.surname = 'Bachino'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   0.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Daniel Adolfo',
   'Sperandío',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Daniel Adolfo' AND
       player.surname = 'Sperandío'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   0.0
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Juan José',
   'Meza',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Juan José' AND
       player.surname = 'Meza'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   35.483333333333334
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'Alfredo',
   'Torres',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'Alfredo' AND
       player.surname = 'Torres'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   35.333333333333336
);
INSERT INTO api_server_player (name, surname, country_of_origin_id) VALUES (
   'José Luis Lanao',
   'Landolfi',
   (
       SELECT country.id FROM api_server_country AS country
       WHERE country.name = 'Argentyna'
   )
);
INSERT INTO api_server_playerinmatch (player_id, match_id, team_id, minutes_played) VALUES (
   (
       SELECT player.id FROM api_server_player AS player
       WHERE player.name = 'José Luis Lanao' AND
       player.surname = 'Landolfi'
   )
   ,2,
   (
       SELECT team.id FROM api_server_team AS team
       WHERE team.name = 'Argentyna U20'
   ),
   0.0
);

INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.983333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.983333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.083333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.016666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.383333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.65,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.366666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.516666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.4,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   29.183333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   33.31666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   35.266666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   35.733333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.18333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   38.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   46.86666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   47.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   50.4,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   58.21666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   60.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   62.2,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   62.31666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   65.61666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.63333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   70.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   74.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   77.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Chanov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.933333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   6.316666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   6.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.516666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   9.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   9.733333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   10.133333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.833333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.533333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   24.4,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.466666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.683333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   29.4,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   33.93333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.36666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.483333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   35.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.65,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   38.28333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.4,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.81666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.166666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   52.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   54.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   58.416666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Viktor Yanushevskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.683333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   10.616666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.116666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.866666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.883333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.216666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.25,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.833333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.916666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   22.966666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   24.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   28.066666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   30.166666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   33.4,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   33.68333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   35.833333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   35.983333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.516666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.416666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   38.483333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   47.03333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.28333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   53.43333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   56.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   57.43333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   57.78333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   58.88333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.63333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   61.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.56666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   70.96666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   77.23333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.13333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   82.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   82.73333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Aleksandr Polukarov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.2,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.566666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.183333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.316666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.433333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   35.78333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.36666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   38.68333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   46.61666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   46.71666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   47.78333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.06666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   52.233333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   58.61666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   62.38333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.61666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.2,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   67.36666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   67.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.51666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   70.83333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   71.46666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.4,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   77.63333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.18333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergiy Ovchinnikov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.683333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   9.833333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   10.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.933333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   16.466666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.383333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   20.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   22.933333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   30.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.81666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   35.166666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   35.38333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.833333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   46.43333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   47.21666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   52.61666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   56.21666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   62.233333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   62.766666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.53333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.36666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   68.4,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   77.08333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.06666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ashot Khachatryan'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.8833333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.25,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.733333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   6.016666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.433333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.466666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   10.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.566666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.166666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.216666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   16.516666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.833333333333332,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.983333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.966666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   22.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.716666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   26.516666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   26.716666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   29.533333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   29.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   30.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   31.733333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.266666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.56666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   33.766666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.43333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.266666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.916666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   38.88333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   39.71666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.53333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   47.25,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   50.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.2,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   52.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   52.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   54.733333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   55.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   55.36666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.583333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   62.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   62.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.06666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.68333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Yaroslav Dumanskiy'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.9166666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.7666666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   10.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.383333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.716666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.433333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.766666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.4,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.983333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   26.766666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.616666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.38333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   38.833333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   47.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.083333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.733333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   52.266666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   53.483333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   54.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   56.53333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Zdobycie gola'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.56666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   68.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   70.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   71.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   74.63333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   76.21666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.01666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.43333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   79.73333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   81.53333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   82.66666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Ponomarev'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.0833333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   6.633333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   9.166666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.466666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   20.033333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   20.783333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   30.216666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   30.333333333333332,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   38.78333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   50.65,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   53.56666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   54.666666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.166666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   67.68333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.16666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   72.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   74.46666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   76.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   77.83333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.53333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   79.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   79.83333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.18333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.33333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Anatoliy Radenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.1166666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.966666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   6.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.583333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   10.083333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   10.583333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Rzut rożny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.516666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.666666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.516666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   30.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   30.65,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   33.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.06666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.833333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   52.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   56.36666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   56.516666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   58.38333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   68.56666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.21666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   74.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   76.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   79.81666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.28333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.88333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Oleg Taran'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.3333333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.016666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.616666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   23.033333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   23.183333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   30.466666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.333333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.416666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   53.583333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.68333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.33333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.38333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   72.61666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   76.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   81.51666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.28333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Igor Gurinovich'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.016666666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.8666666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.233333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   23.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   26.583333333333332,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.566666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   29.466666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   46.93333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   56.28333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.61666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   62.43333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   76.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.11666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergey Stukashov'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.46666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Mykhaylo Olefirenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.56666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Mykhaylo Olefirenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   76.73333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Mykhaylo Olefirenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.13333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Mykhaylo Olefirenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.41666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Mykhaylo Olefirenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.76666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Rzut rożny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Mykhaylo Olefirenko'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   68.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Vladimir Mikhalevsky'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   71.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Vladimir Mikhalevsky'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   72.63333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Vladimir Mikhalevsky'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   76.18333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Vladimir Mikhalevsky'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   76.78333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Vladimir Mikhalevsky'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   77.53333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Vladimir Mikhalevsky'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   77.93333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Vladimir Mikhalevsky'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.31666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Vladimir Mikhalevsky'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   82.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Vladimir Mikhalevsky'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.6833333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.5666666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.483333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.683333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.716666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   9.433333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.583333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.616666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.233333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.25,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.916666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   24.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   24.733333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Rzut rożny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.083333333333332,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   29.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.733333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.86666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.56666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.733333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   49.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   54.11666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   56.06666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   57.28333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   58.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.766666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.81666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   61.11666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   62.766666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.56666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.71666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   68.38333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   74.16666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   80.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Zdobycie gola'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.01666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.06666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.11666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Diego Armando Maradona'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.38333333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.5333333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.216666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.833333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.033333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   10.783333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.866666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   16.566666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.033333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   20.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.566666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   28.266666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   31.766666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.96666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   38.416666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   47.68333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.71666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.88333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   52.166666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   52.65,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   53.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   60.65,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.21666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   67.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   68.88333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.31666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   70.51666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   76.36666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   79.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   81.61666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   81.66666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   82.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.28333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.41666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.43333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Ernesto Simón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.2,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.3833333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.233333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.116666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.383333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.65,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   16.933333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   22.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   22.283333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   23.883333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   23.916666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   24.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.133333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   28.416666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   29.983333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   31.383333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   31.416666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.61666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   38.18333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   39.43333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   46.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.25,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   49.28333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.06666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.11666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   55.233333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   55.71666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   56.13333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   57.71666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   58.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.86666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   61.68333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Rzut rożny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   61.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   67.91666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   70.08333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   74.01666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.63333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   79.01666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   81.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.18333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.71666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.03333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Gabriel Humberto Calderón'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.43333333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.033333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.5666666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.866666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.916666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.316666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.25,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.783333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.866666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.266666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.566666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.733333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.616666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.766666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.283333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.133333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.2,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.733333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   22.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   22.783333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Rzut rożny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   23.783333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   30.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   31.416666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.71666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   49.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Rzut rożny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   53.81666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   53.88333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Salvador Escudero'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.0333333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.5833333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.716666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.583333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.416666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.616666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.566666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.283333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   22.933333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   24.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   24.666666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.183333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   29.033333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   33.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.81666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.833333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   38.21666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   57.25,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   57.983333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał niecelny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   67.36666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   70.66666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   71.2,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.91666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   75.08333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Zdobycie gola'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.08333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Ramón Ángel Díaz'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.3333333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.4,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.866666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   10.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.216666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.516666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.566666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   20.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   23.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   31.233333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   31.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   39.233333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.71666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.766666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.96666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   53.65,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   55.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   55.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   68.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   79.41666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   82.98333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Sergio Rubén García'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.7833333333333332,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.0166666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.066666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.466666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.716666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.433333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.483333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   6.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   6.966666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.166666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   9.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   9.416666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   9.933333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.666666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.783333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.716666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   16.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   16.416666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   16.883333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.033333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.383333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   20.416666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   20.7,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   20.833333333333332,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.216666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   22.166666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   22.833333333333332,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   24.616666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   26.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   30.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   31.883333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.483333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.166666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.583333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.61666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   38.11666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.96666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   46.233333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   46.416666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   47.28333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   47.483333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   47.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   49.25,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   49.516666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.43333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.65,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   54.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   58.46666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   61.43333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   61.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.81666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   65.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.03333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.11666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   72.11666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Zdobycie gola'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.11666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   74.78333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.68333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Hugo Alvez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.6666666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.833333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.216666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.533333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   10.833333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.566666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.883333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   23.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   24.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   24.283333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.033333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.833333333333332,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   26.333333333333332,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   26.633333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.866666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   28.216666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   29.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   31.266666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   33.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.06666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.11666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   52.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   52.766666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   53.25,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   55.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   55.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   57.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   57.666666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   57.916666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   60.766666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.666666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.28333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.53333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   67.58333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   68.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.28333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   71.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   72.81666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   72.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   77.48333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   77.58333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   79.06666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   81.73333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   81.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.91666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   84.91666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Abelardo Carabelli'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.65,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.166666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.283333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.533333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.633333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   10.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.466666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.733333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.683333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   23.733333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   27.083333333333332,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   28.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   30.25,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   30.666666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   31.933333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   33.88333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   35.416666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   38.03333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   47.53333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   47.983333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.93333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.86666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   56.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   62.583333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   65.66666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.61666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   67.88333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   68.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.86666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   79.18333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.36666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Rubén Rossi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   0.2833333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.4333333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.4166666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.2333333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.6833333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.166666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.383333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   5.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.216666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.383333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.933333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   9.366666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   9.966666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   10.866666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.816666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.633333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   12.783333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.533333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   14.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.183333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   16.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   16.916666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.066666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.916666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.316666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.183333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.233333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   20.633333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.666666666666668,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   26.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   26.966666666666665,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   31.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.233333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.61666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   34.666666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   36.68333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.2,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   39.28333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   46.266666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.05,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   49.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.583333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   51.666666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   54.06666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Osvaldo Rinaldi'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   1.5,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   2.3833333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.5166666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   3.5833333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.366666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   4.433333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   7.983333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.183333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   8.316666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.866666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   11.883333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   13.483333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.216666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   15.666666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   17.133333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   18.266666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.1,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   19.266666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   20.866666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.133333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   21.783333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.866666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   25.983333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   26.066666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   26.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   26.683333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   28.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   28.183333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   29.0,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   29.533333333333335,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Obrona'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   29.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   31.333333333333332,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.166666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.516666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.68333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   32.983333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   33.083333333333336,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.81666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   37.983333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   39.666666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   45.666666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   46.61666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.016666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   48.25,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   53.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   55.2,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   55.266666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   58.88333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Rzut rożny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   61.06666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   62.86666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.75,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.35,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.53333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Rzut rożny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.91666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   67.21666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   67.48333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Rzut rożny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   68.01666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   70.58333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   71.16666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   71.45,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Rzut rożny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   72.9,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.65,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   74.06666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   74.91666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   76.96666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   81.71666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   81.83333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   82.31666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.06666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan Alberto Barbas Martínez'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   55.666666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   60.88333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.4,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.516666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.65,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.11666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.41666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   68.93333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   71.03333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.18333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.8,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   74.83333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   78.88333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   79.11666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   79.91666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   81.63333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   82.33333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.13333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.21666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.43333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   83.61666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Juan José Meza'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   55.766666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   57.38333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   57.56666666666667,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.78333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   59.93333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   61.15,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.416666666666664,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   63.63333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   64.98333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Strzał celny'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   66.43333333333334,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   67.11666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   67.3,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   69.06666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.25,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   73.85,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   74.08333333333333,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   74.95,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   76.6,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   77.06666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   79.55,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie nieskuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   80.11666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
INSERT INTO api_server_matchevent (occurrence_minute, event_type_id, player_id, match_id) VALUES (
   81.86666666666666,
   (
       SELECT id FROM api_server_eventtype
       WHERE name = 'Podanie skuteczne'
   ),
   (
       SELECT id FROM api_server_player
       WHERE name || ' ' || surname = 'Alfredo Torres'
   ),
   2
);
