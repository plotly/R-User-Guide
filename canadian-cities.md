See the source code and more examples here: https://github.com/plotly/knitr-demos


```r
library(plotly)
```

```
## Loading required package: RCurl
## Loading required package: bitops
## Loading required package: RJSONIO
```

```r
p = plotly("R-demos", "p9g4f35ytd")
```



```r
# Load maps
library(maps)
```

```
## Warning: package 'maps' was built under R version 3.0.2
```

```r
data(canada.cities)

# Create the hexagone map
trace1 <- list(x = map(regions = "canada", plot = FALSE)$x, y = map(regions = "canada", 
    plot = FALSE)$y)

# Create the plotable city data
trace2 <- list(x = canada.cities$long, y = canada.cities$lat, text = canada.cities$name, 
    type = "scatter", mode = "markers", marker = list(size = sqrt(canada.cities$pop/max(canada.cities$pop)) * 
        100, opacity = 0.5))
```



```r
p$iplot(trace1, trace2, kwargs = list(filename = "canadian cities"))
```

<iframe height="600" id="igraph" scrolling="no" seamless="seamless"
				src="https://plot.ly/~R-demos/4" width="600"></iframe>



```r
p$embed("https://plot.ly/~ChrisP/9/600/600")
```

<iframe height="600" id="igraph" scrolling="no" seamless="seamless"
				src="https://plot.ly/~ChrisP/9/600/600" width="600"></iframe>


