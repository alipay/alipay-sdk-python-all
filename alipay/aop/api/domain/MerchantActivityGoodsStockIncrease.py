#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityGoodsStockIncrease import ActivityGoodsStockIncrease


class MerchantActivityGoodsStockIncrease(object):

    def __init__(self):
        self._goods_benefit_increase_stock = None
        self._merchant_id = None

    @property
    def goods_benefit_increase_stock(self):
        return self._goods_benefit_increase_stock

    @goods_benefit_increase_stock.setter
    def goods_benefit_increase_stock(self, value):
        if isinstance(value, list):
            self._goods_benefit_increase_stock = list()
            for i in value:
                if isinstance(i, ActivityGoodsStockIncrease):
                    self._goods_benefit_increase_stock.append(i)
                else:
                    self._goods_benefit_increase_stock.append(ActivityGoodsStockIncrease.from_alipay_dict(i))
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_benefit_increase_stock:
            if isinstance(self.goods_benefit_increase_stock, list):
                for i in range(0, len(self.goods_benefit_increase_stock)):
                    element = self.goods_benefit_increase_stock[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_benefit_increase_stock[i] = element.to_alipay_dict()
            if hasattr(self.goods_benefit_increase_stock, 'to_alipay_dict'):
                params['goods_benefit_increase_stock'] = self.goods_benefit_increase_stock.to_alipay_dict()
            else:
                params['goods_benefit_increase_stock'] = self.goods_benefit_increase_stock
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
        o = MerchantActivityGoodsStockIncrease()
        if 'goods_benefit_increase_stock' in d:
            o.goods_benefit_increase_stock = d['goods_benefit_increase_stock']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        return o


