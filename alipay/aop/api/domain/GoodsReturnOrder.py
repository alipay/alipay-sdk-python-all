#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodsReturnOrderItem import GoodsReturnOrderItem


class GoodsReturnOrder(object):

    def __init__(self):
        self._erp_order = None
        self._erp_order_type = None
        self._ext_info = None
        self._memo = None
        self._order_item = None
        self._ori_erp_order = None
        self._ori_erp_order_type = None

    @property
    def erp_order(self):
        return self._erp_order

    @erp_order.setter
    def erp_order(self, value):
        self._erp_order = value
    @property
    def erp_order_type(self):
        return self._erp_order_type

    @erp_order_type.setter
    def erp_order_type(self, value):
        self._erp_order_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_item(self):
        return self._order_item

    @order_item.setter
    def order_item(self, value):
        if isinstance(value, list):
            self._order_item = list()
            for i in value:
                if isinstance(i, GoodsReturnOrderItem):
                    self._order_item.append(i)
                else:
                    self._order_item.append(GoodsReturnOrderItem.from_alipay_dict(i))
    @property
    def ori_erp_order(self):
        return self._ori_erp_order

    @ori_erp_order.setter
    def ori_erp_order(self, value):
        self._ori_erp_order = value
    @property
    def ori_erp_order_type(self):
        return self._ori_erp_order_type

    @ori_erp_order_type.setter
    def ori_erp_order_type(self, value):
        self._ori_erp_order_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.erp_order:
            if hasattr(self.erp_order, 'to_alipay_dict'):
                params['erp_order'] = self.erp_order.to_alipay_dict()
            else:
                params['erp_order'] = self.erp_order
        if self.erp_order_type:
            if hasattr(self.erp_order_type, 'to_alipay_dict'):
                params['erp_order_type'] = self.erp_order_type.to_alipay_dict()
            else:
                params['erp_order_type'] = self.erp_order_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_item:
            if isinstance(self.order_item, list):
                for i in range(0, len(self.order_item)):
                    element = self.order_item[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_item[i] = element.to_alipay_dict()
            if hasattr(self.order_item, 'to_alipay_dict'):
                params['order_item'] = self.order_item.to_alipay_dict()
            else:
                params['order_item'] = self.order_item
        if self.ori_erp_order:
            if hasattr(self.ori_erp_order, 'to_alipay_dict'):
                params['ori_erp_order'] = self.ori_erp_order.to_alipay_dict()
            else:
                params['ori_erp_order'] = self.ori_erp_order
        if self.ori_erp_order_type:
            if hasattr(self.ori_erp_order_type, 'to_alipay_dict'):
                params['ori_erp_order_type'] = self.ori_erp_order_type.to_alipay_dict()
            else:
                params['ori_erp_order_type'] = self.ori_erp_order_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsReturnOrder()
        if 'erp_order' in d:
            o.erp_order = d['erp_order']
        if 'erp_order_type' in d:
            o.erp_order_type = d['erp_order_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_item' in d:
            o.order_item = d['order_item']
        if 'ori_erp_order' in d:
            o.ori_erp_order = d['ori_erp_order']
        if 'ori_erp_order_type' in d:
            o.ori_erp_order_type = d['ori_erp_order_type']
        return o


