(nrow(mtcars))
(ncol(mtcars))
(colnames(mtcars))
mtcars[5,3]
mtcars[,4:5]
modified.metcars <- mtcars
colnames(modified.metcars) <- c("modelo",
                                "mpg",
                                "disp",
                                "hp",
                                "drat",
                                "wt",
                                "qsec",
                                "vs",
                                "am",
                                "gear",
                                "carb")
modified.metcars[,2] <- NULL
modified.metcars
