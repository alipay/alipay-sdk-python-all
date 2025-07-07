#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleDeductOutVO import RecycleDeductOutVO
from alipay.aop.api.domain.RecycleInspectProductVO import RecycleInspectProductVO
from alipay.aop.api.domain.RecycleRoyaltyInfo import RecycleRoyaltyInfo


class AlipayCommerceRecycleOrderMerchantConfirmModel(object):

    def __init__(self):
        self._deduct_out = None
        self._inspect_products = None
        self._open_id = None
        self._order_id = None
        self._order_inspect_price = None
        self._out_order_id = None
        self._royalty_infos = None
        self._user_id = None

    @property
    def deduct_out(self):
        return self._deduct_out

    @deduct_out.setter
    def deduct_out(self, value):
        if isinstance(value, RecycleDeductOutVO):
            self._deduct_out = value
        else:
            self._deduct_out = RecycleDeductOutVO.from_alipay_dict(value)
    @property
    def inspect_products(self):
        return self._inspect_products

    @inspect_products.setter
    def inspect_products(self, value):
        if isinstance(value, list):
            self._inspect_products = list()
            for i in value:
                if isinstance(i, RecycleInspectProductVO):
                    self._inspect_products.append(i)
                else:
                    self._inspect_products.append(RecycleInspectProductVO.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_inspect_price(self):
        return self._order_inspect_price

    @order_inspect_price.setter
    def order_inspect_price(self, value):
        self._order_inspect_price = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def royalty_infos(self):
        return self._royalty_infos

    @royalty_infos.setter
    def royalty_infos(self, value):
        if isinstance(value, list):
            self._royalty_infos = list()
            for i in value:
                if isinstance(i, RecycleRoyaltyInfo):
                    self._royalty_infos.append(i)
                else:
                    self._royalty_infos.append(RecycleRoyaltyInfo.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduct_out:
            if hasattr(self.deduct_out, 'to_alipay_dict'):
                params['deduct_out'] = self.deduct_out.to_alipay_dict()
            else:
                params['deduct_out'] = self.deduct_out
        if self.inspect_products:
            if isinstance(self.inspect_products, list):
                for i in range(0, len(self.inspect_products)):
                    element = self.inspect_products[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inspect_products[i] = element.to_alipay_dict()
            if hasattr(self.inspect_products, 'to_alipay_dict'):
                params['inspect_products'] = self.inspect_products.to_alipay_dict()
            else:
                params['inspect_products'] = self.inspect_products
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_inspect_price:
            if hasattr(self.order_inspect_price, 'to_alipay_dict'):
                params['order_inspect_price'] = self.order_inspect_price.to_alipay_dict()
            else:
                params['order_inspect_price'] = self.order_inspect_price
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.royalty_infos:
            if isinstance(self.royalty_infos, list):
                for i in range(0, len(self.royalty_infos)):
                    element = self.royalty_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.royalty_infos[i] = element.to_alipay_dict()
            if hasattr(self.royalty_infos, 'to_alipay_dict'):
                params['royalty_infos'] = self.royalty_infos.to_alipay_dict()
            else:
                params['royalty_infos'] = self.royalty_infos
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleOrderMerchantConfirmModel()
        if 'deduct_out' in d:
            o.deduct_out = d['deduct_out']
        if 'inspect_products' in d:
            o.inspect_products = d['inspect_products']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_inspect_price' in d:
            o.order_inspect_price = d['order_inspect_price']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'royalty_infos' in d:
            o.royalty_infos = d['royalty_infos']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


