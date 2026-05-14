#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpIndustryModelClasses import EpIndustryModelClasses
from alipay.aop.api.domain.ZmEpRegistrationPlaceInfoClasses import ZmEpRegistrationPlaceInfoClasses
from alipay.aop.api.domain.EpStockInfoClasses import EpStockInfoClasses
from alipay.aop.api.domain.FileInfoClasses import FileInfoClasses


class SiteInfoClasses(object):

    def __init__(self):
        self._address = None
        self._approval_date = None
        self._build_date = None
        self._business_period_from = None
        self._business_period_to = None
        self._cancellation_date = None
        self._chief_representative = None
        self._email = None
        self._enterprise_name = None
        self._executing_partner = None
        self._executive_partner = None
        self._frdb = None
        self._grade_a_taxpayer_evaluation_year = None
        self._incoming_gov_office = None
        self._industry_model = None
        self._investors = None
        self._legal_representative = None
        self._legal_representative_or_pe = None
        self._modified_time = None
        self._old_name = None
        self._operating_address = None
        self._operating_scope = None
        self._operator = None
        self._phone = None
        self._principal = None
        self._province_or_city = None
        self._registe_organ = None
        self._register_status = None
        self._registr_id = None
        self._registration_capital = None
        self._registration_place = None
        self._representative_of_partner = None
        self._revocation_date = None
        self._sanitized_name = None
        self._sent_company_name = None
        self._shanghai_shenzhen_stock_list = None
        self._site_info_abbreviation = None
        self._site_info_business_location = None
        self._site_info_enterprise_cert_file_list = None
        self._site_info_id = None
        self._site_info_name = None
        self._site_info_title = None
        self._standardized_name = None
        self._type = None
        self._type_code = None
        self._tyshxydm = None
        self._zczbbz = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def approval_date(self):
        return self._approval_date

    @approval_date.setter
    def approval_date(self, value):
        self._approval_date = value
    @property
    def build_date(self):
        return self._build_date

    @build_date.setter
    def build_date(self, value):
        self._build_date = value
    @property
    def business_period_from(self):
        return self._business_period_from

    @business_period_from.setter
    def business_period_from(self, value):
        self._business_period_from = value
    @property
    def business_period_to(self):
        return self._business_period_to

    @business_period_to.setter
    def business_period_to(self, value):
        self._business_period_to = value
    @property
    def cancellation_date(self):
        return self._cancellation_date

    @cancellation_date.setter
    def cancellation_date(self, value):
        self._cancellation_date = value
    @property
    def chief_representative(self):
        return self._chief_representative

    @chief_representative.setter
    def chief_representative(self, value):
        self._chief_representative = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def executing_partner(self):
        return self._executing_partner

    @executing_partner.setter
    def executing_partner(self, value):
        self._executing_partner = value
    @property
    def executive_partner(self):
        return self._executive_partner

    @executive_partner.setter
    def executive_partner(self, value):
        self._executive_partner = value
    @property
    def frdb(self):
        return self._frdb

    @frdb.setter
    def frdb(self, value):
        self._frdb = value
    @property
    def grade_a_taxpayer_evaluation_year(self):
        return self._grade_a_taxpayer_evaluation_year

    @grade_a_taxpayer_evaluation_year.setter
    def grade_a_taxpayer_evaluation_year(self, value):
        if isinstance(value, list):
            self._grade_a_taxpayer_evaluation_year = list()
            for i in value:
                self._grade_a_taxpayer_evaluation_year.append(i)
    @property
    def incoming_gov_office(self):
        return self._incoming_gov_office

    @incoming_gov_office.setter
    def incoming_gov_office(self, value):
        self._incoming_gov_office = value
    @property
    def industry_model(self):
        return self._industry_model

    @industry_model.setter
    def industry_model(self, value):
        if isinstance(value, EpIndustryModelClasses):
            self._industry_model = value
        else:
            self._industry_model = EpIndustryModelClasses.from_alipay_dict(value)
    @property
    def investors(self):
        return self._investors

    @investors.setter
    def investors(self, value):
        self._investors = value
    @property
    def legal_representative(self):
        return self._legal_representative

    @legal_representative.setter
    def legal_representative(self, value):
        self._legal_representative = value
    @property
    def legal_representative_or_pe(self):
        return self._legal_representative_or_pe

    @legal_representative_or_pe.setter
    def legal_representative_or_pe(self, value):
        self._legal_representative_or_pe = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def old_name(self):
        return self._old_name

    @old_name.setter
    def old_name(self, value):
        self._old_name = value
    @property
    def operating_address(self):
        return self._operating_address

    @operating_address.setter
    def operating_address(self, value):
        self._operating_address = value
    @property
    def operating_scope(self):
        return self._operating_scope

    @operating_scope.setter
    def operating_scope(self, value):
        self._operating_scope = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value
    @property
    def province_or_city(self):
        return self._province_or_city

    @province_or_city.setter
    def province_or_city(self, value):
        self._province_or_city = value
    @property
    def registe_organ(self):
        return self._registe_organ

    @registe_organ.setter
    def registe_organ(self, value):
        self._registe_organ = value
    @property
    def register_status(self):
        return self._register_status

    @register_status.setter
    def register_status(self, value):
        self._register_status = value
    @property
    def registr_id(self):
        return self._registr_id

    @registr_id.setter
    def registr_id(self, value):
        self._registr_id = value
    @property
    def registration_capital(self):
        return self._registration_capital

    @registration_capital.setter
    def registration_capital(self, value):
        self._registration_capital = value
    @property
    def registration_place(self):
        return self._registration_place

    @registration_place.setter
    def registration_place(self, value):
        if isinstance(value, ZmEpRegistrationPlaceInfoClasses):
            self._registration_place = value
        else:
            self._registration_place = ZmEpRegistrationPlaceInfoClasses.from_alipay_dict(value)
    @property
    def representative_of_partner(self):
        return self._representative_of_partner

    @representative_of_partner.setter
    def representative_of_partner(self, value):
        self._representative_of_partner = value
    @property
    def revocation_date(self):
        return self._revocation_date

    @revocation_date.setter
    def revocation_date(self, value):
        self._revocation_date = value
    @property
    def sanitized_name(self):
        return self._sanitized_name

    @sanitized_name.setter
    def sanitized_name(self, value):
        self._sanitized_name = value
    @property
    def sent_company_name(self):
        return self._sent_company_name

    @sent_company_name.setter
    def sent_company_name(self, value):
        self._sent_company_name = value
    @property
    def shanghai_shenzhen_stock_list(self):
        return self._shanghai_shenzhen_stock_list

    @shanghai_shenzhen_stock_list.setter
    def shanghai_shenzhen_stock_list(self, value):
        if isinstance(value, list):
            self._shanghai_shenzhen_stock_list = list()
            for i in value:
                if isinstance(i, EpStockInfoClasses):
                    self._shanghai_shenzhen_stock_list.append(i)
                else:
                    self._shanghai_shenzhen_stock_list.append(EpStockInfoClasses.from_alipay_dict(i))
    @property
    def site_info_abbreviation(self):
        return self._site_info_abbreviation

    @site_info_abbreviation.setter
    def site_info_abbreviation(self, value):
        self._site_info_abbreviation = value
    @property
    def site_info_business_location(self):
        return self._site_info_business_location

    @site_info_business_location.setter
    def site_info_business_location(self, value):
        self._site_info_business_location = value
    @property
    def site_info_enterprise_cert_file_list(self):
        return self._site_info_enterprise_cert_file_list

    @site_info_enterprise_cert_file_list.setter
    def site_info_enterprise_cert_file_list(self, value):
        if isinstance(value, list):
            self._site_info_enterprise_cert_file_list = list()
            for i in value:
                if isinstance(i, FileInfoClasses):
                    self._site_info_enterprise_cert_file_list.append(i)
                else:
                    self._site_info_enterprise_cert_file_list.append(FileInfoClasses.from_alipay_dict(i))
    @property
    def site_info_id(self):
        return self._site_info_id

    @site_info_id.setter
    def site_info_id(self, value):
        self._site_info_id = value
    @property
    def site_info_name(self):
        return self._site_info_name

    @site_info_name.setter
    def site_info_name(self, value):
        self._site_info_name = value
    @property
    def site_info_title(self):
        return self._site_info_title

    @site_info_title.setter
    def site_info_title(self, value):
        self._site_info_title = value
    @property
    def standardized_name(self):
        return self._standardized_name

    @standardized_name.setter
    def standardized_name(self, value):
        self._standardized_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def type_code(self):
        return self._type_code

    @type_code.setter
    def type_code(self, value):
        self._type_code = value
    @property
    def tyshxydm(self):
        return self._tyshxydm

    @tyshxydm.setter
    def tyshxydm(self, value):
        self._tyshxydm = value
    @property
    def zczbbz(self):
        return self._zczbbz

    @zczbbz.setter
    def zczbbz(self, value):
        self._zczbbz = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.approval_date:
            if hasattr(self.approval_date, 'to_alipay_dict'):
                params['approval_date'] = self.approval_date.to_alipay_dict()
            else:
                params['approval_date'] = self.approval_date
        if self.build_date:
            if hasattr(self.build_date, 'to_alipay_dict'):
                params['build_date'] = self.build_date.to_alipay_dict()
            else:
                params['build_date'] = self.build_date
        if self.business_period_from:
            if hasattr(self.business_period_from, 'to_alipay_dict'):
                params['business_period_from'] = self.business_period_from.to_alipay_dict()
            else:
                params['business_period_from'] = self.business_period_from
        if self.business_period_to:
            if hasattr(self.business_period_to, 'to_alipay_dict'):
                params['business_period_to'] = self.business_period_to.to_alipay_dict()
            else:
                params['business_period_to'] = self.business_period_to
        if self.cancellation_date:
            if hasattr(self.cancellation_date, 'to_alipay_dict'):
                params['cancellation_date'] = self.cancellation_date.to_alipay_dict()
            else:
                params['cancellation_date'] = self.cancellation_date
        if self.chief_representative:
            if hasattr(self.chief_representative, 'to_alipay_dict'):
                params['chief_representative'] = self.chief_representative.to_alipay_dict()
            else:
                params['chief_representative'] = self.chief_representative
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.executing_partner:
            if hasattr(self.executing_partner, 'to_alipay_dict'):
                params['executing_partner'] = self.executing_partner.to_alipay_dict()
            else:
                params['executing_partner'] = self.executing_partner
        if self.executive_partner:
            if hasattr(self.executive_partner, 'to_alipay_dict'):
                params['executive_partner'] = self.executive_partner.to_alipay_dict()
            else:
                params['executive_partner'] = self.executive_partner
        if self.frdb:
            if hasattr(self.frdb, 'to_alipay_dict'):
                params['frdb'] = self.frdb.to_alipay_dict()
            else:
                params['frdb'] = self.frdb
        if self.grade_a_taxpayer_evaluation_year:
            if isinstance(self.grade_a_taxpayer_evaluation_year, list):
                for i in range(0, len(self.grade_a_taxpayer_evaluation_year)):
                    element = self.grade_a_taxpayer_evaluation_year[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.grade_a_taxpayer_evaluation_year[i] = element.to_alipay_dict()
            if hasattr(self.grade_a_taxpayer_evaluation_year, 'to_alipay_dict'):
                params['grade_a_taxpayer_evaluation_year'] = self.grade_a_taxpayer_evaluation_year.to_alipay_dict()
            else:
                params['grade_a_taxpayer_evaluation_year'] = self.grade_a_taxpayer_evaluation_year
        if self.incoming_gov_office:
            if hasattr(self.incoming_gov_office, 'to_alipay_dict'):
                params['incoming_gov_office'] = self.incoming_gov_office.to_alipay_dict()
            else:
                params['incoming_gov_office'] = self.incoming_gov_office
        if self.industry_model:
            if hasattr(self.industry_model, 'to_alipay_dict'):
                params['industry_model'] = self.industry_model.to_alipay_dict()
            else:
                params['industry_model'] = self.industry_model
        if self.investors:
            if hasattr(self.investors, 'to_alipay_dict'):
                params['investors'] = self.investors.to_alipay_dict()
            else:
                params['investors'] = self.investors
        if self.legal_representative:
            if hasattr(self.legal_representative, 'to_alipay_dict'):
                params['legal_representative'] = self.legal_representative.to_alipay_dict()
            else:
                params['legal_representative'] = self.legal_representative
        if self.legal_representative_or_pe:
            if hasattr(self.legal_representative_or_pe, 'to_alipay_dict'):
                params['legal_representative_or_pe'] = self.legal_representative_or_pe.to_alipay_dict()
            else:
                params['legal_representative_or_pe'] = self.legal_representative_or_pe
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.old_name:
            if hasattr(self.old_name, 'to_alipay_dict'):
                params['old_name'] = self.old_name.to_alipay_dict()
            else:
                params['old_name'] = self.old_name
        if self.operating_address:
            if hasattr(self.operating_address, 'to_alipay_dict'):
                params['operating_address'] = self.operating_address.to_alipay_dict()
            else:
                params['operating_address'] = self.operating_address
        if self.operating_scope:
            if hasattr(self.operating_scope, 'to_alipay_dict'):
                params['operating_scope'] = self.operating_scope.to_alipay_dict()
            else:
                params['operating_scope'] = self.operating_scope
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        if self.province_or_city:
            if hasattr(self.province_or_city, 'to_alipay_dict'):
                params['province_or_city'] = self.province_or_city.to_alipay_dict()
            else:
                params['province_or_city'] = self.province_or_city
        if self.registe_organ:
            if hasattr(self.registe_organ, 'to_alipay_dict'):
                params['registe_organ'] = self.registe_organ.to_alipay_dict()
            else:
                params['registe_organ'] = self.registe_organ
        if self.register_status:
            if hasattr(self.register_status, 'to_alipay_dict'):
                params['register_status'] = self.register_status.to_alipay_dict()
            else:
                params['register_status'] = self.register_status
        if self.registr_id:
            if hasattr(self.registr_id, 'to_alipay_dict'):
                params['registr_id'] = self.registr_id.to_alipay_dict()
            else:
                params['registr_id'] = self.registr_id
        if self.registration_capital:
            if hasattr(self.registration_capital, 'to_alipay_dict'):
                params['registration_capital'] = self.registration_capital.to_alipay_dict()
            else:
                params['registration_capital'] = self.registration_capital
        if self.registration_place:
            if hasattr(self.registration_place, 'to_alipay_dict'):
                params['registration_place'] = self.registration_place.to_alipay_dict()
            else:
                params['registration_place'] = self.registration_place
        if self.representative_of_partner:
            if hasattr(self.representative_of_partner, 'to_alipay_dict'):
                params['representative_of_partner'] = self.representative_of_partner.to_alipay_dict()
            else:
                params['representative_of_partner'] = self.representative_of_partner
        if self.revocation_date:
            if hasattr(self.revocation_date, 'to_alipay_dict'):
                params['revocation_date'] = self.revocation_date.to_alipay_dict()
            else:
                params['revocation_date'] = self.revocation_date
        if self.sanitized_name:
            if hasattr(self.sanitized_name, 'to_alipay_dict'):
                params['sanitized_name'] = self.sanitized_name.to_alipay_dict()
            else:
                params['sanitized_name'] = self.sanitized_name
        if self.sent_company_name:
            if hasattr(self.sent_company_name, 'to_alipay_dict'):
                params['sent_company_name'] = self.sent_company_name.to_alipay_dict()
            else:
                params['sent_company_name'] = self.sent_company_name
        if self.shanghai_shenzhen_stock_list:
            if isinstance(self.shanghai_shenzhen_stock_list, list):
                for i in range(0, len(self.shanghai_shenzhen_stock_list)):
                    element = self.shanghai_shenzhen_stock_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shanghai_shenzhen_stock_list[i] = element.to_alipay_dict()
            if hasattr(self.shanghai_shenzhen_stock_list, 'to_alipay_dict'):
                params['shanghai_shenzhen_stock_list'] = self.shanghai_shenzhen_stock_list.to_alipay_dict()
            else:
                params['shanghai_shenzhen_stock_list'] = self.shanghai_shenzhen_stock_list
        if self.site_info_abbreviation:
            if hasattr(self.site_info_abbreviation, 'to_alipay_dict'):
                params['site_info_abbreviation'] = self.site_info_abbreviation.to_alipay_dict()
            else:
                params['site_info_abbreviation'] = self.site_info_abbreviation
        if self.site_info_business_location:
            if hasattr(self.site_info_business_location, 'to_alipay_dict'):
                params['site_info_business_location'] = self.site_info_business_location.to_alipay_dict()
            else:
                params['site_info_business_location'] = self.site_info_business_location
        if self.site_info_enterprise_cert_file_list:
            if isinstance(self.site_info_enterprise_cert_file_list, list):
                for i in range(0, len(self.site_info_enterprise_cert_file_list)):
                    element = self.site_info_enterprise_cert_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.site_info_enterprise_cert_file_list[i] = element.to_alipay_dict()
            if hasattr(self.site_info_enterprise_cert_file_list, 'to_alipay_dict'):
                params['site_info_enterprise_cert_file_list'] = self.site_info_enterprise_cert_file_list.to_alipay_dict()
            else:
                params['site_info_enterprise_cert_file_list'] = self.site_info_enterprise_cert_file_list
        if self.site_info_id:
            if hasattr(self.site_info_id, 'to_alipay_dict'):
                params['site_info_id'] = self.site_info_id.to_alipay_dict()
            else:
                params['site_info_id'] = self.site_info_id
        if self.site_info_name:
            if hasattr(self.site_info_name, 'to_alipay_dict'):
                params['site_info_name'] = self.site_info_name.to_alipay_dict()
            else:
                params['site_info_name'] = self.site_info_name
        if self.site_info_title:
            if hasattr(self.site_info_title, 'to_alipay_dict'):
                params['site_info_title'] = self.site_info_title.to_alipay_dict()
            else:
                params['site_info_title'] = self.site_info_title
        if self.standardized_name:
            if hasattr(self.standardized_name, 'to_alipay_dict'):
                params['standardized_name'] = self.standardized_name.to_alipay_dict()
            else:
                params['standardized_name'] = self.standardized_name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.type_code:
            if hasattr(self.type_code, 'to_alipay_dict'):
                params['type_code'] = self.type_code.to_alipay_dict()
            else:
                params['type_code'] = self.type_code
        if self.tyshxydm:
            if hasattr(self.tyshxydm, 'to_alipay_dict'):
                params['tyshxydm'] = self.tyshxydm.to_alipay_dict()
            else:
                params['tyshxydm'] = self.tyshxydm
        if self.zczbbz:
            if hasattr(self.zczbbz, 'to_alipay_dict'):
                params['zczbbz'] = self.zczbbz.to_alipay_dict()
            else:
                params['zczbbz'] = self.zczbbz
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SiteInfoClasses()
        if 'address' in d:
            o.address = d['address']
        if 'approval_date' in d:
            o.approval_date = d['approval_date']
        if 'build_date' in d:
            o.build_date = d['build_date']
        if 'business_period_from' in d:
            o.business_period_from = d['business_period_from']
        if 'business_period_to' in d:
            o.business_period_to = d['business_period_to']
        if 'cancellation_date' in d:
            o.cancellation_date = d['cancellation_date']
        if 'chief_representative' in d:
            o.chief_representative = d['chief_representative']
        if 'email' in d:
            o.email = d['email']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'executing_partner' in d:
            o.executing_partner = d['executing_partner']
        if 'executive_partner' in d:
            o.executive_partner = d['executive_partner']
        if 'frdb' in d:
            o.frdb = d['frdb']
        if 'grade_a_taxpayer_evaluation_year' in d:
            o.grade_a_taxpayer_evaluation_year = d['grade_a_taxpayer_evaluation_year']
        if 'incoming_gov_office' in d:
            o.incoming_gov_office = d['incoming_gov_office']
        if 'industry_model' in d:
            o.industry_model = d['industry_model']
        if 'investors' in d:
            o.investors = d['investors']
        if 'legal_representative' in d:
            o.legal_representative = d['legal_representative']
        if 'legal_representative_or_pe' in d:
            o.legal_representative_or_pe = d['legal_representative_or_pe']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'old_name' in d:
            o.old_name = d['old_name']
        if 'operating_address' in d:
            o.operating_address = d['operating_address']
        if 'operating_scope' in d:
            o.operating_scope = d['operating_scope']
        if 'operator' in d:
            o.operator = d['operator']
        if 'phone' in d:
            o.phone = d['phone']
        if 'principal' in d:
            o.principal = d['principal']
        if 'province_or_city' in d:
            o.province_or_city = d['province_or_city']
        if 'registe_organ' in d:
            o.registe_organ = d['registe_organ']
        if 'register_status' in d:
            o.register_status = d['register_status']
        if 'registr_id' in d:
            o.registr_id = d['registr_id']
        if 'registration_capital' in d:
            o.registration_capital = d['registration_capital']
        if 'registration_place' in d:
            o.registration_place = d['registration_place']
        if 'representative_of_partner' in d:
            o.representative_of_partner = d['representative_of_partner']
        if 'revocation_date' in d:
            o.revocation_date = d['revocation_date']
        if 'sanitized_name' in d:
            o.sanitized_name = d['sanitized_name']
        if 'sent_company_name' in d:
            o.sent_company_name = d['sent_company_name']
        if 'shanghai_shenzhen_stock_list' in d:
            o.shanghai_shenzhen_stock_list = d['shanghai_shenzhen_stock_list']
        if 'site_info_abbreviation' in d:
            o.site_info_abbreviation = d['site_info_abbreviation']
        if 'site_info_business_location' in d:
            o.site_info_business_location = d['site_info_business_location']
        if 'site_info_enterprise_cert_file_list' in d:
            o.site_info_enterprise_cert_file_list = d['site_info_enterprise_cert_file_list']
        if 'site_info_id' in d:
            o.site_info_id = d['site_info_id']
        if 'site_info_name' in d:
            o.site_info_name = d['site_info_name']
        if 'site_info_title' in d:
            o.site_info_title = d['site_info_title']
        if 'standardized_name' in d:
            o.standardized_name = d['standardized_name']
        if 'type' in d:
            o.type = d['type']
        if 'type_code' in d:
            o.type_code = d['type_code']
        if 'tyshxydm' in d:
            o.tyshxydm = d['tyshxydm']
        if 'zczbbz' in d:
            o.zczbbz = d['zczbbz']
        return o


