#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalStoreDeliveryDeleteModel(object):

    def __init__(self):
        self._app_delivery_code = None
        self._store_code = None

    @property
    def app_delivery_code(self):
        return self._app_delivery_code

    @app_delivery_code.setter
    def app_delivery_code(self, value):
        self._app_delivery_code = value
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_delivery_code:
            if hasattr(self.app_delivery_code, 'to_alipay_dict'):
                params['app_delivery_code'] = self.app_delivery_code.to_alipay_dict()
            else:
                params['app_delivery_code'] = self.app_delivery_code
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalStoreDeliveryDeleteModel()
        if 'app_delivery_code' in d:
            o.app_delivery_code = d['app_delivery_code']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


