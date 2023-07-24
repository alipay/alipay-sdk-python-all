#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccountDTO(object):

    def __init__(self):
        self._account_name = None
        self._account_no = None
        self._inst_id = None
        self._offical_name = None
        self._offical_number = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def offical_name(self):
        return self._offical_name

    @offical_name.setter
    def offical_name(self, value):
        self._offical_name = value
    @property
    def offical_number(self):
        return self._offical_number

    @offical_number.setter
    def offical_number(self, value):
        self._offical_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.offical_name:
            if hasattr(self.offical_name, 'to_alipay_dict'):
                params['offical_name'] = self.offical_name.to_alipay_dict()
            else:
                params['offical_name'] = self.offical_name
        if self.offical_number:
            if hasattr(self.offical_number, 'to_alipay_dict'):
                params['offical_number'] = self.offical_number.to_alipay_dict()
            else:
                params['offical_number'] = self.offical_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccountDTO()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'offical_name' in d:
            o.offical_name = d['offical_name']
        if 'offical_number' in d:
            o.offical_number = d['offical_number']
        return o


