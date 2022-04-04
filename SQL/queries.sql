/* Number of observations */
SELECT count(age)
FROM heart_failure_clinical_records_dataset


/* This displays the number of dead and not dead based on each gender */
SELECT sex,COUNT(sex)
FROM heart_failure_clinical_records_dataset
GROUP BY death_event, sex


/* Number of people with abnormal creatinine_phosphokinase*/
SELECT count(creatinine_phosphokinase)
from heart_failure_clinical_records_dataset
where NOT (creatinine_phosphokinase BETWEEN 10 AND 120)

/* Average age based on group */
SELECT sex,AVG(age)
FROM heart_failure_clinical_records_dataset
GROUP BY sex

/* Median age based on group and death */
SELECT sex,MEDIAN(age)
FROM heart_failure_clinical_records_dataset
GROUP BY sex, death_event


/* Number middle aged adults, old adults, and grandparants */
CREATE VIEW [age_distn_1] AS
SELECT 
	CASE
    	WHEN AGE BETWEEN 40 AND 50 THEN 'MIDDLE ADULT'
      	WHEN AGE BETWEEN 50 AND 70 THEN 'OLD ADULT'
      	ELSE 'GRANDPA/GRANDMA'
	END AS age_distn
FROM heart_failure_clinical_records_dataset

SELECT age_distn,COUNT(*)
FROM age_distn_1
GROUP BY age_distn

DROP VIEW age_distn_1