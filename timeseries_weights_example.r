library(ggplot2)
library(plyr)
require(maps)
library(tidyverse)
library(ggthemes)
library(haven)
library(scales)
library(ggpubr)
library(ggalt)
library(zoo)

#import data 
df <- read.csv("year_topic_weights2.csv",
               header = TRUE)
df2 <- df[df$topic_label=="Domestic politics" | df$topic_label=="Diplomacy and trade" | df$topic_label=="Economy"
          | df$topic_label=="Nationalism" | df$topic_label=="Military/Defense", ]
df3 <- df[df$topic_label=="Oil and energy" | df$topic_label=="Regional politics" | df$topic_label=="Crime and punishment"
          | df$topic_label=="Sport and culture" | df$topic_label=="Human development", ]

#find median topic weight
median(df$average_weight)
#.08


#plot
plot1 <- ggplot(df2, aes(x = year, y = average_weight, colour = topic_label)) +
  geom_smooth() +
  geom_hline(yintercept = 0.08, size = 1, colour="#333333") +
  labs(title = "Putin Corpus Top-5 Topic Presence (1999 - 2020)",
       subtitle = "Black line represents median topic weight through time") +
  xlab("Date") + ylab("Average Yearly Topic Weight") + 
  theme_hc()

plot1

plot2 <- ggplot(df3, aes(x = year, y = average_weight, colour = topic_label)) +
  geom_smooth() +
  geom_hline(yintercept = 0.08, size = 1, colour="#333333") +
  labs(title = "Putin Corpus Bottom-5 Topic Presence (1999 - 2020)",
       subtitle = "Black line represents median topic weight through time") +
  xlab("Date") + ylab("Average Yearly Topic Weight") + 
  theme_hc()

plot2



