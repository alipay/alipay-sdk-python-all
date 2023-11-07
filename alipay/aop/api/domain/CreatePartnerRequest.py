#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreatePartnerRequest(object):

    def __init__(self):
        self._bd = None
        self._certificate_number = None
        self._certificate_valid_date = None
        self._charge_person_name = None
        self._country = None
        self._creator = None
        self._ep_cert_no = None
        self._ep_name = None
        self._ep_reg_no = None
        self._ep_status = None
        self._ep_type = None
        self._established_date = None
        self._industry = None
        self._industry_category = None
        self._location = None
        self._memo = None
        self._partner_channel_type = None
        self._partner_type_list = None
        self._pid = None
        self._region = None
        self._registered_address = None
        self._registered_capital = None
        self._risk_warning = None
        self._social_security_account = None

    @property
    def bd(self):
        return self._bd

    @bd.setter
    def bd(self, value):
        self._bd = value
    @property
    def certificate_number(self):
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, value):
        self._certificate_number = value
    @property
    def certificate_valid_date(self):
        return self._certificate_valid_date

    @certificate_valid_date.setter
    def certificate_valid_date(self, value):
        self._certificate_valid_date = value
    @property
    def charge_person_name(self):
        return self._charge_person_name

    @charge_person_name.setter
    def charge_person_name(self, value):
        self._charge_person_name = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def ep_reg_no(self):
        return self._ep_reg_no

    @ep_reg_no.setter
    def ep_reg_no(self, value):
        self._ep_reg_no = value
    @property
    def ep_status(self):
        return self._ep_status

    @ep_status.setter
    def ep_status(self, value):
        self._ep_status = value
    @property
    def ep_type(self):
        return self._ep_type

    @ep_type.setter
    def ep_type(self, value):
        self._ep_type = value
    @property
    def established_date(self):
        return self._established_date

    @established_date.setter
    def established_date(self, value):
        self._established_date = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def industry_category(self):
        return self._industry_category

    @industry_category.setter
    def industry_category(self, value):
        self._industry_category = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def partner_channel_type(self):
        return self._partner_channel_type

    @partner_channel_type.setter
    def partner_channel_type(self, value):
        self._partner_channel_type = value
    @property
    def partner_type_list(self):
        return self._partner_type_list

    @partner_type_list.setter
    def partner_type_list(self, value):
        if isinstance(value, list):
            self._partner_type_list = list()
            for i in value:
                self._partner_type_list.append(i)
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def registered_address(self):
        return self._registered_address

    @registered_address.setter
    def registered_address(self, value):
        self._registered_address = value
    @property
    def registered_capital(self):
        return self._registered_capital

    @registered_capital.setter
    def registered_capital(self, value):
        self._registered_capital = value
    @property
    def risk_warning(self):
        return self._risk_warning

    @risk_warning.setter
    def risk_warning(self, value):
        self._risk_warning = value
    @property
    def social_security_account(self):
        return self._social_security_account

    @social_security_account.setter
    def social_security_account(self, value):
        self._social_security_account = value


    def to_alipay_dict(self):
        params = dict()
        if self.bd:
            if hasattr(self.bd, 'to_alipay_dict'):
                params['bd'] = self.bd.to_alipay_dict()
            else:
                params['bd'] = self.bd
        if self.certificate_number:
            if hasattr(self.certificate_number, 'to_alipay_dict'):
                params['certificate_number'] = self.certificate_number.to_alipay_dict()
            else:
                params['certificate_number'] = self.certificate_number
        if self.certificate_valid_date:
            if hasattr(self.certificate_valid_date, 'to_alipay_dict'):
                params['certificate_valid_date'] = self.certificate_valid_date.to_alipay_dict()
            else:
                params['certificate_valid_date'] = self.certificate_valid_date
        if self.charge_person_name:
            if hasattr(self.charge_person_name, 'to_alipay_dict'):
                params['charge_person_name'] = self.charge_person_name.to_alipay_dict()
            else:
                params['charge_person_name'] = self.charge_person_name
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.ep_reg_no:
            if hasattr(self.ep_reg_no, 'to_alipay_dict'):
                params['ep_reg_no'] = self.ep_reg_no.to_alipay_dict()
            else:
                params['ep_reg_no'] = self.ep_reg_no
        if self.ep_status:
            if hasattr(self.ep_status, 'to_alipay_dict'):
                params['ep_status'] = self.ep_status.to_alipay_dict()
            else:
                params['ep_status'] = self.ep_status
        if self.ep_type:
            if hasattr(self.ep_type, 'to_alipay_dict'):
                params['ep_type'] = self.ep_type.to_alipay_dict()
            else:
                params['ep_type'] = self.ep_type
        if self.established_date:
            if hasattr(self.established_date, 'to_alipay_dict'):
                params['established_date'] = self.established_date.to_alipay_dict()
            else:
                params['established_date'] = self.established_date
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.industry_category:
            if hasattr(self.industry_category, 'to_alipay_dict'):
                params['industry_category'] = self.industry_category.to_alipay_dict()
            else:
                params['industry_category'] = self.industry_category
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.partner_channel_type:
            if hasattr(self.partner_channel_type, 'to_alipay_dict'):
                params['partner_channel_type'] = self.partner_channel_type.to_alipay_dict()
            else:
                params['partner_channel_type'] = self.partner_channel_type
        if self.partner_type_list:
            if isinstance(self.partner_type_list, list):
                for i in range(0, len(self.partner_type_list)):
                    element = self.partner_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.partner_type_list[i] = element.to_alipay_dict()
            if hasattr(self.partner_type_list, 'to_alipay_dict'):
                params['partner_type_list'] = self.partner_type_list.to_alipay_dict()
            else:
                params['partner_type_list'] = self.partner_type_list
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.registered_address:
            if hasattr(self.registered_address, 'to_alipay_dict'):
                params['registered_address'] = self.registered_address.to_alipay_dict()
            else:
                params['registered_address'] = self.registered_address
        if self.registered_capital:
            if hasattr(self.registered_capital, 'to_alipay_dict'):
                params['registered_capital'] = self.registered_capital.to_alipay_dict()
            else:
                params['registered_capital'] = self.registered_capital
        if self.risk_warning:
            if hasattr(self.risk_warning, 'to_alipay_dict'):
                params['risk_warning'] = self.risk_warning.to_alipay_dict()
            else:
                params['risk_warning'] = self.risk_warning
        if self.social_security_account:
            if hasattr(self.social_security_account, 'to_alipay_dict'):
                params['social_security_account'] = self.social_security_account.to_alipay_dict()
            else:
                params['social_security_account'] = self.social_security_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreatePartnerRequest()
        if 'bd' in d:
            o.bd = d['bd']
        if 'certificate_number' in d:
            o.certificate_number = d['certificate_number']
        if 'certificate_valid_date' in d:
            o.certificate_valid_date = d['certificate_valid_date']
        if 'charge_person_name' in d:
            o.charge_person_name = d['charge_person_name']
        if 'country' in d:
            o.country = d['country']
        if 'creator' in d:
            o.creator = d['creator']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'ep_reg_no' in d:
            o.ep_reg_no = d['ep_reg_no']
        if 'ep_status' in d:
            o.ep_status = d['ep_status']
        if 'ep_type' in d:
            o.ep_type = d['ep_type']
        if 'established_date' in d:
            o.established_date = d['established_date']
        if 'industry' in d:
            o.industry = d['industry']
        if 'industry_category' in d:
            o.industry_category = d['industry_category']
        if 'location' in d:
            o.location = d['location']
        if 'memo' in d:
            o.memo = d['memo']
        if 'partner_channel_type' in d:
            o.partner_channel_type = d['partner_channel_type']
        if 'partner_type_list' in d:
            o.partner_type_list = d['partner_type_list']
        if 'pid' in d:
            o.pid = d['pid']
        if 'region' in d:
            o.region = d['region']
        if 'registered_address' in d:
            o.registered_address = d['registered_address']
        if 'registered_capital' in d:
            o.registered_capital = d['registered_capital']
        if 'risk_warning' in d:
            o.risk_warning = d['risk_warning']
        if 'social_security_account' in d:
            o.social_security_account = d['social_security_account']
        return o


