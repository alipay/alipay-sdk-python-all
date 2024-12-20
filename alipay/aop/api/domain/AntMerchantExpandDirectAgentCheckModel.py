#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandDirectAgentCheckModel(object):

    def __init__(self):
        self._leads_id = None
        self._merchant_account = None

    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def merchant_account(self):
        return self._merchant_account

    @merchant_account.setter
    def merchant_account(self, value):
        self._merchant_account = value


    def to_alipay_dict(self):
        params = dict()
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        if self.merchant_account:
            if hasattr(self.merchant_account, 'to_alipay_dict'):
                params['merchant_account'] = self.merchant_account.to_alipay_dict()
            else:
                params['merchant_account'] = self.merchant_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandDirectAgentCheckModel()
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'merchant_account' in d:
            o.merchant_account = d['merchant_account']
        return o


