#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperaPersonVO import OperaPersonVO
from alipay.aop.api.domain.CorpManagerVO import CorpManagerVO
from alipay.aop.api.domain.CorpShareholderVO import CorpShareholderVO
from alipay.aop.api.domain.CurrencyVO import CurrencyVO
from alipay.aop.api.domain.PersonSimpleVO import PersonSimpleVO
from alipay.aop.api.domain.RegisteredAddressVO import RegisteredAddressVO


class CorpCompanyVO(object):

    def __init__(self):
        self._business_activities = None
        self._business_period = None
        self._company_maintainer = None
        self._company_name = None
        self._company_name_en = None
        self._company_status = None
        self._company_type = None
        self._contact_no = None
        self._corp_manager_list = None
        self._corp_shareholder_list = None
        self._country = None
        self._currency = None
        self._email = None
        self._filing_annual_return_start_date = None
        self._finance_year_settlement = None
        self._incorporation_area = None
        self._incorporation_country = None
        self._incorporation_date = None
        self._legal_person = None
        self._ou_code = None
        self._parent_company = None
        self._previous_name = None
        self._registered_address_format = None
        self._registered_office_address_en = None
        self._registration_no = None
        self._shareholders_meeting_date = None

    @property
    def business_activities(self):
        return self._business_activities

    @business_activities.setter
    def business_activities(self, value):
        self._business_activities = value
    @property
    def business_period(self):
        return self._business_period

    @business_period.setter
    def business_period(self, value):
        self._business_period = value
    @property
    def company_maintainer(self):
        return self._company_maintainer

    @company_maintainer.setter
    def company_maintainer(self, value):
        if isinstance(value, list):
            self._company_maintainer = list()
            for i in value:
                if isinstance(i, OperaPersonVO):
                    self._company_maintainer.append(i)
                else:
                    self._company_maintainer.append(OperaPersonVO.from_alipay_dict(i))
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def company_name_en(self):
        return self._company_name_en

    @company_name_en.setter
    def company_name_en(self, value):
        self._company_name_en = value
    @property
    def company_status(self):
        return self._company_status

    @company_status.setter
    def company_status(self, value):
        self._company_status = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def contact_no(self):
        return self._contact_no

    @contact_no.setter
    def contact_no(self, value):
        self._contact_no = value
    @property
    def corp_manager_list(self):
        return self._corp_manager_list

    @corp_manager_list.setter
    def corp_manager_list(self, value):
        if isinstance(value, list):
            self._corp_manager_list = list()
            for i in value:
                if isinstance(i, CorpManagerVO):
                    self._corp_manager_list.append(i)
                else:
                    self._corp_manager_list.append(CorpManagerVO.from_alipay_dict(i))
    @property
    def corp_shareholder_list(self):
        return self._corp_shareholder_list

    @corp_shareholder_list.setter
    def corp_shareholder_list(self, value):
        if isinstance(value, list):
            self._corp_shareholder_list = list()
            for i in value:
                if isinstance(i, CorpShareholderVO):
                    self._corp_shareholder_list.append(i)
                else:
                    self._corp_shareholder_list.append(CorpShareholderVO.from_alipay_dict(i))
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        if isinstance(value, list):
            self._currency = list()
            for i in value:
                if isinstance(i, CurrencyVO):
                    self._currency.append(i)
                else:
                    self._currency.append(CurrencyVO.from_alipay_dict(i))
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def filing_annual_return_start_date(self):
        return self._filing_annual_return_start_date

    @filing_annual_return_start_date.setter
    def filing_annual_return_start_date(self, value):
        self._filing_annual_return_start_date = value
    @property
    def finance_year_settlement(self):
        return self._finance_year_settlement

    @finance_year_settlement.setter
    def finance_year_settlement(self, value):
        self._finance_year_settlement = value
    @property
    def incorporation_area(self):
        return self._incorporation_area

    @incorporation_area.setter
    def incorporation_area(self, value):
        self._incorporation_area = value
    @property
    def incorporation_country(self):
        return self._incorporation_country

    @incorporation_country.setter
    def incorporation_country(self, value):
        self._incorporation_country = value
    @property
    def incorporation_date(self):
        return self._incorporation_date

    @incorporation_date.setter
    def incorporation_date(self, value):
        self._incorporation_date = value
    @property
    def legal_person(self):
        return self._legal_person

    @legal_person.setter
    def legal_person(self, value):
        if isinstance(value, PersonSimpleVO):
            self._legal_person = value
        else:
            self._legal_person = PersonSimpleVO.from_alipay_dict(value)
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def parent_company(self):
        return self._parent_company

    @parent_company.setter
    def parent_company(self, value):
        self._parent_company = value
    @property
    def previous_name(self):
        return self._previous_name

    @previous_name.setter
    def previous_name(self, value):
        self._previous_name = value
    @property
    def registered_address_format(self):
        return self._registered_address_format

    @registered_address_format.setter
    def registered_address_format(self, value):
        if isinstance(value, RegisteredAddressVO):
            self._registered_address_format = value
        else:
            self._registered_address_format = RegisteredAddressVO.from_alipay_dict(value)
    @property
    def registered_office_address_en(self):
        return self._registered_office_address_en

    @registered_office_address_en.setter
    def registered_office_address_en(self, value):
        self._registered_office_address_en = value
    @property
    def registration_no(self):
        return self._registration_no

    @registration_no.setter
    def registration_no(self, value):
        self._registration_no = value
    @property
    def shareholders_meeting_date(self):
        return self._shareholders_meeting_date

    @shareholders_meeting_date.setter
    def shareholders_meeting_date(self, value):
        self._shareholders_meeting_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_activities:
            if hasattr(self.business_activities, 'to_alipay_dict'):
                params['business_activities'] = self.business_activities.to_alipay_dict()
            else:
                params['business_activities'] = self.business_activities
        if self.business_period:
            if hasattr(self.business_period, 'to_alipay_dict'):
                params['business_period'] = self.business_period.to_alipay_dict()
            else:
                params['business_period'] = self.business_period
        if self.company_maintainer:
            if isinstance(self.company_maintainer, list):
                for i in range(0, len(self.company_maintainer)):
                    element = self.company_maintainer[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.company_maintainer[i] = element.to_alipay_dict()
            if hasattr(self.company_maintainer, 'to_alipay_dict'):
                params['company_maintainer'] = self.company_maintainer.to_alipay_dict()
            else:
                params['company_maintainer'] = self.company_maintainer
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.company_name_en:
            if hasattr(self.company_name_en, 'to_alipay_dict'):
                params['company_name_en'] = self.company_name_en.to_alipay_dict()
            else:
                params['company_name_en'] = self.company_name_en
        if self.company_status:
            if hasattr(self.company_status, 'to_alipay_dict'):
                params['company_status'] = self.company_status.to_alipay_dict()
            else:
                params['company_status'] = self.company_status
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.contact_no:
            if hasattr(self.contact_no, 'to_alipay_dict'):
                params['contact_no'] = self.contact_no.to_alipay_dict()
            else:
                params['contact_no'] = self.contact_no
        if self.corp_manager_list:
            if isinstance(self.corp_manager_list, list):
                for i in range(0, len(self.corp_manager_list)):
                    element = self.corp_manager_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.corp_manager_list[i] = element.to_alipay_dict()
            if hasattr(self.corp_manager_list, 'to_alipay_dict'):
                params['corp_manager_list'] = self.corp_manager_list.to_alipay_dict()
            else:
                params['corp_manager_list'] = self.corp_manager_list
        if self.corp_shareholder_list:
            if isinstance(self.corp_shareholder_list, list):
                for i in range(0, len(self.corp_shareholder_list)):
                    element = self.corp_shareholder_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.corp_shareholder_list[i] = element.to_alipay_dict()
            if hasattr(self.corp_shareholder_list, 'to_alipay_dict'):
                params['corp_shareholder_list'] = self.corp_shareholder_list.to_alipay_dict()
            else:
                params['corp_shareholder_list'] = self.corp_shareholder_list
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.currency:
            if isinstance(self.currency, list):
                for i in range(0, len(self.currency)):
                    element = self.currency[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.currency[i] = element.to_alipay_dict()
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.filing_annual_return_start_date:
            if hasattr(self.filing_annual_return_start_date, 'to_alipay_dict'):
                params['filing_annual_return_start_date'] = self.filing_annual_return_start_date.to_alipay_dict()
            else:
                params['filing_annual_return_start_date'] = self.filing_annual_return_start_date
        if self.finance_year_settlement:
            if hasattr(self.finance_year_settlement, 'to_alipay_dict'):
                params['finance_year_settlement'] = self.finance_year_settlement.to_alipay_dict()
            else:
                params['finance_year_settlement'] = self.finance_year_settlement
        if self.incorporation_area:
            if hasattr(self.incorporation_area, 'to_alipay_dict'):
                params['incorporation_area'] = self.incorporation_area.to_alipay_dict()
            else:
                params['incorporation_area'] = self.incorporation_area
        if self.incorporation_country:
            if hasattr(self.incorporation_country, 'to_alipay_dict'):
                params['incorporation_country'] = self.incorporation_country.to_alipay_dict()
            else:
                params['incorporation_country'] = self.incorporation_country
        if self.incorporation_date:
            if hasattr(self.incorporation_date, 'to_alipay_dict'):
                params['incorporation_date'] = self.incorporation_date.to_alipay_dict()
            else:
                params['incorporation_date'] = self.incorporation_date
        if self.legal_person:
            if hasattr(self.legal_person, 'to_alipay_dict'):
                params['legal_person'] = self.legal_person.to_alipay_dict()
            else:
                params['legal_person'] = self.legal_person
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        if self.parent_company:
            if hasattr(self.parent_company, 'to_alipay_dict'):
                params['parent_company'] = self.parent_company.to_alipay_dict()
            else:
                params['parent_company'] = self.parent_company
        if self.previous_name:
            if hasattr(self.previous_name, 'to_alipay_dict'):
                params['previous_name'] = self.previous_name.to_alipay_dict()
            else:
                params['previous_name'] = self.previous_name
        if self.registered_address_format:
            if hasattr(self.registered_address_format, 'to_alipay_dict'):
                params['registered_address_format'] = self.registered_address_format.to_alipay_dict()
            else:
                params['registered_address_format'] = self.registered_address_format
        if self.registered_office_address_en:
            if hasattr(self.registered_office_address_en, 'to_alipay_dict'):
                params['registered_office_address_en'] = self.registered_office_address_en.to_alipay_dict()
            else:
                params['registered_office_address_en'] = self.registered_office_address_en
        if self.registration_no:
            if hasattr(self.registration_no, 'to_alipay_dict'):
                params['registration_no'] = self.registration_no.to_alipay_dict()
            else:
                params['registration_no'] = self.registration_no
        if self.shareholders_meeting_date:
            if hasattr(self.shareholders_meeting_date, 'to_alipay_dict'):
                params['shareholders_meeting_date'] = self.shareholders_meeting_date.to_alipay_dict()
            else:
                params['shareholders_meeting_date'] = self.shareholders_meeting_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CorpCompanyVO()
        if 'business_activities' in d:
            o.business_activities = d['business_activities']
        if 'business_period' in d:
            o.business_period = d['business_period']
        if 'company_maintainer' in d:
            o.company_maintainer = d['company_maintainer']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'company_name_en' in d:
            o.company_name_en = d['company_name_en']
        if 'company_status' in d:
            o.company_status = d['company_status']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'contact_no' in d:
            o.contact_no = d['contact_no']
        if 'corp_manager_list' in d:
            o.corp_manager_list = d['corp_manager_list']
        if 'corp_shareholder_list' in d:
            o.corp_shareholder_list = d['corp_shareholder_list']
        if 'country' in d:
            o.country = d['country']
        if 'currency' in d:
            o.currency = d['currency']
        if 'email' in d:
            o.email = d['email']
        if 'filing_annual_return_start_date' in d:
            o.filing_annual_return_start_date = d['filing_annual_return_start_date']
        if 'finance_year_settlement' in d:
            o.finance_year_settlement = d['finance_year_settlement']
        if 'incorporation_area' in d:
            o.incorporation_area = d['incorporation_area']
        if 'incorporation_country' in d:
            o.incorporation_country = d['incorporation_country']
        if 'incorporation_date' in d:
            o.incorporation_date = d['incorporation_date']
        if 'legal_person' in d:
            o.legal_person = d['legal_person']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'parent_company' in d:
            o.parent_company = d['parent_company']
        if 'previous_name' in d:
            o.previous_name = d['previous_name']
        if 'registered_address_format' in d:
            o.registered_address_format = d['registered_address_format']
        if 'registered_office_address_en' in d:
            o.registered_office_address_en = d['registered_office_address_en']
        if 'registration_no' in d:
            o.registration_no = d['registration_no']
        if 'shareholders_meeting_date' in d:
            o.shareholders_meeting_date = d['shareholders_meeting_date']
        return o


