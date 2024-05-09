#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentItemInfo import RentItemInfo
from alipay.aop.api.domain.RentPriceInfo import RentPriceInfo


class SimpleOrderInfo(object):

    def __init__(self):
        self._item_info_list = None
        self._order_id = None
        self._order_title = None
        self._price_info = None

    @property
    def item_info_list(self):
        return self._item_info_list

    @item_info_list.setter
    def item_info_list(self, value):
        if isinstance(value, list):
            self._item_info_list = list()
            for i in value:
                if isinstance(i, RentItemInfo):
                    self._item_info_list.append(i)
                else:
                    self._item_info_list.append(RentItemInfo.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        if isinstance(value, RentPriceInfo):
            self._price_info = value
        else:
            self._price_info = RentPriceInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.item_info_list:
            if isinstance(self.item_info_list, list):
                for i in range(0, len(self.item_info_list)):
                    element = self.item_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_info_list[i] = element.to_alipay_dict()
            if hasattr(self.item_info_list, 'to_alipay_dict'):
                params['item_info_list'] = self.item_info_list.to_alipay_dict()
            else:
                params['item_info_list'] = self.item_info_list
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
        if self.price_info:
            if hasattr(self.price_info, 'to_alipay_dict'):
                params['price_info'] = self.price_info.to_alipay_dict()
            else:
                params['price_info'] = self.price_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SimpleOrderInfo()
        if 'item_info_list' in d:
            o.item_info_list = d['item_info_list']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'price_info' in d:
            o.price_info = d['price_info']
        return o


