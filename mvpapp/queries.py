from typing import Sequence

from mvpapp.models import Company, Job


def get_avg_funding_by_person(
    person_id: str
) -> int: 
    jobs = Job.objects.filter(person_id=person_id).exclude(company__isnull=True)
    number_of_jobs = Job.objects.filter(person_id=person_id).count() 

    total_funding_known = sum(job.company.known_total_funding for job in jobs)

    return total_funding_known / number_of_jobs  
    

def get_companies_by_person(
    person_id: str
) -> Sequence[str]: 
    jobs = Job.objects.filter(person_id=person_id)
    return [j.company_name for j in jobs]


def get_investors_by_company(
    company_li_name: str
) -> Sequence[str]: 
    qs = Company.objects.exclude(company_linkedin_names__isnull=True).filter(company_linkedin_names__icontains=company_li_name)
    if qs: 
        return qs[0].investors
    else:
        return [] 
    
    







