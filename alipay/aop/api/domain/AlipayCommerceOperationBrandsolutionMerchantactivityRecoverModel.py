#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationBrandsolutionMerchantactivityRecoverModel(object):

    def __init__(self):
        self._activity_id = None
        self._merchant_ids = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def merchant_ids(self):
        return self._merchant_ids

    @merchant_ids.setter
    def merchant_ids(self, value):
        if isinstance(value, list):
            self._merchant_ids = list()
            for i in value:
                self._merchant_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.merchant_ids:
            if isinstance(self.merchant_ids, list):
                for i in range(0, len(self.merchant_ids)):
                    element = self.merchant_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_ids[i] = element.to_alipay_dict()
            if hasattr(self.merchant_ids, 'to_alipay_dict'):
                params['merchant_ids'] = self.merchant_ids.to_alipay_dict()
            else:
                params['merchant_ids'] = self.merchant_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationBrandsolutionMerchantactivityRecoverModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'merchant_ids' in d:
            o.merchant_ids = d['merchant_ids']
        return o


