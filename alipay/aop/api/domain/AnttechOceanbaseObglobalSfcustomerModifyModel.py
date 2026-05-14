#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalSfcustomerModifyModel(object):

    def __init__(self):
        self._bd = None
        self._cid = None
        self._country = None
        self._customer_industry = None
        self._customer_short_name = None
        self._ep_cert_no = None
        self._ep_name = None
        self._operator = None
        self._region = None
        self._salesforce_region = None

    @property
    def bd(self):
        return self._bd

    @bd.setter
    def bd(self, value):
        self._bd = value
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
    def customer_industry(self):
        return self._customer_industry

    @customer_industry.setter
    def customer_industry(self, value):
        self._customer_industry = value
    @property
    def customer_short_name(self):
        return self._customer_short_name

    @customer_short_name.setter
    def customer_short_name(self, value):
        self._customer_short_name = value
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
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def salesforce_region(self):
        return self._salesforce_region

    @salesforce_region.setter
    def salesforce_region(self, value):
        self._salesforce_region = value


    def to_alipay_dict(self):
        params = dict()
        if self.bd:
            if hasattr(self.bd, 'to_alipay_dict'):
                params['bd'] = self.bd.to_alipay_dict()
            else:
                params['bd'] = self.bd
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
        if self.customer_industry:
            if hasattr(self.customer_industry, 'to_alipay_dict'):
                params['customer_industry'] = self.customer_industry.to_alipay_dict()
            else:
                params['customer_industry'] = self.customer_industry
        if self.customer_short_name:
            if hasattr(self.customer_short_name, 'to_alipay_dict'):
                params['customer_short_name'] = self.customer_short_name.to_alipay_dict()
            else:
                params['customer_short_name'] = self.customer_short_name
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
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.salesforce_region:
            if hasattr(self.salesforce_region, 'to_alipay_dict'):
                params['salesforce_region'] = self.salesforce_region.to_alipay_dict()
            else:
                params['salesforce_region'] = self.salesforce_region
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfcustomerModifyModel()
        if 'bd' in d:
            o.bd = d['bd']
        if 'cid' in d:
            o.cid = d['cid']
        if 'country' in d:
            o.country = d['country']
        if 'customer_industry' in d:
            o.customer_industry = d['customer_industry']
        if 'customer_short_name' in d:
            o.customer_short_name = d['customer_short_name']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'operator' in d:
            o.operator = d['operator']
        if 'region' in d:
            o.region = d['region']
        if 'salesforce_region' in d:
            o.salesforce_region = d['salesforce_region']
        return o


