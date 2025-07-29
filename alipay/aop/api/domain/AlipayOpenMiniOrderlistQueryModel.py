#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniOrderlistQueryModel(object):

    def __init__(self):
        self._gmt_create_end = None
        self._gmt_create_start = None
        self._order_status_list = None
        self._page_num = None
        self._page_size = None
        self._sort_order = None

    @property
    def gmt_create_end(self):
        return self._gmt_create_end

    @gmt_create_end.setter
    def gmt_create_end(self, value):
        self._gmt_create_end = value
    @property
    def gmt_create_start(self):
        return self._gmt_create_start

    @gmt_create_start.setter
    def gmt_create_start(self, value):
        self._gmt_create_start = value
    @property
    def order_status_list(self):
        return self._order_status_list

    @order_status_list.setter
    def order_status_list(self, value):
        if isinstance(value, list):
            self._order_status_list = list()
            for i in value:
                self._order_status_list.append(i)
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
    @property
    def sort_order(self):
        return self._sort_order

    @sort_order.setter
    def sort_order(self, value):
        self._sort_order = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create_end:
            if hasattr(self.gmt_create_end, 'to_alipay_dict'):
                params['gmt_create_end'] = self.gmt_create_end.to_alipay_dict()
            else:
                params['gmt_create_end'] = self.gmt_create_end
        if self.gmt_create_start:
            if hasattr(self.gmt_create_start, 'to_alipay_dict'):
                params['gmt_create_start'] = self.gmt_create_start.to_alipay_dict()
            else:
                params['gmt_create_start'] = self.gmt_create_start
        if self.order_status_list:
            if isinstance(self.order_status_list, list):
                for i in range(0, len(self.order_status_list)):
                    element = self.order_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_status_list[i] = element.to_alipay_dict()
            if hasattr(self.order_status_list, 'to_alipay_dict'):
                params['order_status_list'] = self.order_status_list.to_alipay_dict()
            else:
                params['order_status_list'] = self.order_status_list
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
        if self.sort_order:
            if hasattr(self.sort_order, 'to_alipay_dict'):
                params['sort_order'] = self.sort_order.to_alipay_dict()
            else:
                params['sort_order'] = self.sort_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniOrderlistQueryModel()
        if 'gmt_create_end' in d:
            o.gmt_create_end = d['gmt_create_end']
        if 'gmt_create_start' in d:
            o.gmt_create_start = d['gmt_create_start']
        if 'order_status_list' in d:
            o.order_status_list = d['order_status_list']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sort_order' in d:
            o.sort_order = d['sort_order']
        return o


