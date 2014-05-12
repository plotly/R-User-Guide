Bar Charts
========================================================
(See the source code and more examples here: https://github.com/plotly/knitr-demos)

In `ggplot2`, you plot bar charts using `geom_bar` plus `stat_identity`.


```r
library(ggplot2)
library(plotly)
library(devtools)
```

```
## 
## Attaching package: 'devtools'
## 
## The following objects are masked from 'package:utils':
## 
##     ?, help
## 
## The following object is masked from 'package:base':
## 
##     system.file
```

```r
install_github("ropensci/plotly")
```

```
## Installing github repo plotly/master from ropensci
## Downloading master.zip from https://github.com/ropensci/plotly/archive/master.zip
## Installing package from /tmp/RtmpG0q1r8/master.zip
## arguments 'minimized' and 'invisible' are for Windows only
## Installing plotly
## '/usr/lib/R/bin/R' --vanilla CMD INSTALL  \
##   '/tmp/RtmpG0q1r8/devtools6ea031063046/plotly-master'  \
##   --library='/home/marianne/R/x86_64-pc-linux-gnu-library/3.1'  \
##   --install-tests 
## 
## Reloading installed plotly
```

```r
# Initialize a plotly object to sign in to your Plotly API account
py <- plotly("R-demos", "p9g4f35ytd")
```


Basic Bar Chart
===


```r
# Consider the following data frame
researchers <- data.frame(country = c("Canada", "Canada", "Germany", "USA"), 
    name = c("Warren", "Andreanne", "Stefan", "Toby"), papers = c(23, 14, 37, 
        20), field = c("Math", "Bio", "Bio", "Math"))

# Let us plot the number of papers (y) per name (x)
gg.basic <- ggplot(researchers, aes(x = name, y = papers)) + geom_bar(stat = "identity")
```


In R your plot looks like this:


```r
print(gg.basic)
```

![plot of chunk unnamed-chunk-3](figure/unnamed-chunk-3.png) 


Now send it to Plotly!


```r
py$ggplotly(gg.basic)
```

<iframe height="600" id="igraph" scrolling="no" seamless="seamless"
				src="https://plot.ly/~R-demos/25" width="600" frameBorder="0"></iframe>


Grouped Bar Chart
===


```r
# Let us plot the number of papers (y) per country (x) splitting by field
gg.dodge <- ggplot(researchers, aes(x = country, y = papers, fill = field)) + 
    geom_bar(stat = "identity", position = "dodge")
```


In R your plot looks like this:


```r
print(gg.dodge)
```

![plot of chunk unnamed-chunk-6](figure/unnamed-chunk-6.png) 


Send it to Plotly!


```r
py$ggplotly(gg.dodge)
```

<iframe height="600" id="igraph" scrolling="no" seamless="seamless"
				src="https://plot.ly/~R-demos/26" width="600" frameBorder="0"></iframe>


Oh, the default colors are different.  Let us change the colors the way we like using Plotly's UI.  Say we are happy with the following:


```r
py$embed("https://plot.ly/~R-demos/11/papers-vs-country/")
```

<iframe height="600" id="igraph" scrolling="no" seamless="seamless"
				src="https://plot.ly/~R-demos/11/papers-vs-country/" width="600" frameBorder="0"></iframe>


Stacked Bar Chart
===


```r
# Let us plot the same thing but with a different layout (barmode='stack')
gg.stack <- ggplot(researchers, aes(x = country, y = papers, fill = field)) + 
    geom_bar(stat = "identity", position = "stack")
```


In R your plot looks like this:


```r
print(gg.stack)
```

![plot of chunk unnamed-chunk-10](figure/unnamed-chunk-10.png) 


Send it to Plotly!


```r
py$ggplotly(gg.stack)
```

<iframe height="600" id="igraph" scrolling="no" seamless="seamless"
				src="https://plot.ly/~R-demos/27" width="600" frameBorder="0"></iframe>


Overlaid Bar Chart
===


```r
# Let us plot the same thing but with a different layout (barmode='overlay')
gg.identity <- ggplot(researchers, aes(x = country, y = papers, fill = field)) + 
    geom_bar(stat = "identity", position = "identity")
```


In R your plot looks like this:


```r
print(gg.identity)
```

![plot of chunk unnamed-chunk-13](figure/unnamed-chunk-13.png) 


Send it to Plotly!


```r
py$ggplotly(gg.identity)
```

<iframe height="600" id="igraph" scrolling="no" seamless="seamless"
				src="https://plot.ly/~R-demos/28" width="600" frameBorder="0"></iframe>


You need to hover over the 'Canada' bar to see the info for 'Bio' (i.e., 14), which lies underneath.
