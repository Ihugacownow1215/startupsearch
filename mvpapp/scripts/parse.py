import json

import numpy as np
import pandas as pd
from mvpapp.models import Company, Job


def parseFiles(): 
    parseCompany() 
    parseJob()
    addJobToCompanyIfCompanyExists()


def parseCompany(): 
    company_url = 'https://contrary-engineering-interview.s3.amazonaws.com/data/companies.csv'
    stg_company_nan = pd.read_csv(company_url)
    stg_company = stg_company_nan.replace(np.nan, None, regex=True)

    success_count = 0 
    failure_count = 0

    for inx in stg_company.index:
        try:
            Company.objects.update_or_create(
                name=stg_company['NAME'][inx],
                company_linkedin_names=json.loads(stg_company['COMPANY_LINKEDIN_NAMES'][inx]),
                headcount=stg_company['HEADCOUNT'][inx],
                known_total_funding=stg_company['KNOWN_TOTAL_FUNDING'][inx],  
                investors=stg_company['INVESTORS'][inx],
            )
            success_count = success_count + 1
        except Exception as e:
            print("e", e)
            failure_count = failure_count + 1

    print("success count", success_count)
    print("failure", failure_count)


def parseJob(): 
    people_url = 'https://contrary-engineering-interview.s3.amazonaws.com/data/people.csv'

    stg_people_nan = pd.read_csv(people_url)
    stg_people = stg_people_nan.where(pd.notna(stg_people_nan), None)

    success_count = 0 
    failure_count = 0

    for inx in stg_people_nan.index:
        try:
            Job.objects.update_or_create(
                person_id=stg_people['PERSON_ID'][inx],
                company_name=stg_people['COMPANY_NAME'][inx],
                company_li_name=stg_people['COMPANY_LI_NAME'][inx],
                last_title=stg_people['LAST_TITLE'][inx],
                start_date=stg_people['GROUP_START_DATE'][inx],
                end_date=stg_people['GROUP_END_DATE'][inx],  
            )
            success_count = success_count + 1
        except Exception as e:
            print(e)
            failure_count = failure_count + 1

    print("success count", success_count)
    print("failure", failure_count) 

def addJobToCompanyIfCompanyExists():
    for job in Job.objects.all(): 
        company = Company.objects.filter(name__icontains=job.company_name) 
        if company:
            job.company = company[0] 
            job.save()
            
