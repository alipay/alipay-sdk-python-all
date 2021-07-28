#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingIotMerchantplanCancelModel(object):

    def __init__(self):
        self._merchant_plan_id = None

    @property
    def merchant_plan_id(self):
        return self._merchant_plan_id

    @merchant_plan_id.setter
    def merchant_plan_id(self, value):
        self._merchant_plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_plan_id:
            if hasattr(self.merchant_plan_id, 'to_alipay_dict'):
                params['merchant_plan_id'] = self.merchant_plan_id.to_alipay_dict()
            else:
                params['merchant_plan_id'] = self.merchant_plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingIotMerchantplanCancelModel()
        if 'merchant_plan_id' in d:
            o.merchant_plan_id = d['merchant_plan_id']
        return o


