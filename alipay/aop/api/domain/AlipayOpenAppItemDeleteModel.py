#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppItemDeleteModel(object):

    def __init__(self):
        self._item_id_list = None
        self._out_item_id_list = None

    @property
    def item_id_list(self):
        return self._item_id_list

    @item_id_list.setter
    def item_id_list(self, value):
        if isinstance(value, list):
            self._item_id_list = list()
            for i in value:
                self._item_id_list.append(i)
    @property
    def out_item_id_list(self):
        return self._out_item_id_list

    @out_item_id_list.setter
    def out_item_id_list(self, value):
        if isinstance(value, list):
            self._out_item_id_list = list()
            for i in value:
                self._out_item_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.item_id_list:
            if isinstance(self.item_id_list, list):
                for i in range(0, len(self.item_id_list)):
                    element = self.item_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_id_list[i] = element.to_alipay_dict()
            if hasattr(self.item_id_list, 'to_alipay_dict'):
                params['item_id_list'] = self.item_id_list.to_alipay_dict()
            else:
                params['item_id_list'] = self.item_id_list
        if self.out_item_id_list:
            if isinstance(self.out_item_id_list, list):
                for i in range(0, len(self.out_item_id_list)):
                    element = self.out_item_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_item_id_list[i] = element.to_alipay_dict()
            if hasattr(self.out_item_id_list, 'to_alipay_dict'):
                params['out_item_id_list'] = self.out_item_id_list.to_alipay_dict()
            else:
                params['out_item_id_list'] = self.out_item_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppItemDeleteModel()
        if 'item_id_list' in d:
            o.item_id_list = d['item_id_list']
        if 'out_item_id_list' in d:
            o.out_item_id_list = d['out_item_id_list']
        return o


