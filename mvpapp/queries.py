from typing import Sequence 

from mvpapp.models import Company, Job

def get_avg_funding_by_person(
    person_id: str
) -> int: 
    # TODO: should use foreign key on job company field instead (and use related_set)
    qs = '''
        SELECT AVG(COALESCE(known_total_funding, 0)) 
        FROM mvpapp_job a
        LEFT JOIN mvpapp_company b
        ON LOWER(a.company_name) = LOWER(b.name)
        WHERE p.person_id = %s
    
    ''' % person_id
    results = Job.objects.raw(qs)

    return results[0]  
    

def get_companies_by_person(
    person_id: str
) -> Sequence[str]: 
    jobs = Job.objects.filter(person_id=person_id)
    return [j.company_name for j in jobs]


def get_investors_by_company(
    company_li_name: str
) -> Sequence[str]: 
    qs = Company.objects.exclude(company_linkedin_names__isnull=True).filter(company_linkedin_names__contains=[company_li_name])
    return [i for i in c.investors for c in qs]
    
    







