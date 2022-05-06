#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MarketingPartner(object):

    def __init__(self):
        self._industry_plan_id = None
        self._merchant_id = None
        self._mini_app_id = None
        self._type = None

    @property
    def industry_plan_id(self):
        return self._industry_plan_id

    @industry_plan_id.setter
    def industry_plan_id(self, value):
        self._industry_plan_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.industry_plan_id:
            if hasattr(self.industry_plan_id, 'to_alipay_dict'):
                params['industry_plan_id'] = self.industry_plan_id.to_alipay_dict()
            else:
                params['industry_plan_id'] = self.industry_plan_id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MarketingPartner()
        if 'industry_plan_id' in d:
            o.industry_plan_id = d['industry_plan_id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'type' in d:
            o.type = d['type']
        return o


