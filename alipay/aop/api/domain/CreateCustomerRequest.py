#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreateCustomerRequest(object):

    def __init__(self):
        self._bd = None
        self._charge_person_name = None
        self._cid = None
        self._country = None
        self._creator = None
        self._customer_industry = None
        self._customer_source = None
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
        self._region = None
        self._registered_address = None
        self._registered_capital = None
        self._social_security_account = None

    @property
    def bd(self):
        return self._bd

    @bd.setter
    def bd(self, value):
        self._bd = value
    @property
    def charge_person_name(self):
        return self._charge_person_name

    @charge_person_name.setter
    def charge_person_name(self, value):
        self._charge_person_name = value
    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
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
    def customer_industry(self):
        return self._customer_industry

    @customer_industry.setter
    def customer_industry(self, value):
        self._customer_industry = value
    @property
    def customer_source(self):
        return self._customer_source

    @customer_source.setter
    def customer_source(self, value):
        self._customer_source = value
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
        if self.charge_person_name:
            if hasattr(self.charge_person_name, 'to_alipay_dict'):
                params['charge_person_name'] = self.charge_person_name.to_alipay_dict()
            else:
                params['charge_person_name'] = self.charge_person_name
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
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
        if self.customer_industry:
            if hasattr(self.customer_industry, 'to_alipay_dict'):
                params['customer_industry'] = self.customer_industry.to_alipay_dict()
            else:
                params['customer_industry'] = self.customer_industry
        if self.customer_source:
            if hasattr(self.customer_source, 'to_alipay_dict'):
                params['customer_source'] = self.customer_source.to_alipay_dict()
            else:
                params['customer_source'] = self.customer_source
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
        o = CreateCustomerRequest()
        if 'bd' in d:
            o.bd = d['bd']
        if 'charge_person_name' in d:
            o.charge_person_name = d['charge_person_name']
        if 'cid' in d:
            o.cid = d['cid']
        if 'country' in d:
            o.country = d['country']
        if 'creator' in d:
            o.creator = d['creator']
        if 'customer_industry' in d:
            o.customer_industry = d['customer_industry']
        if 'customer_source' in d:
            o.customer_source = d['customer_source']
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
        if 'region' in d:
            o.region = d['region']
        if 'registered_address' in d:
            o.registered_address = d['registered_address']
        if 'registered_capital' in d:
            o.registered_capital = d['registered_capital']
        if 'social_security_account' in d:
            o.social_security_account = d['social_security_account']
        return o


