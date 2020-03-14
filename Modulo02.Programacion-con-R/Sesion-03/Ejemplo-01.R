if (!require("pacman"))
  install.packages("pacman")
pacman::p_load(tidyverse)

str(mtcars)
class(mtcars)

mtcars2 <- mtcars

mtcars2$vs = as.logical(mtcars2$vs)
mtcars2$am = as.logical(mtcars2$am)
class(mtcars2$vs)
class(mtcars2$am)

mtcars2.new <- transform(mtcars2, wt = wt * 1000 / 2.2046)

summary(mtcars)
summary(mtcars2)