#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRecycleInstshopQrcodeConsultModel(object):

    def __init__(self):
        self._alipay_shop_id = None
        self._service_code = None

    @property
    def alipay_shop_id(self):
        return self._alipay_shop_id

    @alipay_shop_id.setter
    def alipay_shop_id(self, value):
        self._alipay_shop_id = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_shop_id:
            if hasattr(self.alipay_shop_id, 'to_alipay_dict'):
                params['alipay_shop_id'] = self.alipay_shop_id.to_alipay_dict()
            else:
                params['alipay_shop_id'] = self.alipay_shop_id
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleInstshopQrcodeConsultModel()
        if 'alipay_shop_id' in d:
            o.alipay_shop_id = d['alipay_shop_id']
        if 'service_code' in d:
            o.service_code = d['service_code']
        return o


