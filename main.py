import numpy as np
import matplotlib.pyplot as plt

from tools import simpleContinuousAnalytical, dailyCompound, monthlyCompound, yearlyCompound, finalProfit, marginalValue



###################### SETUP ######################

principal = 300 # Money at the start of the investment.
saving = 300 # How much money is added to the account each month.
timeEnd = 40 # How many years the computations should extend for.
r = 0.1 # Interest rate, decimal (0.1 is 10%)

###################################################

#Analytical:
times = np.arange(0,timeEnd+1,1)
analyticalSavings,times = simpleContinuousAnalytical(principal,saving,r,times)
analyticalSavings2,times = simpleContinuousAnalytical(principal,saving-150,r,times)
analyticalSavings3,times = simpleContinuousAnalytical(principal,saving+150,r,times)

#Unit Profit
unitProfit, times = finalProfit(timeEnd, times, r)
marginalValues, times = marginalValue(timeEnd, times, r)


#Numerical:
daily, timesDaily = dailyCompound(principal,saving,r,timeEnd)
monthly, timesMonthly = monthlyCompound(principal,saving,r,timeEnd)
yearly, timesYearly = yearlyCompound(principal,saving,r,timeEnd)

daily2, timesDaily = dailyCompound(principal,saving-150,r,timeEnd)
monthly2, timesMonthly = monthlyCompound(principal,saving-150,r,timeEnd)
yearly2, timesYearly = yearlyCompound(principal,saving-150,r,timeEnd)

daily3, timesDaily = dailyCompound(principal,saving+150,r,timeEnd)
monthly3, timesMonthly = monthlyCompound(principal,saving+150,r,timeEnd)
yearly3, timesYearly = yearlyCompound(principal,saving+150,r,timeEnd)

fig, ax = plt.subplots(2,2)

ax[0,0].plot(times,analyticalSavings,'r',label='Analytical solution')
ax[0,0].plot(timesDaily,daily,label='Daily compounding')
ax[0,0].plot(timesMonthly,monthly,label='Monthly compounding')
ax[0,0].plot(timesYearly,yearly,label='Yearly compounding')

ax[0,1].plot(timesYearly,yearly,label='Yearly compounding')
ax[0,1].plot(timesYearly,yearly2,'--',label='Yearly compounding, - 150€/month')
ax[0,1].plot(timesYearly,yearly3,'-.',label='Yearly compounding, + 150€/month')

ax[1,0].plot(times, unitProfit)

ax[1,1].plot(times, marginalValues)

ax[0,0].legend()
ax[0,0].set_xlim(0,timeEnd+10)
ax[0,0].grid()
ax[0,0].set_xlabel('Time (years)')
ax[0,0].set_ylabel('Money in account')

ax[0,1].legend()
ax[0,1].set_xlim(0,timeEnd+10)
ax[0,1].grid()
ax[0,1].set_xlabel('Time (years)')
ax[0,1].set_ylabel('Money in account')

ax[1,0].set_xlim(0,timeEnd+10)
ax[1,0].grid()
ax[1,0].set_xlabel('Time (years)')
ax[1,0].set_ylabel(f'Final money gained from 1€ invested at time t.')

ax[1,1].set_xlim(0,timeEnd+10)
ax[1,1].grid()
ax[1,1].set_xlabel('Time (years)')
ax[1,1].set_ylabel(f'Marginal value of 1€ at t={timeEnd} years')

plt.show()


