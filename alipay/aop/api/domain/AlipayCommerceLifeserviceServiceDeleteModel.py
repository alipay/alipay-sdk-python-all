#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceServiceDeleteModel(object):

    def __init__(self):
        self._out_service_id = None
        self._service_id = None
        self._shop_id = None

    @property
    def out_service_id(self):
        return self._out_service_id

    @out_service_id.setter
    def out_service_id(self, value):
        self._out_service_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_service_id:
            if hasattr(self.out_service_id, 'to_alipay_dict'):
                params['out_service_id'] = self.out_service_id.to_alipay_dict()
            else:
                params['out_service_id'] = self.out_service_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
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
        o = AlipayCommerceLifeserviceServiceDeleteModel()
        if 'out_service_id' in d:
            o.out_service_id = d['out_service_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


