#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePromoterRelationDeleteModel(object):

    def __init__(self):
        self._merchant_pid = None
        self._promoter_id = None
        self._shop_id = None

    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def promoter_id(self):
        return self._promoter_id

    @promoter_id.setter
    def promoter_id(self, value):
        self._promoter_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.promoter_id:
            if hasattr(self.promoter_id, 'to_alipay_dict'):
                params['promoter_id'] = self.promoter_id.to_alipay_dict()
            else:
                params['promoter_id'] = self.promoter_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePromoterRelationDeleteModel()
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'promoter_id' in d:
            o.promoter_id = d['promoter_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


