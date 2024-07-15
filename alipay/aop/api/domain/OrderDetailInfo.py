#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemDetailInfo import ItemDetailInfo


class OrderDetailInfo(object):

    def __init__(self):
        self._amount = None
        self._item_detail_info_list = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def item_detail_info_list(self):
        return self._item_detail_info_list

    @item_detail_info_list.setter
    def item_detail_info_list(self, value):
        if isinstance(value, list):
            self._item_detail_info_list = list()
            for i in value:
                if isinstance(i, ItemDetailInfo):
                    self._item_detail_info_list.append(i)
                else:
                    self._item_detail_info_list.append(ItemDetailInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.item_detail_info_list:
            if isinstance(self.item_detail_info_list, list):
                for i in range(0, len(self.item_detail_info_list)):
                    element = self.item_detail_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_detail_info_list[i] = element.to_alipay_dict()
            if hasattr(self.item_detail_info_list, 'to_alipay_dict'):
                params['item_detail_info_list'] = self.item_detail_info_list.to_alipay_dict()
            else:
                params['item_detail_info_list'] = self.item_detail_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderDetailInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'item_detail_info_list' in d:
            o.item_detail_info_list = d['item_detail_info_list']
        return o


