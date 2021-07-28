#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LoanContractInfo(object):

    def __init__(self):
        self._contract_code = None
        self._contract_end_date = None
        self._contract_name = None
        self._contract_no = None
        self._contract_oss_url = None
        self._contract_sign_date = None
        self._contract_version = None

    @property
    def contract_code(self):
        return self._contract_code

    @contract_code.setter
    def contract_code(self, value):
        self._contract_code = value
    @property
    def contract_end_date(self):
        return self._contract_end_date

    @contract_end_date.setter
    def contract_end_date(self, value):
        self._contract_end_date = value
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def contract_oss_url(self):
        return self._contract_oss_url

    @contract_oss_url.setter
    def contract_oss_url(self, value):
        self._contract_oss_url = value
    @property
    def contract_sign_date(self):
        return self._contract_sign_date

    @contract_sign_date.setter
    def contract_sign_date(self, value):
        self._contract_sign_date = value
    @property
    def contract_version(self):
        return self._contract_version

    @contract_version.setter
    def contract_version(self, value):
        self._contract_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_code:
            if hasattr(self.contract_code, 'to_alipay_dict'):
                params['contract_code'] = self.contract_code.to_alipay_dict()
            else:
                params['contract_code'] = self.contract_code
        if self.contract_end_date:
            if hasattr(self.contract_end_date, 'to_alipay_dict'):
                params['contract_end_date'] = self.contract_end_date.to_alipay_dict()
            else:
                params['contract_end_date'] = self.contract_end_date
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.contract_oss_url:
            if hasattr(self.contract_oss_url, 'to_alipay_dict'):
                params['contract_oss_url'] = self.contract_oss_url.to_alipay_dict()
            else:
                params['contract_oss_url'] = self.contract_oss_url
        if self.contract_sign_date:
            if hasattr(self.contract_sign_date, 'to_alipay_dict'):
                params['contract_sign_date'] = self.contract_sign_date.to_alipay_dict()
            else:
                params['contract_sign_date'] = self.contract_sign_date
        if self.contract_version:
            if hasattr(self.contract_version, 'to_alipay_dict'):
                params['contract_version'] = self.contract_version.to_alipay_dict()
            else:
                params['contract_version'] = self.contract_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoanContractInfo()
        if 'contract_code' in d:
            o.contract_code = d['contract_code']
        if 'contract_end_date' in d:
            o.contract_end_date = d['contract_end_date']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'contract_oss_url' in d:
            o.contract_oss_url = d['contract_oss_url']
        if 'contract_sign_date' in d:
            o.contract_sign_date = d['contract_sign_date']
        if 'contract_version' in d:
            o.contract_version = d['contract_version']
        return o


