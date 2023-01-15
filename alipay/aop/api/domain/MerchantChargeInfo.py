#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantChargeInfo(object):

    def __init__(self):
        self._certify_id = None
        self._charge_type = None
        self._error_code = None

    @property
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.certify_id:
            if hasattr(self.certify_id, 'to_alipay_dict'):
                params['certify_id'] = self.certify_id.to_alipay_dict()
            else:
                params['certify_id'] = self.certify_id
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantChargeInfo()
        if 'certify_id' in d:
            o.certify_id = d['certify_id']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'error_code' in d:
            o.error_code = d['error_code']
        return o


