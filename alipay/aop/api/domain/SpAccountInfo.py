#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpAccountInfo(object):

    def __init__(self):
        self._account_inst_name = None
        self._account_name = None
        self._inst_branch_name = None
        self._inst_location = None
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
    def inst_branch_name(self):
        return self._inst_branch_name

    @inst_branch_name.setter
    def inst_branch_name(self, value):
        self._inst_branch_name = value
    @property
    def inst_location(self):
        return self._inst_location

    @inst_location.setter
    def inst_location(self, value):
        self._inst_location = value
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
        if self.inst_branch_name:
            if hasattr(self.inst_branch_name, 'to_alipay_dict'):
                params['inst_branch_name'] = self.inst_branch_name.to_alipay_dict()
            else:
                params['inst_branch_name'] = self.inst_branch_name
        if self.inst_location:
            if hasattr(self.inst_location, 'to_alipay_dict'):
                params['inst_location'] = self.inst_location.to_alipay_dict()
            else:
                params['inst_location'] = self.inst_location
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
        if 'inst_branch_name' in d:
            o.inst_branch_name = d['inst_branch_name']
        if 'inst_location' in d:
            o.inst_location = d['inst_location']
        if 'sp_account_no' in d:
            o.sp_account_no = d['sp_account_no']
        return o


