![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | AB-Testing

![cats](images/cats.jpeg)


## Introduction

Imaginad que somos los científicos de datos de la empresa de videojuegos Tactile Entertainment. 

Los desarrolladores del juego Cookie Cats pretenden introducir un cambio en el juego para aumentar la retencion de los jugadores. En cierto nivel del juego los jugadores se encuentran una puerta que les obliga a esperar o a pagar la app. 

Actualmente la puerta se encuentra en nivel 30 y se pretende pasar al nivel 40, para comprobar la retencion a 1 y 7 dias. Antes de realizar el cambio definitivo en el juego se raliza un test AB.

## Data description

+ **UserID**: A unique number that identifies each player.
+ **Version**: Whether the player was put in the control group (gate_30 - a gate at level 30) or the group with the moved gate (gate_40 - a gate at level 40).
+ **sum_gamerounds**: The number of game rounds played by the player during the first 14 days after install.
+ **retention_1**: Did the player come back and play 1 day after installing?
+ **retention_7**: Did the player come back and play 7 days after installing?


## Getting Started

Los datos estan alojados en `data/cookie_cats.csv`. Nuestro grupo de control sera la version actual `gate_30` y el grupo de tratamiento sera la version `gate_40`. Debemos realizar el test para 1 dia de retencion `retention_1` y para 7 dias `retention_7`. 

## Deliverables

* Jupyter Notebook with AB testing.
