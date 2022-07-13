
## Name = chBullBearOverUnder
## Annotate chart to show various bullish and bearish candlestick patterns used in scans from following sessions
##Building Bullish Scans Part 1
##Building a Bullish Scan Part 2 Oct 1 2021


#Bullish signs in a downtrend
def IsUpDayAfterDownDay = close > open and close[1] < open[1];
#Bullish Candlestick pattern type or types
#Bullish Engulfing
def IsBE = open < close[1] and close > open[1];
AddChartBubble( IsBE and IsUpDayAfterDownDay ,close,"BE",color.Green,up=Yes);
 #Piercing Signal
def IsPL = open < close[1] and close > (open[1] + close[1] ) / 2;
AddChartBubble( IsPL and IsUpDayAfterDownDay ,close,"PL",color.Green,up=Yes);
#CAHOLD
def IsCAHOLD = close > high[1];
AddChartBubble( IsCAHOLD and IsUpDayAfterDownDay ,close,"CAHOLD",color.Green,up=Yes);

# Down yesterday and up today
Def IsDownDayAfterUpDay = close<open and close[1]>open[1];
#Bearish Candlestick pattern type or types
# Bearish Engulfing
Def IsBrE = open > close[1] and close <open[1];
AddChartBubble( IsBE and IsDownDayAfterUpDay ,close,"BrE",color.Red,up=No);
# Dark Cloud Cover
Def IsDCC = open>close[1] and close > (open[1] + close[1] )/2;
AddChartBubble( IsDCC and IsDownDayAfterUpDay ,close,"DCC",color.Red,up=No);
#CBLOHD
Def IsCBLOHD = close < low[1];  
AddChartBubble( IsCBLOHD and IsDownDayAfterUpDay ,close,"CBLOHD",color.Red,up=No);