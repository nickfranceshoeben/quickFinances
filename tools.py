import numpy as np


def simpleContinuousAnalytical(principal,saving,r,times):
    """ Calculates money saved with the solved differential equation for the particular case where
    y' = r*y + C, where C = money added each month. It is therefore continuous, and not representative
    of how these things usually operate.
    
    If I have not been lazy, I will have included a solution of the differential equation in the repository.

    Args:
        principal (float): Starting money in the account.
        saving (float): Money added each month.
        r (float): Interest rate (yearly)
        t (np.array): Times (years)

    Returns:
        tuple: Money in account at given times, and times.
    """    
    C = saving*12
    money = np.copy(times)
    
    for t in range(len(times)):
        mt = (principal + (C/r)) * np.exp(r*times[t]) - C/r
        money[t] = mt
        
    
    return money, times

def dailyCompound(principal, saving, r, timeEnd):
    """ Calculates money saved numerically, at day resolution and compounding daily. All computations assume 365 days a year,
    and all years having the same number of days.

    Args:
        principal (float): Starting money in the account.
        saving (float): Money added each month.
        r (float): Interest rate (yearly)
        timeEnd (float): Time at the end (years). Assumed start is 0.
        
    Returns:
        tuple: Money in account at given times, and times.
    """    
    C = (saving*12)/365
    rDaily = r/365
    times = np.linspace(0,timeEnd,365*timeEnd + 1)
    money = np.copy(times)
    
    money[0] = principal
    
    for t in range(1,len(times-1)):
        
        mt = money[t-1]*rDaily + C
        money[t] = money [t-1] + mt
        
    return money, times

def monthlyCompound(principal, saving, r, timeEnd):
    """Calculates money saved numerically, at month resolution and compounding monthly. All computations assume 365 days a year,
    and all years having the same number of days.

    Args:
        principal (float): Starting money in the account.
        saving (float): Money added each month.
        r (float): Interest rate (yearly)
        timeEnd (float): Time at the end (years). Assumed start is 0.
        
    Returns:
        tuple: Money in account at given times, and times.
    """    
    C = saving
    rMonthly = r/12
    times = np.linspace(0,timeEnd,12*timeEnd + 1)
    money = np.copy(times)
    
    money[0] = principal
    
    for t in range(1,len(times-1)):
        
        mt = money[t-1]*rMonthly + C
        money[t] = money [t-1] + mt
        
    return money, times

def yearlyCompound(principal, saving, r, timeEnd):
    """Calculates money saved numerically, at year resolution and compounding yearly. All computations assume 365 days a year,
    and all years having the same number of days.

    Args:
        principal (float): Starting money in the account.
        saving (float): Money added each month.
        r (float): Interest rate (yearly)
        timeEnd (float): Time at the end (years). Assumed start is 0.
        
    Returns:
        tuple: Money in account at given times, and times.
    """    
    C = saving*12
    times = np.linspace(0,timeEnd,timeEnd+1)
    money = np.copy(times)
    
    money[0] = principal
    
    for t in range(1,len(times-1)):
        
        mt = money[t-1]*r + C
        money[t] = money [t-1] + mt
        
    return money, times

def finalProfit(timeEnd,times,r):
    """Computes the final profit made from investing a unit at time t.

    Args:
        timeEnd (float): Time at the end (years). Assumed start is 0.
        times (np.array): Times (years)
        r (float): Interest rate (yearly)

    Returns:
        tuple: Profit made, and times.
    """    
    profit = np.zeros(len(times))
    profit[0] = np.exp(r * (timeEnd)) - 1
        
    for t in range(1,len(times)-1):
        
        profit[t] = np.exp(r * (timeEnd-t)) - 1
        
    return profit, times

def marginalValue(timeEnd, times, r):
    """Computes the marginal value of investing a unit at time t.
    
    Args:
        timeEnd (float): Time at the end (years). Assumed start is 0.
        times (np.array): Times (years)
        r (float): Interest rate (yearly)

    Returns:
        tuple: Marginal value, and times.
    """    
    marginalValue = np.zeros(len(times))
    marginalValue[0] = -r * np.exp(r*timeEnd)
        
    for t in range(1,len(times)-1):
        
        marginalValue[t] = -r * np.exp(r * (timeEnd-t))
        
    return marginalValue, times
    
        
        