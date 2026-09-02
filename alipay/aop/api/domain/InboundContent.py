#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InboundContent(object):

    def __init__(self):
        self._company_cert_no = None
        self._company_name = None
        self._contact_info = None
        self._legal_person_name = None
        self._link_url = None
        self._main_business = None
        self._match_score = None
        self._name = None
        self._opportunity_analysis = None
        self._purchasing_power_rationale = None
        self._purchasing_power_score = None
        self._recommendation_rationale = None
        self._similar_companies = None
        self._similarity_rationale = None
        self._tender_budget = None
        self._tender_contact_name = None
        self._tender_deadline = None
        self._tender_publish_time = None
        self._tender_winning_amount = None
        self._tender_winning_company = None
        self._tenderee_list = None

    @property
    def company_cert_no(self):
        return self._company_cert_no

    @company_cert_no.setter
    def company_cert_no(self, value):
        self._company_cert_no = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, list):
            self._contact_info = list()
            for i in value:
                self._contact_info.append(i)
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def main_business(self):
        return self._main_business

    @main_business.setter
    def main_business(self, value):
        if isinstance(value, list):
            self._main_business = list()
            for i in value:
                self._main_business.append(i)
    @property
    def match_score(self):
        return self._match_score

    @match_score.setter
    def match_score(self, value):
        self._match_score = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def opportunity_analysis(self):
        return self._opportunity_analysis

    @opportunity_analysis.setter
    def opportunity_analysis(self, value):
        self._opportunity_analysis = value
    @property
    def purchasing_power_rationale(self):
        return self._purchasing_power_rationale

    @purchasing_power_rationale.setter
    def purchasing_power_rationale(self, value):
        self._purchasing_power_rationale = value
    @property
    def purchasing_power_score(self):
        return self._purchasing_power_score

    @purchasing_power_score.setter
    def purchasing_power_score(self, value):
        self._purchasing_power_score = value
    @property
    def recommendation_rationale(self):
        return self._recommendation_rationale

    @recommendation_rationale.setter
    def recommendation_rationale(self, value):
        self._recommendation_rationale = value
    @property
    def similar_companies(self):
        return self._similar_companies

    @similar_companies.setter
    def similar_companies(self, value):
        if isinstance(value, list):
            self._similar_companies = list()
            for i in value:
                self._similar_companies.append(i)
    @property
    def similarity_rationale(self):
        return self._similarity_rationale

    @similarity_rationale.setter
    def similarity_rationale(self, value):
        self._similarity_rationale = value
    @property
    def tender_budget(self):
        return self._tender_budget

    @tender_budget.setter
    def tender_budget(self, value):
        self._tender_budget = value
    @property
    def tender_contact_name(self):
        return self._tender_contact_name

    @tender_contact_name.setter
    def tender_contact_name(self, value):
        if isinstance(value, list):
            self._tender_contact_name = list()
            for i in value:
                self._tender_contact_name.append(i)
    @property
    def tender_deadline(self):
        return self._tender_deadline

    @tender_deadline.setter
    def tender_deadline(self, value):
        self._tender_deadline = value
    @property
    def tender_publish_time(self):
        return self._tender_publish_time

    @tender_publish_time.setter
    def tender_publish_time(self, value):
        self._tender_publish_time = value
    @property
    def tender_winning_amount(self):
        return self._tender_winning_amount

    @tender_winning_amount.setter
    def tender_winning_amount(self, value):
        self._tender_winning_amount = value
    @property
    def tender_winning_company(self):
        return self._tender_winning_company

    @tender_winning_company.setter
    def tender_winning_company(self, value):
        if isinstance(value, list):
            self._tender_winning_company = list()
            for i in value:
                self._tender_winning_company.append(i)
    @property
    def tenderee_list(self):
        return self._tenderee_list

    @tenderee_list.setter
    def tenderee_list(self, value):
        if isinstance(value, list):
            self._tenderee_list = list()
            for i in value:
                self._tenderee_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.company_cert_no:
            if hasattr(self.company_cert_no, 'to_alipay_dict'):
                params['company_cert_no'] = self.company_cert_no.to_alipay_dict()
            else:
                params['company_cert_no'] = self.company_cert_no
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.contact_info:
            if isinstance(self.contact_info, list):
                for i in range(0, len(self.contact_info)):
                    element = self.contact_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_info[i] = element.to_alipay_dict()
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.main_business:
            if isinstance(self.main_business, list):
                for i in range(0, len(self.main_business)):
                    element = self.main_business[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.main_business[i] = element.to_alipay_dict()
            if hasattr(self.main_business, 'to_alipay_dict'):
                params['main_business'] = self.main_business.to_alipay_dict()
            else:
                params['main_business'] = self.main_business
        if self.match_score:
            if hasattr(self.match_score, 'to_alipay_dict'):
                params['match_score'] = self.match_score.to_alipay_dict()
            else:
                params['match_score'] = self.match_score
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.opportunity_analysis:
            if hasattr(self.opportunity_analysis, 'to_alipay_dict'):
                params['opportunity_analysis'] = self.opportunity_analysis.to_alipay_dict()
            else:
                params['opportunity_analysis'] = self.opportunity_analysis
        if self.purchasing_power_rationale:
            if hasattr(self.purchasing_power_rationale, 'to_alipay_dict'):
                params['purchasing_power_rationale'] = self.purchasing_power_rationale.to_alipay_dict()
            else:
                params['purchasing_power_rationale'] = self.purchasing_power_rationale
        if self.purchasing_power_score:
            if hasattr(self.purchasing_power_score, 'to_alipay_dict'):
                params['purchasing_power_score'] = self.purchasing_power_score.to_alipay_dict()
            else:
                params['purchasing_power_score'] = self.purchasing_power_score
        if self.recommendation_rationale:
            if hasattr(self.recommendation_rationale, 'to_alipay_dict'):
                params['recommendation_rationale'] = self.recommendation_rationale.to_alipay_dict()
            else:
                params['recommendation_rationale'] = self.recommendation_rationale
        if self.similar_companies:
            if isinstance(self.similar_companies, list):
                for i in range(0, len(self.similar_companies)):
                    element = self.similar_companies[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.similar_companies[i] = element.to_alipay_dict()
            if hasattr(self.similar_companies, 'to_alipay_dict'):
                params['similar_companies'] = self.similar_companies.to_alipay_dict()
            else:
                params['similar_companies'] = self.similar_companies
        if self.similarity_rationale:
            if hasattr(self.similarity_rationale, 'to_alipay_dict'):
                params['similarity_rationale'] = self.similarity_rationale.to_alipay_dict()
            else:
                params['similarity_rationale'] = self.similarity_rationale
        if self.tender_budget:
            if hasattr(self.tender_budget, 'to_alipay_dict'):
                params['tender_budget'] = self.tender_budget.to_alipay_dict()
            else:
                params['tender_budget'] = self.tender_budget
        if self.tender_contact_name:
            if isinstance(self.tender_contact_name, list):
                for i in range(0, len(self.tender_contact_name)):
                    element = self.tender_contact_name[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tender_contact_name[i] = element.to_alipay_dict()
            if hasattr(self.tender_contact_name, 'to_alipay_dict'):
                params['tender_contact_name'] = self.tender_contact_name.to_alipay_dict()
            else:
                params['tender_contact_name'] = self.tender_contact_name
        if self.tender_deadline:
            if hasattr(self.tender_deadline, 'to_alipay_dict'):
                params['tender_deadline'] = self.tender_deadline.to_alipay_dict()
            else:
                params['tender_deadline'] = self.tender_deadline
        if self.tender_publish_time:
            if hasattr(self.tender_publish_time, 'to_alipay_dict'):
                params['tender_publish_time'] = self.tender_publish_time.to_alipay_dict()
            else:
                params['tender_publish_time'] = self.tender_publish_time
        if self.tender_winning_amount:
            if hasattr(self.tender_winning_amount, 'to_alipay_dict'):
                params['tender_winning_amount'] = self.tender_winning_amount.to_alipay_dict()
            else:
                params['tender_winning_amount'] = self.tender_winning_amount
        if self.tender_winning_company:
            if isinstance(self.tender_winning_company, list):
                for i in range(0, len(self.tender_winning_company)):
                    element = self.tender_winning_company[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tender_winning_company[i] = element.to_alipay_dict()
            if hasattr(self.tender_winning_company, 'to_alipay_dict'):
                params['tender_winning_company'] = self.tender_winning_company.to_alipay_dict()
            else:
                params['tender_winning_company'] = self.tender_winning_company
        if self.tenderee_list:
            if isinstance(self.tenderee_list, list):
                for i in range(0, len(self.tenderee_list)):
                    element = self.tenderee_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tenderee_list[i] = element.to_alipay_dict()
            if hasattr(self.tenderee_list, 'to_alipay_dict'):
                params['tenderee_list'] = self.tenderee_list.to_alipay_dict()
            else:
                params['tenderee_list'] = self.tenderee_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InboundContent()
        if 'company_cert_no' in d:
            o.company_cert_no = d['company_cert_no']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'main_business' in d:
            o.main_business = d['main_business']
        if 'match_score' in d:
            o.match_score = d['match_score']
        if 'name' in d:
            o.name = d['name']
        if 'opportunity_analysis' in d:
            o.opportunity_analysis = d['opportunity_analysis']
        if 'purchasing_power_rationale' in d:
            o.purchasing_power_rationale = d['purchasing_power_rationale']
        if 'purchasing_power_score' in d:
            o.purchasing_power_score = d['purchasing_power_score']
        if 'recommendation_rationale' in d:
            o.recommendation_rationale = d['recommendation_rationale']
        if 'similar_companies' in d:
            o.similar_companies = d['similar_companies']
        if 'similarity_rationale' in d:
            o.similarity_rationale = d['similarity_rationale']
        if 'tender_budget' in d:
            o.tender_budget = d['tender_budget']
        if 'tender_contact_name' in d:
            o.tender_contact_name = d['tender_contact_name']
        if 'tender_deadline' in d:
            o.tender_deadline = d['tender_deadline']
        if 'tender_publish_time' in d:
            o.tender_publish_time = d['tender_publish_time']
        if 'tender_winning_amount' in d:
            o.tender_winning_amount = d['tender_winning_amount']
        if 'tender_winning_company' in d:
            o.tender_winning_company = d['tender_winning_company']
        if 'tenderee_list' in d:
            o.tenderee_list = d['tenderee_list']
        return o


