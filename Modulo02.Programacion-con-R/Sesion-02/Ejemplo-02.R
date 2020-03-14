df.example <- data.frame(clave = seq(1:10),
                         grado = seq(1:10),
                         sexo = c('F','M','M','F','M','M','F','M','M','M'))
df.example
str(df.example)
str(iris)
dim(iris)
ncol(iris)
nrow(iris)

paste("El numero de columnas de nuestro DF es de ", ncol(iris), sep = " ")

wl_name <- names(iris)
class(wl_name)

View(iris[1,1])
View(iris[1,])
View(iris[1:3,])
View(iris[-1,])

iris[,'Sepal.Length']
iris$Sepal.Length

iris[,1:2]
iris[1:3,2:3]