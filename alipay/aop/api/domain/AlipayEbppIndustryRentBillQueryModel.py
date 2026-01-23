#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryRentBillQueryModel(object):

    def __init__(self):
        self._cert_num = None
        self._cert_type = None
        self._end_time = None
        self._enterprise_credit_no = None
        self._enterprise_name = None
        self._enterprise_proof = None
        self._org_code = None
        self._start_date = None
        self._user_name = None

    @property
    def cert_num(self):
        return self._cert_num

    @cert_num.setter
    def cert_num(self, value):
        self._cert_num = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def enterprise_credit_no(self):
        return self._enterprise_credit_no

    @enterprise_credit_no.setter
    def enterprise_credit_no(self, value):
        self._enterprise_credit_no = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def enterprise_proof(self):
        return self._enterprise_proof

    @enterprise_proof.setter
    def enterprise_proof(self, value):
        self._enterprise_proof = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_num:
            if hasattr(self.cert_num, 'to_alipay_dict'):
                params['cert_num'] = self.cert_num.to_alipay_dict()
            else:
                params['cert_num'] = self.cert_num
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.enterprise_credit_no:
            if hasattr(self.enterprise_credit_no, 'to_alipay_dict'):
                params['enterprise_credit_no'] = self.enterprise_credit_no.to_alipay_dict()
            else:
                params['enterprise_credit_no'] = self.enterprise_credit_no
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.enterprise_proof:
            if hasattr(self.enterprise_proof, 'to_alipay_dict'):
                params['enterprise_proof'] = self.enterprise_proof.to_alipay_dict()
            else:
                params['enterprise_proof'] = self.enterprise_proof
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryRentBillQueryModel()
        if 'cert_num' in d:
            o.cert_num = d['cert_num']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'enterprise_credit_no' in d:
            o.enterprise_credit_no = d['enterprise_credit_no']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'enterprise_proof' in d:
            o.enterprise_proof = d['enterprise_proof']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


