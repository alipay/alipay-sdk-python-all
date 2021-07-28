#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantContractCommonCancelModel(object):

    def __init__(self):
        self._contract_no = None
        self._sign_principal_id = None

    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def sign_principal_id(self):
        return self._sign_principal_id

    @sign_principal_id.setter
    def sign_principal_id(self, value):
        self._sign_principal_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.sign_principal_id:
            if hasattr(self.sign_principal_id, 'to_alipay_dict'):
                params['sign_principal_id'] = self.sign_principal_id.to_alipay_dict()
            else:
                params['sign_principal_id'] = self.sign_principal_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantContractCommonCancelModel()
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'sign_principal_id' in d:
            o.sign_principal_id = d['sign_principal_id']
        return o


