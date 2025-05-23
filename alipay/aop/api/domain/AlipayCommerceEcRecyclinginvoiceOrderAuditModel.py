#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecyclinginvoiceOrderAuditItem import RecyclinginvoiceOrderAuditItem


class AlipayCommerceEcRecyclinginvoiceOrderAuditModel(object):

    def __init__(self):
        self._memo = None
        self._order_id = None
        self._order_item_list = None
        self._product_id = None
        self._tax_no = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_item_list(self):
        return self._order_item_list

    @order_item_list.setter
    def order_item_list(self, value):
        if isinstance(value, list):
            self._order_item_list = list()
            for i in value:
                if isinstance(i, RecyclinginvoiceOrderAuditItem):
                    self._order_item_list.append(i)
                else:
                    self._order_item_list.append(RecyclinginvoiceOrderAuditItem.from_alipay_dict(i))
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_item_list:
            if isinstance(self.order_item_list, list):
                for i in range(0, len(self.order_item_list)):
                    element = self.order_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_item_list[i] = element.to_alipay_dict()
            if hasattr(self.order_item_list, 'to_alipay_dict'):
                params['order_item_list'] = self.order_item_list.to_alipay_dict()
            else:
                params['order_item_list'] = self.order_item_list
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceOrderAuditModel()
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_item_list' in d:
            o.order_item_list = d['order_item_list']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


