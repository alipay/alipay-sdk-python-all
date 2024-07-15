#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoSumInfo(object):

    def __init__(self):
        self._sale_promo_type = None
        self._total_point_amount = None

    @property
    def sale_promo_type(self):
        return self._sale_promo_type

    @sale_promo_type.setter
    def sale_promo_type(self, value):
        self._sale_promo_type = value
    @property
    def total_point_amount(self):
        return self._total_point_amount

    @total_point_amount.setter
    def total_point_amount(self, value):
        self._total_point_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.sale_promo_type:
            if hasattr(self.sale_promo_type, 'to_alipay_dict'):
                params['sale_promo_type'] = self.sale_promo_type.to_alipay_dict()
            else:
                params['sale_promo_type'] = self.sale_promo_type
        if self.total_point_amount:
            if hasattr(self.total_point_amount, 'to_alipay_dict'):
                params['total_point_amount'] = self.total_point_amount.to_alipay_dict()
            else:
                params['total_point_amount'] = self.total_point_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoSumInfo()
        if 'sale_promo_type' in d:
            o.sale_promo_type = d['sale_promo_type']
        if 'total_point_amount' in d:
            o.total_point_amount = d['total_point_amount']
        return o


