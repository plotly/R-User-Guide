Plotly in Shiny
========================================================

Shiny is an R package to create web applications with your data. If you have never used it before you should read RStudio’s tutorial here: http://shiny.rstudio.com/

We will start with a basic example of Plotly in Shiny using group checkbox, and ggplot’s iris dataset.


```r
summary(iris)
```

```
##   Sepal.Length   Sepal.Width    Petal.Length   Petal.Width 
##  Min.   :4.30   Min.   :2.00   Min.   :1.00   Min.   :0.1  
##  1st Qu.:5.10   1st Qu.:2.80   1st Qu.:1.60   1st Qu.:0.3  
##  Median :5.80   Median :3.00   Median :4.35   Median :1.3  
##  Mean   :5.84   Mean   :3.06   Mean   :3.76   Mean   :1.2  
##  3rd Qu.:6.40   3rd Qu.:3.30   3rd Qu.:5.10   3rd Qu.:1.8  
##  Max.   :7.90   Max.   :4.40   Max.   :6.90   Max.   :2.5  
##        Species  
##  setosa    :50  
##  versicolor:50  
##  virginica :50  
##                 
##                 
## 
```

Our ui.R file:


```r
library(shiny) 

shinyUI(
  pageWithSidebar(
    
    headerPanel(title=HTML("Plotly in Shiny"), windowTitle="Plotly in Shiny"),
    
    sidebarPanel(
      checkboxGroupInput(inputId="check_group",  # ID to be used in server.R
                         label="Select species:",
                         choices=list("Setosa"="setosa",  # Make sure not to mix names with values
                                      "Versicolor"="versicolor",
                                      "Virginica"="virginica"),
                         selected=list("setosa", "versicolor", "virginica"))
      ),
    
    mainPanel(
      htmlOutput("plot")  # Argument name from server.R
      )
    ))
```

Remember to add commas after sidebarPanel() and headerPanel(). 
For more information on checkboxGroupInput() click here: http://shiny.rstudio.com/reference/shiny/latest/checkboxGroupInput.html

Our server.R:


```r
library(shiny) # Load libraries we will be using
library(plotly)

shinyServer(function(input, output) {
  
  output$plot <- renderUI({  # "main" to be used as argument in server.R

    subset_iris <- iris[iris$Species %in% input$check_group, ]  # Subset dataset
    
    ggiris <- qplot(x=Petal.Width, y=Sepal.Length, data=subset_iris, color=Species)

    py <- plotly(username="r_user_guide", key="mw5isa4yqp")  # Open Plotly connection
    
    res <- py$ggplotly(ggiris, kwargs=list(filename="Plotly in Shiny", 
                                           fileopt="overwrite", # Overwrite plot in Plotly's website
                                           auto_open=FALSE))

    tags$iframe(src=res$response$url,
                  frameBorder="0",  # Some aesthetics
                  height=400,
                  width=650)
 
  })
})
```

For more information on tags$iframe() click here: http://shiny.rstudio.com/articles/tag-glossary.html

Then after you make sure ui.R and server.R are in the same folder (and working directory), run on your console:


```r
runApp()
```

And voilà, a Shiny app using Plotly!

<iframe src="http://plotly.shinyapps.io/plotly_in_shiny/" width="1000" height="500" frameBorder="0"></iframe>
