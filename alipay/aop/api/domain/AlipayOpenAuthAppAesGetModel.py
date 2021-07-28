#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAuthAppAesGetModel(object):

    def __init__(self):
        self._merchant_app_id = None

    @property
    def merchant_app_id(self):
        return self._merchant_app_id

    @merchant_app_id.setter
    def merchant_app_id(self, value):
        self._merchant_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_app_id:
            if hasattr(self.merchant_app_id, 'to_alipay_dict'):
                params['merchant_app_id'] = self.merchant_app_id.to_alipay_dict()
            else:
                params['merchant_app_id'] = self.merchant_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthAppAesGetModel()
        if 'merchant_app_id' in d:
            o.merchant_app_id = d['merchant_app_id']
        return o


