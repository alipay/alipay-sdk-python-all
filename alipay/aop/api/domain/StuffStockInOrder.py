#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StuffStockInOrderItem import StuffStockInOrderItem


class StuffStockInOrder(object):

    def __init__(self):
        self._erp_order = None
        self._erp_order_type = None
        self._ext_info = None
        self._order_items = None
        self._scheduled_receipt_date = None
        self._warehouse_code = None

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
    def order_items(self):
        return self._order_items

    @order_items.setter
    def order_items(self, value):
        if isinstance(value, list):
            self._order_items = list()
            for i in value:
                if isinstance(i, StuffStockInOrderItem):
                    self._order_items.append(i)
                else:
                    self._order_items.append(StuffStockInOrderItem.from_alipay_dict(i))
    @property
    def scheduled_receipt_date(self):
        return self._scheduled_receipt_date

    @scheduled_receipt_date.setter
    def scheduled_receipt_date(self, value):
        self._scheduled_receipt_date = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


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
        if self.order_items:
            if isinstance(self.order_items, list):
                for i in range(0, len(self.order_items)):
                    element = self.order_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_items[i] = element.to_alipay_dict()
            if hasattr(self.order_items, 'to_alipay_dict'):
                params['order_items'] = self.order_items.to_alipay_dict()
            else:
                params['order_items'] = self.order_items
        if self.scheduled_receipt_date:
            if hasattr(self.scheduled_receipt_date, 'to_alipay_dict'):
                params['scheduled_receipt_date'] = self.scheduled_receipt_date.to_alipay_dict()
            else:
                params['scheduled_receipt_date'] = self.scheduled_receipt_date
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StuffStockInOrder()
        if 'erp_order' in d:
            o.erp_order = d['erp_order']
        if 'erp_order_type' in d:
            o.erp_order_type = d['erp_order_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'order_items' in d:
            o.order_items = d['order_items']
        if 'scheduled_receipt_date' in d:
            o.scheduled_receipt_date = d['scheduled_receipt_date']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


