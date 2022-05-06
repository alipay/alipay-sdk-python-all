#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantActivityGoodsStockIncrease import MerchantActivityGoodsStockIncrease


class AlipayCommerceOperationBrandsolutionGoodsstockAddModel(object):

    def __init__(self):
        self._activity_id = None
        self._merchant_activity_goods_increase_stock = None
        self._out_biz_no = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def merchant_activity_goods_increase_stock(self):
        return self._merchant_activity_goods_increase_stock

    @merchant_activity_goods_increase_stock.setter
    def merchant_activity_goods_increase_stock(self, value):
        if isinstance(value, list):
            self._merchant_activity_goods_increase_stock = list()
            for i in value:
                if isinstance(i, MerchantActivityGoodsStockIncrease):
                    self._merchant_activity_goods_increase_stock.append(i)
                else:
                    self._merchant_activity_goods_increase_stock.append(MerchantActivityGoodsStockIncrease.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.merchant_activity_goods_increase_stock:
            if isinstance(self.merchant_activity_goods_increase_stock, list):
                for i in range(0, len(self.merchant_activity_goods_increase_stock)):
                    element = self.merchant_activity_goods_increase_stock[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_activity_goods_increase_stock[i] = element.to_alipay_dict()
            if hasattr(self.merchant_activity_goods_increase_stock, 'to_alipay_dict'):
                params['merchant_activity_goods_increase_stock'] = self.merchant_activity_goods_increase_stock.to_alipay_dict()
            else:
                params['merchant_activity_goods_increase_stock'] = self.merchant_activity_goods_increase_stock
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationBrandsolutionGoodsstockAddModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'merchant_activity_goods_increase_stock' in d:
            o.merchant_activity_goods_increase_stock = d['merchant_activity_goods_increase_stock']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


