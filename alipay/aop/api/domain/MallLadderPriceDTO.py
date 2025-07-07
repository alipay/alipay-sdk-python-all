#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MallLadderPriceDTO(object):

    def __init__(self):
        self._goods_quotation_id = None
        self._minimum_purchase_quantity = None
        self._unit_price = None

    @property
    def goods_quotation_id(self):
        return self._goods_quotation_id

    @goods_quotation_id.setter
    def goods_quotation_id(self, value):
        self._goods_quotation_id = value
    @property
    def minimum_purchase_quantity(self):
        return self._minimum_purchase_quantity

    @minimum_purchase_quantity.setter
    def minimum_purchase_quantity(self, value):
        self._minimum_purchase_quantity = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_quotation_id:
            if hasattr(self.goods_quotation_id, 'to_alipay_dict'):
                params['goods_quotation_id'] = self.goods_quotation_id.to_alipay_dict()
            else:
                params['goods_quotation_id'] = self.goods_quotation_id
        if self.minimum_purchase_quantity:
            if hasattr(self.minimum_purchase_quantity, 'to_alipay_dict'):
                params['minimum_purchase_quantity'] = self.minimum_purchase_quantity.to_alipay_dict()
            else:
                params['minimum_purchase_quantity'] = self.minimum_purchase_quantity
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MallLadderPriceDTO()
        if 'goods_quotation_id' in d:
            o.goods_quotation_id = d['goods_quotation_id']
        if 'minimum_purchase_quantity' in d:
            o.minimum_purchase_quantity = d['minimum_purchase_quantity']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


