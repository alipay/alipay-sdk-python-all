#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniItemPageQueryModel(object):

    def __init__(self):
        self._item_id_list = None
        self._operation = None
        self._page_num = None
        self._page_size = None

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
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


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
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniItemPageQueryModel()
        if 'item_id_list' in d:
            o.item_id_list = d['item_id_list']
        if 'operation' in d:
            o.operation = d['operation']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


