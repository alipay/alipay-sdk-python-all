#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandIndirectSupplementCreateModel(object):

    def __init__(self):
        self._logo_key = None
        self._sub_merchant_id = None

    @property
    def logo_key(self):
        return self._logo_key

    @logo_key.setter
    def logo_key(self, value):
        self._logo_key = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.logo_key:
            if hasattr(self.logo_key, 'to_alipay_dict'):
                params['logo_key'] = self.logo_key.to_alipay_dict()
            else:
                params['logo_key'] = self.logo_key
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectSupplementCreateModel()
        if 'logo_key' in d:
            o.logo_key = d['logo_key']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        return o


