#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditPayClauseVO(object):

    def __init__(self):
        self._contract_key = None
        self._contract_name = None
        self._contract_url = None

    @property
    def contract_key(self):
        return self._contract_key

    @contract_key.setter
    def contract_key(self, value):
        self._contract_key = value
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def contract_url(self):
        return self._contract_url

    @contract_url.setter
    def contract_url(self, value):
        self._contract_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_key:
            if hasattr(self.contract_key, 'to_alipay_dict'):
                params['contract_key'] = self.contract_key.to_alipay_dict()
            else:
                params['contract_key'] = self.contract_key
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.contract_url:
            if hasattr(self.contract_url, 'to_alipay_dict'):
                params['contract_url'] = self.contract_url.to_alipay_dict()
            else:
                params['contract_url'] = self.contract_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPayClauseVO()
        if 'contract_key' in d:
            o.contract_key = d['contract_key']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'contract_url' in d:
            o.contract_url = d['contract_url']
        return o


