#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherAvailableOutItemInfo import VoucherAvailableOutItemInfo


class VoucherAvailableItemInfo(object):

    def __init__(self):
        self._item_id = None
        self._out_item_info = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def out_item_info(self):
        return self._out_item_info

    @out_item_info.setter
    def out_item_info(self, value):
        if isinstance(value, list):
            self._out_item_info = list()
            for i in value:
                if isinstance(i, VoucherAvailableOutItemInfo):
                    self._out_item_info.append(i)
                else:
                    self._out_item_info.append(VoucherAvailableOutItemInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.out_item_info:
            if isinstance(self.out_item_info, list):
                for i in range(0, len(self.out_item_info)):
                    element = self.out_item_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_item_info[i] = element.to_alipay_dict()
            if hasattr(self.out_item_info, 'to_alipay_dict'):
                params['out_item_info'] = self.out_item_info.to_alipay_dict()
            else:
                params['out_item_info'] = self.out_item_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableItemInfo()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'out_item_info' in d:
            o.out_item_info = d['out_item_info']
        return o


