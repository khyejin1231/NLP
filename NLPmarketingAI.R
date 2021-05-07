#install.packages("bibliometrix")
library(bibliometrix)

M <- convert2df(file = "scopus.bib",dbsource = "scopus", format = "bibtex")
results <- biblioAnalysis(M, sep = ";")
options(width = 100)
S <- summary(object = results, k = 10, pause = FALSE)
plot(x = results, k = 10, pause = FALSE)

