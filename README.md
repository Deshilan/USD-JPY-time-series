# What's this all about?
<h3>This repository is part of my project classes at AGH (Time-series course). 
My goal is to find and analise (as much as i can) some time series record. I choose USD-JPY currency pair. Why? Because i'm really interested in stock market (also trading). <h3>

## What's already done?

+ **Price variation in different minutes of the day**

This one might be obvious, but as we can see: biggest changes are at opening of markets. Our data is from +5:30 UTC, so it's respectively: Asia (~210), and USA (1440/1500). 

+ **New dataset, which consists of hour data**

For long term analysis, it's not necessary to use one minute data; it might be difficult to train models. Also, one hour data has few other advanteges, which i will describe in next points.
Data for every hour are from last minute of this hour (for example: for 17:00 it's from 17:59). 

+ **Holt Model**

 Rather useless; I tried this just to understand how it works. Also, it might be used in some cases, like find some long term trend. 

+ **ARIMA Model** 

Probably most important thing in this whole project. Not because of results, portion of coding (honestly- it's few lines with dedicated functions), but rather due to gained knowledge. 
First of all: number of satisfying results in short term prediction is bigger than i thought it would be. Of course, prediction is not really accurate, but it shows trend AND in some cases trend reversal. Why? Because in some periods values are jumping
from one point to another. Values at which trend will change aren't specific, but in many cases model predicts change in near future (due to coming to last breaking value for example). It doesn't mean that you can trade just by knowing those values, but
it might be helpful to make decision. 

+ **New data: interest rates**
My next thought was: "What makes me better than model?" and quickly find out: full perspective! Before any investment, I'm not only checking the price, but also IR in countries, GDP, inflation and many other parameters. Of course, in this case i can't give model
all of it: collecting whole knowledge, month by month would take a lot of time. But i found out something: in this case IR would be kinda simple! In both countries decisions are regular and not so often bring changes. I decided to add them to dataset by simple script.
I tried to place them properly in hour dataset, but it's really difficult to find information about hours of IR publication.

+ ** SARIMAX test version **
It's first model i decided to try with IR data. Unfortunately, it doesn't work like i supposed it will. Probably problems are about unconsistency of data: by most of the time, IRs are stable. My biggest advantage became my greatest enemy. Also, it's possible that i didn't
configure model properly. 
