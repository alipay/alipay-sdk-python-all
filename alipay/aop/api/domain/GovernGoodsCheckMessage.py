#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GovernGoodsCheckMessage(object):

    def __init__(self):
        self._merchant_id = None
        self._need_grovern_point = None
        self._result = None
        self._type = None

    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def need_grovern_point(self):
        return self._need_grovern_point

    @need_grovern_point.setter
    def need_grovern_point(self, value):
        self._need_grovern_point = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.need_grovern_point:
            if hasattr(self.need_grovern_point, 'to_alipay_dict'):
                params['need_grovern_point'] = self.need_grovern_point.to_alipay_dict()
            else:
                params['need_grovern_point'] = self.need_grovern_point
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
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
        o = GovernGoodsCheckMessage()
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'need_grovern_point' in d:
            o.need_grovern_point = d['need_grovern_point']
        if 'result' in d:
            o.result = d['result']
        if 'type' in d:
            o.type = d['type']
        return o


