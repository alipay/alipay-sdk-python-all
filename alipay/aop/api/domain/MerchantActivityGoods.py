#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityGoods import ActivityGoods


class MerchantActivityGoods(object):

    def __init__(self):
        self._activity_goods_benefit = None
        self._merchant_activity_status = None
        self._merchant_id = None

    @property
    def activity_goods_benefit(self):
        return self._activity_goods_benefit

    @activity_goods_benefit.setter
    def activity_goods_benefit(self, value):
        if isinstance(value, list):
            self._activity_goods_benefit = list()
            for i in value:
                if isinstance(i, ActivityGoods):
                    self._activity_goods_benefit.append(i)
                else:
                    self._activity_goods_benefit.append(ActivityGoods.from_alipay_dict(i))
    @property
    def merchant_activity_status(self):
        return self._merchant_activity_status

    @merchant_activity_status.setter
    def merchant_activity_status(self, value):
        self._merchant_activity_status = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_goods_benefit:
            if isinstance(self.activity_goods_benefit, list):
                for i in range(0, len(self.activity_goods_benefit)):
                    element = self.activity_goods_benefit[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_goods_benefit[i] = element.to_alipay_dict()
            if hasattr(self.activity_goods_benefit, 'to_alipay_dict'):
                params['activity_goods_benefit'] = self.activity_goods_benefit.to_alipay_dict()
            else:
                params['activity_goods_benefit'] = self.activity_goods_benefit
        if self.merchant_activity_status:
            if hasattr(self.merchant_activity_status, 'to_alipay_dict'):
                params['merchant_activity_status'] = self.merchant_activity_status.to_alipay_dict()
            else:
                params['merchant_activity_status'] = self.merchant_activity_status
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
        o = MerchantActivityGoods()
        if 'activity_goods_benefit' in d:
            o.activity_goods_benefit = d['activity_goods_benefit']
        if 'merchant_activity_status' in d:
            o.merchant_activity_status = d['merchant_activity_status']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        return o


