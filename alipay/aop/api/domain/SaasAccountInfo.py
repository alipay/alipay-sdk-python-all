#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaasAccountInfo(object):

    def __init__(self):
        self._customer_id = None
        self._enterprise_registration_no = None
        self._inst_account_name = None
        self._inst_account_no = None
        self._inst_name = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def enterprise_registration_no(self):
        return self._enterprise_registration_no

    @enterprise_registration_no.setter
    def enterprise_registration_no(self, value):
        self._enterprise_registration_no = value
    @property
    def inst_account_name(self):
        return self._inst_account_name

    @inst_account_name.setter
    def inst_account_name(self, value):
        self._inst_account_name = value
    @property
    def inst_account_no(self):
        return self._inst_account_no

    @inst_account_no.setter
    def inst_account_no(self, value):
        self._inst_account_no = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.enterprise_registration_no:
            if hasattr(self.enterprise_registration_no, 'to_alipay_dict'):
                params['enterprise_registration_no'] = self.enterprise_registration_no.to_alipay_dict()
            else:
                params['enterprise_registration_no'] = self.enterprise_registration_no
        if self.inst_account_name:
            if hasattr(self.inst_account_name, 'to_alipay_dict'):
                params['inst_account_name'] = self.inst_account_name.to_alipay_dict()
            else:
                params['inst_account_name'] = self.inst_account_name
        if self.inst_account_no:
            if hasattr(self.inst_account_no, 'to_alipay_dict'):
                params['inst_account_no'] = self.inst_account_no.to_alipay_dict()
            else:
                params['inst_account_no'] = self.inst_account_no
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaasAccountInfo()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'enterprise_registration_no' in d:
            o.enterprise_registration_no = d['enterprise_registration_no']
        if 'inst_account_name' in d:
            o.inst_account_name = d['inst_account_name']
        if 'inst_account_no' in d:
            o.inst_account_no = d['inst_account_no']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        return o


