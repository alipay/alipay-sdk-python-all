#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaDataFeedbackurlQueryModel(object):

    def __init__(self):
        self._merchant_id = None

    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaDataFeedbackurlQueryModel()
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        return o


