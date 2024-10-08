#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubMerchantModifyDTO(object):

    def __init__(self):
        self._real_merchant_id = None

    @property
    def real_merchant_id(self):
        return self._real_merchant_id

    @real_merchant_id.setter
    def real_merchant_id(self, value):
        self._real_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.real_merchant_id:
            if hasattr(self.real_merchant_id, 'to_alipay_dict'):
                params['real_merchant_id'] = self.real_merchant_id.to_alipay_dict()
            else:
                params['real_merchant_id'] = self.real_merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubMerchantModifyDTO()
        if 'real_merchant_id' in d:
            o.real_merchant_id = d['real_merchant_id']
        return o


