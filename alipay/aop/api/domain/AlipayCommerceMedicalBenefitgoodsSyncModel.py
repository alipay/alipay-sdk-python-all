#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitGoodDetail import BenefitGoodDetail


class AlipayCommerceMedicalBenefitgoodsSyncModel(object):

    def __init__(self):
        self._operate_type = None
        self._product = None

    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        if isinstance(value, BenefitGoodDetail):
            self._product = value
        else:
            self._product = BenefitGoodDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.product:
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalBenefitgoodsSyncModel()
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'product' in d:
            o.product = d['product']
        return o


