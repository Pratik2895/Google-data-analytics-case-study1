import pandas as pd
df=pd.concat(map(pd.read_csv,['202103-divvy-tripdata.csv','202104-divvy-tripdata.csv','202105-divvy-tripdata.csv','202106-divvy-tripdata.csv','202107-divvy-tripdata.csv','202108-divvy-tripdata.csv','202109-divvy-tripdata.csv','202110-divvy-tripdata.csv','202111-divvy-tripdata.csv'
                              ,'202112-divvy-tripdata.csv','202111-divvy-tripdata.csv','202201-divvy-tripdata.csv','202202-divvy-tripdata.csv']),ignore_index=True)

dg=df[['rideable_type','trip_duration_m','Day_of_week','member_casual']]
dg.to_csv('sample2.csv',sep='\t')

