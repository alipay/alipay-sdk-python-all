#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpAccountInfo(object):

    def __init__(self):
        self._account_inst_name = None
        self._account_name = None
        self._sp_account_no = None

    @property
    def account_inst_name(self):
        return self._account_inst_name

    @account_inst_name.setter
    def account_inst_name(self, value):
        self._account_inst_name = value
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def sp_account_no(self):
        return self._sp_account_no

    @sp_account_no.setter
    def sp_account_no(self, value):
        self._sp_account_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_inst_name:
            if hasattr(self.account_inst_name, 'to_alipay_dict'):
                params['account_inst_name'] = self.account_inst_name.to_alipay_dict()
            else:
                params['account_inst_name'] = self.account_inst_name
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.sp_account_no:
            if hasattr(self.sp_account_no, 'to_alipay_dict'):
                params['sp_account_no'] = self.sp_account_no.to_alipay_dict()
            else:
                params['sp_account_no'] = self.sp_account_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpAccountInfo()
        if 'account_inst_name' in d:
            o.account_inst_name = d['account_inst_name']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'sp_account_no' in d:
            o.sp_account_no = d['sp_account_no']
        return o


