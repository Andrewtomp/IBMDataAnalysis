# Series of queries using a subset of the city of Chicagos Crime, Census, and School Data for the IBM Data Analyst Course
# Census: https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2
# School: https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t
# Crime: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2

# These libraries are pre-installed in SN Labs. If running in another environment please uncomment lines below to install them:
!pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3
# Ensure we don't load_ext with sqlalchemy>=1.4 (incompadible)
!pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24
!pip install ipython-sql

%load_ext sql

# Remember the connection string is of the format:
# %sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name?security=SSL
# Enter the connection string for your Db2 on Cloud database instance below

# Data base login is left out


# Problem 1 : Find the total number of crimes recorded in the CRIME table
%sql SELECT COUNT(*) FROM CRIMEDATA 

# Problem 2: List community areas with per capita income less than 11000
%sql SELECT COMMUNITY_AREA_NAME, PER_CAPITA_INCOME FROM CENSUSDATA WHERE PER_CAPITA_INCOME < 11000

# Problem 3: List all case numbers for crimes involving minors?(children are not considered minors for the purposes of crime analysis)
%sql SELECT CASE_NUMBER,DESCRIPTION FROM CRIMEDATA WHERE DESCRIPTION LIKE '%MINOR%'

# Problem 4: List all kidnapping crimes involving a child?
%sql SELECT CASE_NUMBER,DESCRIPTION FROM CRIMEDATA WHERE DESCRIPTION LIKE '%CHILD ABDUCTION%'

# Problem 5: What kinds of crimes were recorded at schools?
%sql SELECT PRIMARY_TYPE,LOCATION_DESCRIPTION FROM CRIMEDATA WHERE LOCATION_DESCRIPTION LIKE '%SCHOOL%'

# Problem 6: List the average safety score for each type of school.
%sql SELECT "Elementary, Middle, or High School", AVG(SAFETY_SCORE) FROM SCHOOLDATA  GROUP BY "Elementary, Middle, or High School"

# Problem 7: List 5 community areas with highest % of households below poverty line
%sql SELECT COMMUNITY_AREA_NAME, PERCENT_HOUSEHOLDS_BELOW_POVERTY FROM CENSUSDATA ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC LIMIT 5 

# Problem 8: Which community area is most crime prone?
%sql SELECT CRIMEDATA.COMMUNITY_AREA_NUMBER, COUNT(CRIMEDATA.CASE_NUMBER) FROM CRIMEDATA GROUP BY CRIMEDATA.COMMUNITY_AREA_NUMBER ORDER BY COUNT(CRIMEDATA.CASE_NUMBER) DESC LIMIT 1

# Problem 9: Use a sub-query to find the name of the community area with highest hardship inde
%sql SELECT COMMUNITY_AREA_NAME, HARDSHIP_INDEX FROM CENSUSDATA WHERE HARDSHIP_INDEX = (SELECT MAX(HARDSHIP_INDEX) FROM CENSUSDATA)

# Problem 10: Use a sub-query to determine the Community Area Name with most number of crimes?
%sql SELECT COMMUNITY_AREA_NAME FROM CENSUSDATA WHERE COMMUNITY_AREA_NUMBER = (SELECT COMMUNITY_AREA_NUMBER FROM CRIMEDATA GROUP BY COMMUNITY_AREA_NUMBER ORDER BY COUNT(CRIMEDATA.CASE_NUMBER) DESC LIMIT 1) 
                                                                               




