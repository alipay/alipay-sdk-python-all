#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SkuInfo import SkuInfo


class AlipayUserAliyunbenefitSyncModel(object):

    def __init__(self):
        self._category_code = None
        self._item_id = None
        self._item_title = None
        self._main_pic = None
        self._op_action = None
        self._op_timestamp = None
        self._operator = None
        self._reserve_price = None
        self._shop_name = None
        self._sku_infos = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_title(self):
        return self._item_title

    @item_title.setter
    def item_title(self, value):
        self._item_title = value
    @property
    def main_pic(self):
        return self._main_pic

    @main_pic.setter
    def main_pic(self, value):
        self._main_pic = value
    @property
    def op_action(self):
        return self._op_action

    @op_action.setter
    def op_action(self, value):
        self._op_action = value
    @property
    def op_timestamp(self):
        return self._op_timestamp

    @op_timestamp.setter
    def op_timestamp(self, value):
        self._op_timestamp = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def reserve_price(self):
        return self._reserve_price

    @reserve_price.setter
    def reserve_price(self, value):
        self._reserve_price = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def sku_infos(self):
        return self._sku_infos

    @sku_infos.setter
    def sku_infos(self, value):
        if isinstance(value, list):
            self._sku_infos = list()
            for i in value:
                if isinstance(i, SkuInfo):
                    self._sku_infos.append(i)
                else:
                    self._sku_infos.append(SkuInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_title:
            if hasattr(self.item_title, 'to_alipay_dict'):
                params['item_title'] = self.item_title.to_alipay_dict()
            else:
                params['item_title'] = self.item_title
        if self.main_pic:
            if hasattr(self.main_pic, 'to_alipay_dict'):
                params['main_pic'] = self.main_pic.to_alipay_dict()
            else:
                params['main_pic'] = self.main_pic
        if self.op_action:
            if hasattr(self.op_action, 'to_alipay_dict'):
                params['op_action'] = self.op_action.to_alipay_dict()
            else:
                params['op_action'] = self.op_action
        if self.op_timestamp:
            if hasattr(self.op_timestamp, 'to_alipay_dict'):
                params['op_timestamp'] = self.op_timestamp.to_alipay_dict()
            else:
                params['op_timestamp'] = self.op_timestamp
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.reserve_price:
            if hasattr(self.reserve_price, 'to_alipay_dict'):
                params['reserve_price'] = self.reserve_price.to_alipay_dict()
            else:
                params['reserve_price'] = self.reserve_price
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.sku_infos:
            if isinstance(self.sku_infos, list):
                for i in range(0, len(self.sku_infos)):
                    element = self.sku_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_infos[i] = element.to_alipay_dict()
            if hasattr(self.sku_infos, 'to_alipay_dict'):
                params['sku_infos'] = self.sku_infos.to_alipay_dict()
            else:
                params['sku_infos'] = self.sku_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAliyunbenefitSyncModel()
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_title' in d:
            o.item_title = d['item_title']
        if 'main_pic' in d:
            o.main_pic = d['main_pic']
        if 'op_action' in d:
            o.op_action = d['op_action']
        if 'op_timestamp' in d:
            o.op_timestamp = d['op_timestamp']
        if 'operator' in d:
            o.operator = d['operator']
        if 'reserve_price' in d:
            o.reserve_price = d['reserve_price']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'sku_infos' in d:
            o.sku_infos = d['sku_infos']
        return o


