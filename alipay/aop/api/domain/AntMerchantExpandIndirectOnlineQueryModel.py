#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandIndirectOnlineQueryModel(object):

    def __init__(self):
        self._external_id = None
        self._sub_merchant_id = None

    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
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
        o = AntMerchantExpandIndirectOnlineQueryModel()
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        return o


