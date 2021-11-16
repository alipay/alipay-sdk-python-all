#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OneStepSignDTO(object):

    def __init__(self):
        self._biz_accept_voucher_id = None
        self._contract_code = None
        self._contract_sign_type = None
        self._sign_instant_id = None

    @property
    def biz_accept_voucher_id(self):
        return self._biz_accept_voucher_id

    @biz_accept_voucher_id.setter
    def biz_accept_voucher_id(self, value):
        self._biz_accept_voucher_id = value
    @property
    def contract_code(self):
        return self._contract_code

    @contract_code.setter
    def contract_code(self, value):
        self._contract_code = value
    @property
    def contract_sign_type(self):
        return self._contract_sign_type

    @contract_sign_type.setter
    def contract_sign_type(self, value):
        self._contract_sign_type = value
    @property
    def sign_instant_id(self):
        return self._sign_instant_id

    @sign_instant_id.setter
    def sign_instant_id(self, value):
        self._sign_instant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_accept_voucher_id:
            if hasattr(self.biz_accept_voucher_id, 'to_alipay_dict'):
                params['biz_accept_voucher_id'] = self.biz_accept_voucher_id.to_alipay_dict()
            else:
                params['biz_accept_voucher_id'] = self.biz_accept_voucher_id
        if self.contract_code:
            if hasattr(self.contract_code, 'to_alipay_dict'):
                params['contract_code'] = self.contract_code.to_alipay_dict()
            else:
                params['contract_code'] = self.contract_code
        if self.contract_sign_type:
            if hasattr(self.contract_sign_type, 'to_alipay_dict'):
                params['contract_sign_type'] = self.contract_sign_type.to_alipay_dict()
            else:
                params['contract_sign_type'] = self.contract_sign_type
        if self.sign_instant_id:
            if hasattr(self.sign_instant_id, 'to_alipay_dict'):
                params['sign_instant_id'] = self.sign_instant_id.to_alipay_dict()
            else:
                params['sign_instant_id'] = self.sign_instant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OneStepSignDTO()
        if 'biz_accept_voucher_id' in d:
            o.biz_accept_voucher_id = d['biz_accept_voucher_id']
        if 'contract_code' in d:
            o.contract_code = d['contract_code']
        if 'contract_sign_type' in d:
            o.contract_sign_type = d['contract_sign_type']
        if 'sign_instant_id' in d:
            o.sign_instant_id = d['sign_instant_id']
        return o


