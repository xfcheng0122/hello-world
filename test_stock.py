import requests

base_url = 'https://api.iextrading.com/1.0'
res = {'quote': {'symbol': 'AAPL', 'companyName': 'Apple Inc.', 'primaryExchange': 'Nasdaq Global Select', 'sector': 'Technology', 'calculationPrice': 'close', 'open': 219.66, 'openTime': 1540215000651, 'close': 220.65, 'closeTime': 1540238400188, 'high': 223.36, 'low': 218.94, 'latestPrice': 220.65, 'latestSource': 'Close', 'latestTime': 'October 22, 2018', 'latestUpdate': 1540238400188, 'latestVolume': 28576651, 'iexRealtimePrice': 220.61, 'iexRealtimeSize': 100, 'iexLastUpdated': 1540238399824, 'delayedPrice': 220.59, 'delayedPriceTime': 1540238400242, 'extendedPrice': 220.65, 'extendedChange': 0, 'extendedChangePercent': 0, 'extendedPriceTime': 1540241992052, 'previousClose': 219.31, 'change': 1.34, 'changePercent': 0.00611, 'iexMarketPercent': 0.0427, 'iexVolume': 1220223, 'avgTotalVolume': 34317785, 'iexBidPrice': 0, 'iexBidSize': 0, 'iexAskPrice': 0, 'iexAskSize': 0, 'marketCap': 1065723171900, 'peRatio': 20, 'week52High': 233.47, 'week52Low': 150.24, 'ytdChange': 0.30173277383646435}, 'news': [{'datetime': '2018-10-22T20:35:34-04:00', 'headline': 'Could Apple Really Hit $310 In 2019?', 'source': 'SeekingAlpha', 'url': 'https://api.iextrading.com/1.0/stock/aapl/article/7212636922090000', 'summary': '   Apple (AAPL) is far and away my largest holding, making up nearly 10% of my portfolio, so Im always happy when I see a positive analyst note. For some reason or another, the market typically moves on these notes. When doing my daily due diligence last week, I came across a  note  put o…', 'related': 'AAPL,Computer Hardware,CON31167138,NASDAQ01,Computing and Information Technology', 'image': 'https://api.iextrading.com/1.0/stock/aapl/news-image/7212636922090000'}], 'chart': [{'date': '2018-09-24', 'open': 216.82, 'high': 221.26, 'low': 216.63, 'close': 220.79, 'volume': 27693358, 'unadjustedVolume': 27693358, 'change': 3.13, 'changePercent': 1.438, 'vwap': 219.4487, 'label': 'Sep 24', 'changeOverTime': 0}, {'date': '2018-09-25', 'open': 219.75, 'high': 222.82, 'low': 219.7, 'close': 222.19, 'volume': 24554379, 'unadjustedVolume': 24554379, 'change': 1.4, 'changePercent': 0.634, 'vwap': 221.6295, 'label': 'Sep 25', 'changeOverTime': 0.0063408668870873035}, {'date': '2018-09-26', 'open': 221, 'high': 223.75, 'low': 219.76, 'close': 220.42, 'volume': 23984706, 'unadjustedVolume': 23984706, 'change': -1.77, 'changePercent': -0.797, 'vwap': 221.8912, 'label': 'Sep 26', 'changeOverTime': -0.0016758005344445154}, {'date': '2018-09-27', 'open': 223.82, 'high': 226.44, 'low': 223.54, 'close': 224.95, 'volume': 30181227, 'unadjustedVolume': 30181227, 'change': 4.53, 'changePercent': 2.055, 'vwap': 225.1658, 'label': 'Sep 27', 'changeOverTime': 0.018841433035916465}, {'date': '2018-09-28', 'open': 224.79, 'high': 225.84, 'low': 224.02, 'close': 225.74, 'volume': 22929364, 'unadjustedVolume': 22929364, 'change': 0.79, 'changePercent': 0.351, 'vwap': 225.1516, 'label': 'Sep 28', 'changeOverTime': 0.022419493636487237}, {'date': '2018-10-01', 'open': 227.95, 'high': 229.42, 'low': 226.35, 'close': 227.26, 'volume': 23600802, 'unadjustedVolume': 23600802, 'change': 1.52, 'changePercent': 0.673, 'vwap': 228.0504, 'label': 'Oct 1', 'changeOverTime': 0.029303863399610487}, {'date': '2018-10-02', 'open': 227.25, 'high': 230, 'low': 226.63, 'close': 229.28, 'volume': 24788170, 'unadjustedVolume': 24788170, 'change': 2.02, 'changePercent': 0.889, 'vwap': 229.0433, 'label': 'Oct 2', 'changeOverTime': 0.03845282847955075}, {'date': '2018-10-03', 'open': 230.05, 'high': 233.47, 'low': 229.78, 'close': 232.07, 'volume': 28654799, 'unadjustedVolume': 28654799, 'change': 2.79, 'changePercent': 1.217, 'vwap': 232.2344, 'label': 'Oct 3', 'changeOverTime': 0.05108927034738893}, {'date': '2018-10-04', 'open': 230.78, 'high': 232.35, 'low': 226.73, 'close': 227.99, 'volume': 32042000, 'unadjustedVolume': 32042000, 'change': -4.08, 'changePercent': -1.758, 'vwap': 228.7941, 'label': 'Oct 4', 'changeOverTime': 0.03261017256216322}, {'date': '2018-10-05', 'open': 227.96, 'high': 228.41, 'low': 220.58, 'close': 224.29, 'volume': 33580463, 'unadjustedVolume': 33580463, 'change': -3.7, 'changePercent': -1.623, 'vwap': 224.3801, 'label': 'Oct 5', 'changeOverTime': 0.015852167217718195}, {'date': '2018-10-08', 'open': 222.21, 'high': 224.8, 'low': 220.2, 'close': 223.77, 'volume': 29663923, 'unadjustedVolume': 29663923, 'change': -0.52, 'changePercent': -0.232, 'vwap': 222.7821, 'label': 'Oct 8', 'changeOverTime': 0.013496988088228716}, {'date': '2018-10-09', 'open': 223.64, 'high': 227.27, 'low': 222.2462, 'close': 226.87, 'volume': 26891029, 'unadjustedVolume': 26891029, 'change': 3.1, 'changePercent': 1.385, 'vwap': 225.6084, 'label': 'Oct 9', 'changeOverTime': 0.027537479052493378}, {'date': '2018-10-10', 'open': 225.46, 'high': 226.35, 'low': 216.05, 'close': 216.36, 'volume': 41990554, 'unadjustedVolume': 41990554, 'change': -10.51, 'changePercent': -4.633, 'vwap': 221.0408, 'label': 'Oct 10', 'changeOverTime': -0.020064314506997503}, {'date': '2018-10-11', 'open': 214.52, 'high': 219.5, 'low': 212.32, 'close': 214.45, 'volume': 53124392, 'unadjustedVolume': 53124392, 'change': -1.91, 'changePercent': -0.883, 'vwap': 215.8281, 'label': 'Oct 11', 'changeOverTime': -0.028715068617238115}, {'date': '2018-10-12', 'open': 220.42, 'high': 222.88, 'low': 216.84, 'close': 222.11, 'volume': 40337851, 'unadjustedVolume': 40337851, 'change': 7.66, 'changePercent': 3.572, 'vwap': 220.3926, 'label': 'Oct 12', 'changeOverTime': 0.005978531636396674}, {'date': '2018-10-15', 'open': 221.16, 'high': 221.83, 'low': 217.27, 'close': 217.36, 'volume': 30791007, 'unadjustedVolume': 30791007, 'change': -4.75, 'changePercent': -2.139, 'vwap': 218.7385, 'label': 'Oct 15', 'changeOverTime': -0.015535123873363733}, {'date': '2018-10-16', 'open': 218.93, 'high': 222.99, 'low': 216.7627, 'close': 222.15, 'volume': 29183963, 'unadjustedVolume': 29183963, 'change': 4.79, 'changePercent': 2.204, 'vwap': 219.9988, 'label': 'Oct 16', 'changeOverTime': 0.006159699261741989}, {'date': '2018-10-17', 'open': 222.3, 'high': 222.64, 'low': 219.34, 'close': 221.19, 'volume': 22885397, 'unadjustedVolume': 22885397, 'change': -0.96, 'changePercent': -0.432, 'vwap': 221.0079, 'label': 'Oct 17', 'changeOverTime': 0.0018116762534535337}, {'date': '2018-10-18', 'open': 217.86, 'high': 219.74, 'low': 213, 'close': 216.02, 'volume': 32581315, 'unadjustedVolume': 32581315, 'change': -5.17, 'changePercent': -2.337, 'vwap': 216.9844, 'label': 'Oct 18', 'changeOverTime': -0.021604239322433}, {'date': '2018-10-19', 'open': 218.06, 'high': 221.26, 'low': 217.43, 'close': 219.31, 'volume': 33078726, 'unadjustedVolume': 33078726, 'change': 3.29, 'changePercent': 1.523, 'vwap': 219.3602, 'label': 'Oct 19', 'changeOverTime': -0.006703202137777933}, {'date': '2018-10-22', 'open': 219.79, 'high': 223.36, 'low': 218.94, 'close': 220.65, 'volume': 28792082, 'unadjustedVolume': 28792082, 'change': 1.34, 'changePercent': 0.611, 'vwap': 221.288, 'label': 'Oct 22', 'changeOverTime': -0.000634086688708666}]}
res2 = {'AAPL': {'quote': {'symbol': 'AAPL', 'companyName': 'Apple Inc.', 'primaryExchange': 'Nasdaq Global Select', 'sector': 'Technology', 'calculationPrice': 'close', 'open': 219.66, 'openTime': 1540215000651, 'close': 220.65, 'closeTime': 1540238400188, 'high': 223.36, 'low': 218.94, 'latestPrice': 220.65, 'latestSource': 'Close', 'latestTime': 'October 22, 2018', 'latestUpdate': 1540238400188, 'latestVolume': 28576651, 'iexRealtimePrice': 220.61, 'iexRealtimeSize': 100, 'iexLastUpdated': 1540238399824, 'delayedPrice': 220.59, 'delayedPriceTime': 1540238400242, 'extendedPrice': 220.65, 'extendedChange': 0, 'extendedChangePercent': 0, 'extendedPriceTime': 1540241992052, 'previousClose': 219.31, 'change': 1.34, 'changePercent': 0.00611, 'iexMarketPercent': 0.0427, 'iexVolume': 1220223, 'avgTotalVolume': 34317785, 'iexBidPrice': 0, 'iexBidSize': 0, 'iexAskPrice': 0, 'iexAskSize': 0, 'marketCap': 1065723171900, 'peRatio': 20, 'week52High': 233.47, 'week52Low': 150.24, 'ytdChange': 0.30173277383646435}, 'news': [{'datetime': '2018-10-22T20:35:34-04:00', 'headline': 'Could Apple Really Hit $310 In 2019?', 'source': 'SeekingAlpha', 'url': 'https://api.iextrading.com/1.0/stock/aapl/article/7212636922090000', 'summary': '   Apple (AAPL) is far and away my largest holding, making up nearly 10% of my portfolio, so Im always happy when I see a positive analyst note. For some reason or another, the market typically moves on these notes. When doing my daily due diligence last week, I came across a  note  put o…', 'related': 'AAPL,Computer Hardware,CON31167138,NASDAQ01,Computing and Information Technology', 'image': 'https://api.iextrading.com/1.0/stock/aapl/news-image/7212636922090000'}], 'chart': [{'date': '2018-09-24', 'open': 216.82, 'high': 221.26, 'low': 216.63, 'close': 220.79, 'volume': 27693358, 'unadjustedVolume': 27693358, 'change': 3.13, 'changePercent': 1.438, 'vwap': 219.4487, 'label': 'Sep 24', 'changeOverTime': 0}, {'date': '2018-09-25', 'open': 219.75, 'high': 222.82, 'low': 219.7, 'close': 222.19, 'volume': 24554379, 'unadjustedVolume': 24554379, 'change': 1.4, 'changePercent': 0.634, 'vwap': 221.6295, 'label': 'Sep 25', 'changeOverTime': 0.0063408668870873035}, {'date': '2018-09-26', 'open': 221, 'high': 223.75, 'low': 219.76, 'close': 220.42, 'volume': 23984706, 'unadjustedVolume': 23984706, 'change': -1.77, 'changePercent': -0.797, 'vwap': 221.8912, 'label': 'Sep 26', 'changeOverTime': -0.0016758005344445154}, {'date': '2018-09-27', 'open': 223.82, 'high': 226.44, 'low': 223.54, 'close': 224.95, 'volume': 30181227, 'unadjustedVolume': 30181227, 'change': 4.53, 'changePercent': 2.055, 'vwap': 225.1658, 'label': 'Sep 27', 'changeOverTime': 0.018841433035916465}, {'date': '2018-09-28', 'open': 224.79, 'high': 225.84, 'low': 224.02, 'close': 225.74, 'volume': 22929364, 'unadjustedVolume': 22929364, 'change': 0.79, 'changePercent': 0.351, 'vwap': 225.1516, 'label': 'Sep 28', 'changeOverTime': 0.022419493636487237}, {'date': '2018-10-01', 'open': 227.95, 'high': 229.42, 'low': 226.35, 'close': 227.26, 'volume': 23600802, 'unadjustedVolume': 23600802, 'change': 1.52, 'changePercent': 0.673, 'vwap': 228.0504, 'label': 'Oct 1', 'changeOverTime': 0.029303863399610487}, {'date': '2018-10-02', 'open': 227.25, 'high': 230, 'low': 226.63, 'close': 229.28, 'volume': 24788170, 'unadjustedVolume': 24788170, 'change': 2.02, 'changePercent': 0.889, 'vwap': 229.0433, 'label': 'Oct 2', 'changeOverTime': 0.03845282847955075}, {'date': '2018-10-03', 'open': 230.05, 'high': 233.47, 'low': 229.78, 'close': 232.07, 'volume': 28654799, 'unadjustedVolume': 28654799, 'change': 2.79, 'changePercent': 1.217, 'vwap': 232.2344, 'label': 'Oct 3', 'changeOverTime': 0.05108927034738893}, {'date': '2018-10-04', 'open': 230.78, 'high': 232.35, 'low': 226.73, 'close': 227.99, 'volume': 32042000, 'unadjustedVolume': 32042000, 'change': -4.08, 'changePercent': -1.758, 'vwap': 228.7941, 'label': 'Oct 4', 'changeOverTime': 0.03261017256216322}, {'date': '2018-10-05', 'open': 227.96, 'high': 228.41, 'low': 220.58, 'close': 224.29, 'volume': 33580463, 'unadjustedVolume': 33580463, 'change': -3.7, 'changePercent': -1.623, 'vwap': 224.3801, 'label': 'Oct 5', 'changeOverTime': 0.015852167217718195}, {'date': '2018-10-08', 'open': 222.21, 'high': 224.8, 'low': 220.2, 'close': 223.77, 'volume': 29663923, 'unadjustedVolume': 29663923, 'change': -0.52, 'changePercent': -0.232, 'vwap': 222.7821, 'label': 'Oct 8', 'changeOverTime': 0.013496988088228716}, {'date': '2018-10-09', 'open': 223.64, 'high': 227.27, 'low': 222.2462, 'close': 226.87, 'volume': 26891029, 'unadjustedVolume': 26891029, 'change': 3.1, 'changePercent': 1.385, 'vwap': 225.6084, 'label': 'Oct 9', 'changeOverTime': 0.027537479052493378}, {'date': '2018-10-10', 'open': 225.46, 'high': 226.35, 'low': 216.05, 'close': 216.36, 'volume': 41990554, 'unadjustedVolume': 41990554, 'change': -10.51, 'changePercent': -4.633, 'vwap': 221.0408, 'label': 'Oct 10', 'changeOverTime': -0.020064314506997503}, {'date': '2018-10-11', 'open': 214.52, 'high': 219.5, 'low': 212.32, 'close': 214.45, 'volume': 53124392, 'unadjustedVolume': 53124392, 'change': -1.91, 'changePercent': -0.883, 'vwap': 215.8281, 'label': 'Oct 11', 'changeOverTime': -0.028715068617238115}, {'date': '2018-10-12', 'open': 220.42, 'high': 222.88, 'low': 216.84, 'close': 222.11, 'volume': 40337851, 'unadjustedVolume': 40337851, 'change': 7.66, 'changePercent': 3.572, 'vwap': 220.3926, 'label': 'Oct 12', 'changeOverTime': 0.005978531636396674}, {'date': '2018-10-15', 'open': 221.16, 'high': 221.83, 'low': 217.27, 'close': 217.36, 'volume': 30791007, 'unadjustedVolume': 30791007, 'change': -4.75, 'changePercent': -2.139, 'vwap': 218.7385, 'label': 'Oct 15', 'changeOverTime': -0.015535123873363733}, {'date': '2018-10-16', 'open': 218.93, 'high': 222.99, 'low': 216.7627, 'close': 222.15, 'volume': 29183963, 'unadjustedVolume': 29183963, 'change': 4.79, 'changePercent': 2.204, 'vwap': 219.9988, 'label': 'Oct 16', 'changeOverTime': 0.006159699261741989}, {'date': '2018-10-17', 'open': 222.3, 'high': 222.64, 'low': 219.34, 'close': 221.19, 'volume': 22885397, 'unadjustedVolume': 22885397, 'change': -0.96, 'changePercent': -0.432, 'vwap': 221.0079, 'label': 'Oct 17', 'changeOverTime': 0.0018116762534535337}, {'date': '2018-10-18', 'open': 217.86, 'high': 219.74, 'low': 213, 'close': 216.02, 'volume': 32581315, 'unadjustedVolume': 32581315, 'change': -5.17, 'changePercent': -2.337, 'vwap': 216.9844, 'label': 'Oct 18', 'changeOverTime': -0.021604239322433}, {'date': '2018-10-19', 'open': 218.06, 'high': 221.26, 'low': 217.43, 'close': 219.31, 'volume': 33078726, 'unadjustedVolume': 33078726, 'change': 3.29, 'changePercent': 1.523, 'vwap': 219.3602, 'label': 'Oct 19', 'changeOverTime': -0.006703202137777933}, {'date': '2018-10-22', 'open': 219.79, 'high': 223.36, 'low': 218.94, 'close': 220.65, 'volume': 28792082, 'unadjustedVolume': 28792082, 'change': 1.34, 'changePercent': 0.611, 'vwap': 221.288, 'label': 'Oct 22', 'changeOverTime': -0.000634086688708666}]}, 'FB': {'quote': {'symbol': 'FB', 'companyName': 'Facebook Inc.', 'primaryExchange': 'Nasdaq Global Select', 'sector': 'Technology', 'calculationPrice': 'close', 'open': 154.76, 'openTime': 1540215000501, 'close': 154.78, 'closeTime': 1540238400231, 'high': 157.34, 'low': 154.46, 'latestPrice': 154.78, 'latestSource': 'Close', 'latestTime': 'October 22, 2018', 'latestUpdate': 1540238400231, 'latestVolume': 15179196, 'iexRealtimePrice': 154.81, 'iexRealtimeSize': 100, 'iexLastUpdated': 1540238399749, 'delayedPrice': 154.81, 'delayedPriceTime': 1540238400243, 'extendedPrice': 154.9, 'extendedChange': 0.12, 'extendedChangePercent': 0.00078, 'extendedPriceTime': 1540241941660, 'previousClose': 154.05, 'change': 0.73, 'changePercent': 0.00474, 'iexMarketPercent': 0.03658, 'iexVolume': 555255, 'avgTotalVolume': 24614145, 'iexBidPrice': 0, 'iexBidSize': 0, 'iexAskPrice': 0, 'iexAskSize': 0, 'marketCap': 446883704814, 'peRatio': 21.44, 'week52High': 218.62, 'week52Low': 149.02, 'ytdChange': -0.14210158306691648}, 'news': [{'datetime': '2018-10-22T18:50:00-04:00', 'headline': "Cramer's lightning round: I think Dropbox's stock is 'trying to bottom'", 'source': 'CNBC', 'url': 'https://api.iextrading.com/1.0/stock/fb/article/8744373879434531', 'summary': 'No summary available.', 'related': 'ALB,FB,JKHY,PANW,TTD', 'image': 'https://api.iextrading.com/1.0/stock/fb/news-image/8744373879434531'}, {'datetime': '2018-10-22T18:10:00-04:00', 'headline': 'Cramer: We could be facing a cold war with China, and these stocks may be sacrificed', 'source': 'CNBC', 'url': 'https://api.iextrading.com/1.0/stock/fb/article/6290239235980837', 'summary': 'No summary available.', 'related': 'AAPL,AMAT,AMZN,COL,FB,GOOGL,MU,UTX', 'image': 'https://api.iextrading.com/1.0/stock/fb/news-image/6290239235980837'}, {'datetime': '2018-10-22T18:01:00-04:00', 'headline': 'Apple is probably the best tech bet heading into earnings, says venture capitalist Gene Munster', 'source': 'CNBC', 'url': 'https://api.iextrading.com/1.0/stock/fb/article/8083958942383177', 'summary': 'No summary available.', 'related': 'AAPL,AMZN,FB,GOOGL,INTC', 'image': 'https://api.iextrading.com/1.0/stock/fb/news-image/8083958942383177'}, {'datetime': '2018-10-22T15:51:00-04:00', 'headline': "The man behind TSA's wildly popular and bizarre Instagram account unexpectedly dies at 48", 'source': 'CNBC', 'url': 'https://api.iextrading.com/1.0/stock/fb/article/8111825077651662', 'summary': 'No summary available.', 'related': 'AAL,FB', 'image': 'https://api.iextrading.com/1.0/stock/fb/news-image/8111825077651662'}, {'datetime': '2018-10-22T15:41:24-04:00', 'headline': "Oppenheimer names its picks for Facebook's cybersecurity buy", 'source': 'SeekingAlpha', 'url': 'https://api.iextrading.com/1.0/stock/fb/article/6708420787694031', 'summary': '      Oppenheimer names its top picks for Facebooks ( FB   +0.9% ) potential cybersecurity acquisition: Fortinet ( FTNT   +2.5% ), Palo Alto Networks ( PANW   +0.7% ), Check Point Software ( CHKP   +2.6% ), Splunk ( SPLK   +2.1% ), and FireEye ( FEYE   +4.2% ).   More news on: Facebook, F…', 'related': 'CHKP,FB,FEYE,FTNT,INT31168144,NASDAQ01,ONL31168,PANW,SPLK,Computing and Information Technology', 'image': 'https://api.iextrading.com/1.0/stock/fb/news-image/6708420787694031'}], 'chart': [{'date': '2018-09-24', 'open': 161.03, 'high': 165.7, 'low': 160.88, 'close': 165.41, 'volume': 19222775, 'unadjustedVolume': 19222775, 'change': 2.48, 'changePercent': 1.522, 'vwap': 164.4054, 'label': 'Sep 24', 'changeOverTime': 0}, {'date': '2018-09-25', 'open': 161.99, 'high': 165.59, 'low': 161.15, 'close': 164.91, 'volume': 27622806, 'unadjustedVolume': 27622806, 'change': -0.5, 'changePercent': -0.302, 'vwap': 163.6232, 'label': 'Sep 25', 'changeOverTime': -0.003022791850553171}, {'date': '2018-09-26', 'open': 164.3, 'high': 169.3, 'low': 164.21, 'close': 166.95, 'volume': 25252231, 'unadjustedVolume': 25252231, 'change': 2.04, 'changePercent': 1.237, 'vwap': 167.3214, 'label': 'Sep 26', 'changeOverTime': 0.009310198899703718}, {'date': '2018-09-27', 'open': 167.55, 'high': 171.77, 'low': 167.21, 'close': 168.84, 'volume': 27266856, 'unadjustedVolume': 27266856, 'change': 1.89, 'changePercent': 1.132, 'vwap': 169.7643, 'label': 'Sep 27', 'changeOverTime': 0.020736352094794793}, {'date': '2018-09-28', 'open': 168.33, 'high': 168.79, 'low': 162.56, 'close': 164.46, 'volume': 34265638, 'unadjustedVolume': 34265638, 'change': -4.38, 'changePercent': -2.594, 'vwap': 164.8263, 'label': 'Sep 28', 'changeOverTime': -0.005743304516050956}, {'date': '2018-10-01', 'open': 163.03, 'high': 165.88, 'low': 161.26, 'close': 162.44, 'volume': 26407677, 'unadjustedVolume': 26407677, 'change': -2.02, 'changePercent': -1.228, 'vwap': 162.9928, 'label': 'Oct 1', 'changeOverTime': -0.01795538359228583}, {'date': '2018-10-02', 'open': 161.58, 'high': 162.28, 'low': 158.67, 'close': 159.33, 'volume': 36030977, 'unadjustedVolume': 36030977, 'change': -3.11, 'changePercent': -1.915, 'vwap': 159.8712, 'label': 'Oct 2', 'changeOverTime': -0.03675714890272646}, {'date': '2018-10-03', 'open': 160, 'high': 163.66, 'low': 159.53, 'close': 162.43, 'volume': 23109456, 'unadjustedVolume': 23109456, 'change': 3.1, 'changePercent': 1.946, 'vwap': 161.8944, 'label': 'Oct 3', 'changeOverTime': -0.018015839429296836}, {'date': '2018-10-04', 'open': 161.46, 'high': 161.46, 'low': 157.35, 'close': 158.85, 'volume': 25739635, 'unadjustedVolume': 25739635, 'change': -3.58, 'changePercent': -2.204, 'vwap': 158.9925, 'label': 'Oct 4', 'changeOverTime': -0.03965902907925762}, {'date': '2018-10-05', 'open': 159.21, 'high': 160.9, 'low': 156.2, 'close': 157.33, 'volume': 25744047, 'unadjustedVolume': 25744047, 'change': -1.52, 'changePercent': -0.957, 'vwap': 158.1677, 'label': 'Oct 5', 'changeOverTime': -0.048848316304939146}, {'date': '2018-10-08', 'open': 155.54, 'high': 158.34, 'low': 154.39, 'close': 157.25, 'volume': 24045968, 'unadjustedVolume': 24045968, 'change': -0.08, 'changePercent': -0.051, 'vwap': 156.5515, 'label': 'Oct 8', 'changeOverTime': -0.04933196300102773}, {'date': '2018-10-09', 'open': 157.69, 'high': 160.59, 'low': 157.42, 'close': 157.9, 'volume': 18844425, 'unadjustedVolume': 18844425, 'change': 0.65, 'changePercent': 0.413, 'vwap': 159.032, 'label': 'Oct 9', 'changeOverTime': -0.045402333595308576}, {'date': '2018-10-10', 'open': 156.82, 'high': 157.69, 'low': 151.31, 'close': 151.38, 'volume': 30609970, 'unadjustedVolume': 30609970, 'change': -6.52, 'changePercent': -4.129, 'vwap': 154.1822, 'label': 'Oct 10', 'changeOverTime': -0.08481953932652199}, {'date': '2018-10-11', 'open': 150.13, 'high': 154.81, 'low': 149.16, 'close': 153.35, 'volume': 35338901, 'unadjustedVolume': 35338901, 'change': 1.97, 'changePercent': 1.301, 'vwap': 152.6894, 'label': 'Oct 11', 'changeOverTime': -0.0729097394353425}, {'date': '2018-10-12', 'open': 156.73, 'high': 156.89, 'low': 151.2998, 'close': 153.74, 'volume': 25293492, 'unadjustedVolume': 25293492, 'change': 0.39, 'changePercent': 0.254, 'vwap': 153.7208, 'label': 'Oct 12', 'changeOverTime': -0.07055196179191094}, {'date': '2018-10-15', 'open': 153.32, 'high': 155.57, 'low': 152.55, 'close': 153.52, 'volume': 15433521, 'unadjustedVolume': 15433521, 'change': -0.22, 'changePercent': -0.143, 'vwap': 154.1451, 'label': 'Oct 15', 'changeOverTime': -0.07188199020615432}, {'date': '2018-10-16', 'open': 155.4, 'high': 159.46, 'low': 155.01, 'close': 158.78, 'volume': 19180095, 'unadjustedVolume': 19180095, 'change': 5.26, 'changePercent': 3.426, 'vwap': 157.3995, 'label': 'Oct 16', 'changeOverTime': -0.040082219938335016}, {'date': '2018-10-17', 'open': 159.56, 'high': 160.49, 'low': 157.95, 'close': 159.42, 'volume': 17592003, 'unadjustedVolume': 17592003, 'change': 0.64, 'changePercent': 0.403, 'vwap': 159.1927, 'label': 'Oct 17', 'changeOverTime': -0.03621304636962704}, {'date': '2018-10-18', 'open': 158.51, 'high': 158.66, 'low': 153.28, 'close': 154.92, 'volume': 21675084, 'unadjustedVolume': 21675084, 'change': -4.5, 'changePercent': -2.823, 'vwap': 155.485, 'label': 'Oct 18', 'changeOverTime': -0.06341817302460558}, {'date': '2018-10-19', 'open': 155.86, 'high': 157.35, 'low': 153.55, 'close': 154.05, 'volume': 19761347, 'unadjustedVolume': 19761347, 'change': -0.87, 'changePercent': -0.562, 'vwap': 155.0912, 'label': 'Oct 19', 'changeOverTime': -0.06867783084456795}, {'date': '2018-10-22', 'open': 154.76, 'high': 157.34, 'low': 154.46, 'close': 154.78, 'volume': 15424658, 'unadjustedVolume': 15424658, 'change': 0.73, 'changePercent': 0.474, 'vwap': 155.584, 'label': 'Oct 22', 'changeOverTime': -0.06426455474276038}]}, 'TSLA': {'quote': {'symbol': 'TSLA', 'companyName': 'Tesla Inc.', 'primaryExchange': 'Nasdaq Global Select', 'sector': 'Consumer Cyclical', 'calculationPrice': 'close', 'open': 260.68, 'openTime': 1540215000635, 'close': 260.95, 'closeTime': 1540238400399, 'high': 261.86, 'low': 252.59, 'latestPrice': 260.95, 'latestSource': 'Close', 'latestTime': 'October 22, 2018', 'latestUpdate': 1540238400399, 'latestVolume': 5570414, 'iexRealtimePrice': 261.03, 'iexRealtimeSize': 24, 'iexLastUpdated': 1540238395567, 'delayedPrice': 260.95, 'delayedPriceTime': 1540238400399, 'extendedPrice': 260.64, 'extendedChange': -0.31, 'extendedChangePercent': -0.00119, 'extendedPriceTime': 1540241989945, 'previousClose': 260, 'change': 0.95, 'changePercent': 0.00365, 'iexMarketPercent': 0.02704, 'iexVolume': 150624, 'avgTotalVolume': 10406754, 'iexBidPrice': 0, 'iexBidSize': 0, 'iexAskPrice': 0, 'iexAskSize': 0, 'marketCap': 44516280927, 'peRatio': -16.47, 'week52High': 387.46, 'week52Low': 244.5901, 'ytdChange': -0.18222963685146473}, 'news': [{'datetime': '2018-10-22T19:50:12-04:00', 'headline': 'Volvo Opens U.S. Factory, Grows 30% In 2018, Will Launch 5 Electric Cars', 'source': 'SeekingAlpha', 'url': 'https://api.iextrading.com/1.0/stock/tsla/article/8621867891816298', 'summary': '     The automotive industry is beset by a few major challenges that have, on the whole, compressed valuation multiples in recent months. Almost all automakers are trading well below where they were six or 12 months ago: Ford ( F ), General Motors ( GM ), FCA ( FCAU ), Tesla ( TSLA ) and others. …', 'related': 'AUT10209,AUT10209017,Automotive,CON102,DDAIF,F,FCAU,GELYF,GM,GMM.U:CA,Industrial Goods,INTHPINK,MZDAF,NASDAQ01,SCITECH1,TM,TSLA,TSXTSX01', 'image': 'https://api.iextrading.com/1.0/stock/tsla/news-image/8621867891816298'}, {'datetime': '2018-10-22T16:41:44-04:00', 'headline': 'Tesla Is Misleading Markets About China Factory', 'source': 'SeekingAlpha', 'url': 'https://api.iextrading.com/1.0/stock/tsla/article/5298918336960711', 'summary': "   Tesla ( TSLA ) has always been great at selling dreams of tomorrow while distracting from the problems of today.   The company's hype machine, signal-boosted by CEO Elon Musk and a host of adoring fans, has repeatedly managed to shift narratives from near-term struggles to the future, when som…", 'related': 'AUT10209,AUT10209017,CON102,NASDAQ01,SCITECH1,TSLA', 'image': 'https://api.iextrading.com/1.0/stock/tsla/news-image/5298918336960711'}, {'datetime': '2018-10-22T13:45:31-04:00', 'headline': 'Tesla, Universe And Everything?', 'source': 'SeekingAlpha', 'url': 'https://api.iextrading.com/1.0/stock/tsla/article/6408546135675475', 'summary': "   With the recent wild swings in the market and turbulence in the Tesla ( TSLA ) share price, investors are looking for insight into the future of the company and of the stock. Many factors are driving the market for Tesla shares right now, so let's take a look.   Tesla's Model 3 electric car is…", 'related': 'BASICMAT,CHE10103,INTHPINK,NASDAQ01,NNOMF,SPECCHEM,TSLA', 'image': 'https://api.iextrading.com/1.0/stock/tsla/news-image/6408546135675475'}, {'datetime': '2018-10-22T13:34:50-04:00', 'headline': 'Will The Tesla Model 3 Be Approved For Sale In Europe?', 'source': 'SeekingAlpha', 'url': 'https://api.iextrading.com/1.0/stock/tsla/article/4872977691335190', 'summary': "     There's a new issue that has emerged, from two separate directions, that we need to talk about. Over the last month or so, the lack of any word about Europe approving the Tesla (TSLA) Model 3 for sale caused several people to reach out to me and ask whether I think that Europe will deny the …", 'related': 'AUDVF,AUT10209,AUT10209017,CON102,Europe,INTHPINK,NASDAQ01,OTCBULLB,TSLA,TTM,VLKAF,VLKPF,VWAGY,WOMPOLIX', 'image': 'https://api.iextrading.com/1.0/stock/tsla/news-image/4872977691335190'}, {'datetime': '2018-10-22T13:24:09-04:00', 'headline': 'Tesla Faces A Margin Problem In 2019', 'source': 'SeekingAlpha', 'url': 'https://api.iextrading.com/1.0/stock/tsla/article/4716452027539274', 'summary': '   Now that production has seemed to stabilize a bit for Tesla ( TSLA ) more than a year after the Model 3 launch, investors are curious as to whether or not the company can be profitable on a sustained basis. Last week, the company launched a  new mid-range version  of the vehicle that has broug…', 'related': 'AUT10209,AUT10209017,CON102,NASDAQ01,TSLA', 'image': 'https://api.iextrading.com/1.0/stock/tsla/news-image/4716452027539274'}], 'chart': [{'date': '2018-09-24', 'open': 298.48, 'high': 302.9993, 'low': 293.58, 'close': 299.68, 'volume': 4842961, 'unadjustedVolume': 4842961, 'change': 0.58, 'changePercent': 0.194, 'vwap': 298.5245, 'label': 'Sep 24', 'changeOverTime': 0}, {'date': '2018-09-25', 'open': 300, 'high': 304.6, 'low': 296.5, 'close': 300.99, 'volume': 4481729, 'unadjustedVolume': 4481729, 'change': 1.31, 'changePercent': 0.437, 'vwap': 299.6735, 'label': 'Sep 25', 'changeOverTime': 0.004371329418045923}, {'date': '2018-09-26', 'open': 301.91, 'high': 313.89, 'low': 301.1093, 'close': 309.58, 'volume': 7843216, 'unadjustedVolume': 7843216, 'change': 8.59, 'changePercent': 2.854, 'vwap': 308.6394, 'label': 'Sep 26', 'changeOverTime': 0.033035237586759136}, {'date': '2018-09-27', 'open': 312.9, 'high': 314.96, 'low': 306.91, 'close': 307.52, 'volume': 8509084, 'unadjustedVolume': 8509084, 'change': -2.06, 'changePercent': -0.665, 'vwap': 309.839, 'label': 'Sep 27', 'changeOverTime': 0.026161238654564784}, {'date': '2018-09-28', 'open': 270.26, 'high': 278, 'low': 260.555, 'close': 264.77, 'volume': 33649694, 'unadjustedVolume': 33649694, 'change': -42.75, 'changePercent': -13.902, 'vwap': 268.9403, 'label': 'Sep 28', 'changeOverTime': -0.11649092365189544}, {'date': '2018-10-01', 'open': 305.77, 'high': 311.44, 'low': 301.05, 'close': 310.7, 'volume': 21777597, 'unadjustedVolume': 21777597, 'change': 45.93, 'changePercent': 17.347, 'vwap': 307.6083, 'label': 'Oct 1', 'changeOverTime': 0.03677255739455413}, {'date': '2018-10-02', 'open': 313.95, 'high': 316.84, 'low': 299.15, 'close': 301.02, 'volume': 11743511, 'unadjustedVolume': 11743511, 'change': -9.68, 'changePercent': -3.116, 'vwap': 306.3166, 'label': 'Oct 2', 'changeOverTime': 0.004471436198611769}, {'date': '2018-10-03', 'open': 303.33, 'high': 304.6, 'low': 291.57, 'close': 294.8, 'volume': 7994988, 'unadjustedVolume': 7994988, 'change': -6.22, 'changePercent': -2.066, 'vwap': 295.9612, 'label': 'Oct 3', 'changeOverTime': -0.016284036305392404}, {'date': '2018-10-04', 'open': 293.95, 'high': 294, 'low': 277.67, 'close': 281.83, 'volume': 9814212, 'unadjustedVolume': 9814212, 'change': -12.97, 'changePercent': -4.4, 'vwap': 283.1426, 'label': 'Oct 4', 'changeOverTime': -0.05956353443673259}, {'date': '2018-10-05', 'open': 274.65, 'high': 274.88, 'low': 260, 'close': 261.95, 'volume': 17944537, 'unadjustedVolume': 17944537, 'change': -19.88, 'changePercent': -7.054, 'vwap': 265.4947, 'label': 'Oct 5', 'changeOverTime': -0.1259009610250935}, {'date': '2018-10-08', 'open': 264.52, 'high': 267.7599, 'low': 249, 'close': 250.56, 'volume': 13472653, 'unadjustedVolume': 13472653, 'change': -11.39, 'changePercent': -4.348, 'vwap': 255.3077, 'label': 'Oct 8', 'changeOverTime': -0.1639081687132942}, {'date': '2018-10-09', 'open': 255.25, 'high': 266.77, 'low': 253.3, 'close': 262.8, 'volume': 12060574, 'unadjustedVolume': 12060574, 'change': 12.24, 'changePercent': 4.885, 'vwap': 261.4977, 'label': 'Oct 9', 'changeOverTime': -0.12306460224239187}, {'date': '2018-10-10', 'open': 264.61, 'high': 265.51, 'low': 247.77, 'close': 256.88, 'volume': 12815278, 'unadjustedVolume': 12815278, 'change': -5.92, 'changePercent': -2.253, 'vwap': 255.1419, 'label': 'Oct 10', 'changeOverTime': -0.14281900694073682}, {'date': '2018-10-11', 'open': 257.53, 'high': 262.25, 'low': 249.03, 'close': 252.23, 'volume': 8167738, 'unadjustedVolume': 8167738, 'change': -4.65, 'changePercent': -1.81, 'vwap': 253.6752, 'label': 'Oct 11', 'changeOverTime': -0.15833555792845708}, {'date': '2018-10-12', 'open': 261, 'high': 261.99, 'low': 252.01, 'close': 258.78, 'volume': 7201404, 'unadjustedVolume': 7201404, 'change': 6.55, 'changePercent': 2.597, 'vwap': 256.9542, 'label': 'Oct 12', 'changeOverTime': -0.13647891083822755}, {'date': '2018-10-15', 'open': 259.06, 'high': 263.28, 'low': 254.5367, 'close': 259.59, 'volume': 6199965, 'unadjustedVolume': 6199965, 'change': 0.81, 'changePercent': 0.313, 'vwap': 258.8046, 'label': 'Oct 15', 'changeOverTime': -0.13377602776294725}, {'date': '2018-10-16', 'open': 265.7, 'high': 277.375, 'low': 262.24, 'close': 276.59, 'volume': 9526401, 'unadjustedVolume': 9526401, 'change': 17, 'changePercent': 6.549, 'vwap': 271.5296, 'label': 'Oct 16', 'changeOverTime': -0.07704885210891628}, {'date': '2018-10-17', 'open': 282.4, 'high': 282.7, 'low': 265.8032, 'close': 271.78, 'volume': 8655542, 'unadjustedVolume': 8655542, 'change': -4.81, 'changePercent': -1.739, 'vwap': 272.1143, 'label': 'Oct 17', 'changeOverTime': -0.09309930592632153}, {'date': '2018-10-18', 'open': 269.29, 'high': 271, 'low': 263, 'close': 263.91, 'volume': 5421184, 'unadjustedVolume': 5421184, 'change': -7.87, 'changePercent': -2.896, 'vwap': 266.2906, 'label': 'Oct 18', 'changeOverTime': -0.11936065136145216}, {'date': '2018-10-19', 'open': 267.39, 'high': 269.66, 'low': 253.5, 'close': 260, 'volume': 9375549, 'unadjustedVolume': 9375549, 'change': -3.91, 'changePercent': -1.482, 'vwap': 259.7345, 'label': 'Oct 19', 'changeOverTime': -0.13240790176187936}, {'date': '2018-10-22', 'open': 260.68, 'high': 261.86, 'low': 252.59, 'close': 260.95, 'volume': 5600260, 'unadjustedVolume': 5600260, 'change': 0.95, 'changePercent': 0.365, 'vwap': 257.7557, 'label': 'Oct 22', 'changeOverTime': -0.1292378537106247}]}}
res3 = {'quote': {'symbol': 'AAPL', 'companyName': 'Apple Inc.', 'primaryExchange': 'Nasdaq Global Select', 'sector': 'Technology', 'calculationPrice': 'close', 'open': 219.66, 'openTime': 1540215000651, 'close': 220.65, 'closeTime': 1540238400188, 'high': 223.36, 'low': 218.94, 'latestPrice': 220.65, 'latestSource': 'Close', 'latestTime': 'October 22, 2018', 'latestUpdate': 1540238400188, 'latestVolume': 28576651, 'iexRealtimePrice': 220.61, 'iexRealtimeSize': 100, 'iexLastUpdated': 1540238399824, 'delayedPrice': 220.59, 'delayedPriceTime': 1540238400242, 'extendedPrice': 220.65, 'extendedChange': 0, 'extendedChangePercent': 0, 'extendedPriceTime': 1540241992052, 'previousClose': 219.31, 'change': 1.34, 'changePercent': 0.00611, 'iexMarketPercent': 0.0427, 'iexVolume': 1220223, 'avgTotalVolume': 34317785, 'iexBidPrice': 0, 'iexBidSize': 0, 'iexAskPrice': 0, 'iexAskSize': 0, 'marketCap': 1065723171900, 'peRatio': 20, 'week52High': 233.47, 'week52Low': 150.24, 'ytdChange': 0.30173277383646435}, 'bids': [], 'asks': [], 'trades': [{'price': 220.61, 'size': 100, 'tradeId': 1094967312, 'isISO': True, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238399824}, {'price': 220.61, 'size': 100, 'tradeId': 1094967292, 'isISO': True, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238399824}, {'price': 220.64, 'size': 100, 'tradeId': 1094950643, 'isISO': True, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238399749}, {'price': 220.64, 'size': 100, 'tradeId': 1094950605, 'isISO': True, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238399749}, {'price': 220.66, 'size': 100, 'tradeId': 1094904168, 'isISO': True, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238399524}, {'price': 220.66, 'size': 100, 'tradeId': 1094813552, 'isISO': True, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238399038}, {'price': 220.66, 'size': 100, 'tradeId': 1094813539, 'isISO': True, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238399038}, {'price': 220.67, 'size': 100, 'tradeId': 1094615062, 'isISO': True, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238398131}, {'price': 220.67, 'size': 100, 'tradeId': 1094615047, 'isISO': True, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238398131}, {'price': 220.72, 'size': 100, 'tradeId': 1094280883, 'isISO': True, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238396690}, {'price': 220.83, 'size': 100, 'tradeId': 1093911343, 'isISO': True, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238395202}, {'price': 220.88, 'size': 100, 'tradeId': 1093893685, 'isISO': False, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238395161}, {'price': 220.87, 'size': 100, 'tradeId': 1093885379, 'isISO': False, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238395148}, {'price': 220.88, 'size': 45, 'tradeId': 1093883318, 'isISO': False, 'isOddLot': True, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238395145}, {'price': 220.82, 'size': 100, 'tradeId': 1093864301, 'isISO': True, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238395110}, {'price': 220.82, 'size': 100, 'tradeId': 1093859447, 'isISO': False, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238395105}, {'price': 220.82, 'size': 100, 'tradeId': 1093859436, 'isISO': False, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238395105}, {'price': 220.9, 'size': 100, 'tradeId': 1093856648, 'isISO': False, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238395101}, {'price': 220.77, 'size': 48, 'tradeId': 1093846483, 'isISO': False, 'isOddLot': True, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238395085}, {'price': 220.77, 'size': 100, 'tradeId': 1093806592, 'isISO': False, 'isOddLot': False, 'isOutsideRegularHours': False, 'isSinglePriceCross': False, 'isTradeThroughExempt': False, 'timestamp': 1540238395040}], 'systemEvent': {'systemEvent': 'C', 'timestamp': 1540242600000}}
#resp = requests.get(base_url + '/ref-data/symbols')
#resp = requests.get(base_url + '/stock/aapl/batch?types=quote,news,chart&range=1m&last=1')
#resp = requests.get(base_url + '/stock/market/batch?symbols=aapl,fb,tsla&types=quote,news,chart&range=1m&last=5')
#resp = requests.get(base_url + '/stock/aapl/book')
resp = requests.get(base_url + '/stock/aapl/chart')
resp = requests.get(base_url + '/stock/aapl/chart/5y')
resp = requests.get(base_url + '/stock/aapl/chart/2y')
resp = requests.get(base_url + '/stock/aapl/chart/1y')
resp = requests.get(base_url + '/stock/aapl/chart/ytd')
resp = requests.get(base_url + '/stock/aapl/chart/6m')
resp = requests.get(base_url + '/stock/aapl/chart/3m')
resp = requests.get(base_url + '/stock/aapl/chart/1m')
resp = requests.get(base_url + '/stock/aapl/chart/1d')
resp = requests.get(base_url + '/stock/aapl/chart/date/20181022')
resp = requests.get(base_url + '/stock/aapl/chart/6m')
if resp.status_code == requests.codes.ok:
    print(resp.json())