#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractInformationVo(object):

    def __init__(self):
        self._contract_id = None
        self._contract_period = None
        self._contract_status = None
        self._contract_title = None
        self._other_company = None
        self._other_company_location = None
        self._our_company = None
        self._our_company_name = None
        self._region = None
        self._tenant = None

    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def contract_period(self):
        return self._contract_period

    @contract_period.setter
    def contract_period(self, value):
        self._contract_period = value
    @property
    def contract_status(self):
        return self._contract_status

    @contract_status.setter
    def contract_status(self, value):
        self._contract_status = value
    @property
    def contract_title(self):
        return self._contract_title

    @contract_title.setter
    def contract_title(self, value):
        self._contract_title = value
    @property
    def other_company(self):
        return self._other_company

    @other_company.setter
    def other_company(self, value):
        self._other_company = value
    @property
    def other_company_location(self):
        return self._other_company_location

    @other_company_location.setter
    def other_company_location(self, value):
        self._other_company_location = value
    @property
    def our_company(self):
        return self._our_company

    @our_company.setter
    def our_company(self, value):
        self._our_company = value
    @property
    def our_company_name(self):
        return self._our_company_name

    @our_company_name.setter
    def our_company_name(self, value):
        self._our_company_name = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.contract_period:
            if hasattr(self.contract_period, 'to_alipay_dict'):
                params['contract_period'] = self.contract_period.to_alipay_dict()
            else:
                params['contract_period'] = self.contract_period
        if self.contract_status:
            if hasattr(self.contract_status, 'to_alipay_dict'):
                params['contract_status'] = self.contract_status.to_alipay_dict()
            else:
                params['contract_status'] = self.contract_status
        if self.contract_title:
            if hasattr(self.contract_title, 'to_alipay_dict'):
                params['contract_title'] = self.contract_title.to_alipay_dict()
            else:
                params['contract_title'] = self.contract_title
        if self.other_company:
            if hasattr(self.other_company, 'to_alipay_dict'):
                params['other_company'] = self.other_company.to_alipay_dict()
            else:
                params['other_company'] = self.other_company
        if self.other_company_location:
            if hasattr(self.other_company_location, 'to_alipay_dict'):
                params['other_company_location'] = self.other_company_location.to_alipay_dict()
            else:
                params['other_company_location'] = self.other_company_location
        if self.our_company:
            if hasattr(self.our_company, 'to_alipay_dict'):
                params['our_company'] = self.our_company.to_alipay_dict()
            else:
                params['our_company'] = self.our_company
        if self.our_company_name:
            if hasattr(self.our_company_name, 'to_alipay_dict'):
                params['our_company_name'] = self.our_company_name.to_alipay_dict()
            else:
                params['our_company_name'] = self.our_company_name
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractInformationVo()
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'contract_period' in d:
            o.contract_period = d['contract_period']
        if 'contract_status' in d:
            o.contract_status = d['contract_status']
        if 'contract_title' in d:
            o.contract_title = d['contract_title']
        if 'other_company' in d:
            o.other_company = d['other_company']
        if 'other_company_location' in d:
            o.other_company_location = d['other_company_location']
        if 'our_company' in d:
            o.our_company = d['our_company']
        if 'our_company_name' in d:
            o.our_company_name = d['our_company_name']
        if 'region' in d:
            o.region = d['region']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


