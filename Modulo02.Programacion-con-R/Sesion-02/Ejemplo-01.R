integro <- as.integer(1)
numerico <- "3242342"
logico <- FALSE
texto <- "texto"

numerico <- as.numeric(numerico)

typeof(integro)
is.integer(integro)
is.numeric(numerico)
is.logical(logico)


xm <- matrix(1:9 , byrow = T, nrow = 3)


prework <- c(100/4,108/5,200/20,sqrt(81),3*5)
summary(prework)


# Para crear un vector con secuencia
vector.seq.byone <- seq(from=1, to=10, by=1)
print(vector.seq.byone)

vector.seq.bytwo <- seq(from=1, to = 10, by=2)
print(vector.seq.bytwo)

vector.seq.negative <- seq(from = 10, to = 1, by=-1)
print(vector.seq.negative)


# Para crear un vector con valores repetidos
vector.rep <- rep(x=1, times = 3)
print(vector.rep)

vector.rep.each <- rep(x = c(1,2), each = 3)
print(vector.rep.each)

vector.rep.complete <- rep(x=c(1,2), each = 3, times = 2)
print(vector.rep.complete)

e <- seq(1:20)

e[1] <- 100
e

print(vector.new) <-  seq(0,25,5)
options(scipen = 100)
vector.new * 100000000000000000000000000000000