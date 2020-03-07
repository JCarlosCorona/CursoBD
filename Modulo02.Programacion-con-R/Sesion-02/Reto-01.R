mi.vector <- seq(0,500,10)
mi.vector.length <- length(mi.vector)
mi.vector[mi.vector.length] <- -1
mi.vector.transformado <- (mi.vector*0.85 + 10)
(mi.vector.transformado <- sort(mi.vector.transformado,decreasing = T))
