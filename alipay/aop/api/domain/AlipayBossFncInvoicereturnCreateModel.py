#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ArInvoiceReturnDetailOrder import ArInvoiceReturnDetailOrder


class AlipayBossFncInvoicereturnCreateModel(object):

    def __init__(self):
        self._ar_invoice_return_apply_detail_orders = None
        self._memo = None
        self._modified_item = None
        self._operator = None
        self._operator_type = None
        self._return_order_type = None
        self._return_reason_type = None
        self._tracking_no = None

    @property
    def ar_invoice_return_apply_detail_orders(self):
        return self._ar_invoice_return_apply_detail_orders

    @ar_invoice_return_apply_detail_orders.setter
    def ar_invoice_return_apply_detail_orders(self, value):
        if isinstance(value, list):
            self._ar_invoice_return_apply_detail_orders = list()
            for i in value:
                if isinstance(i, ArInvoiceReturnDetailOrder):
                    self._ar_invoice_return_apply_detail_orders.append(i)
                else:
                    self._ar_invoice_return_apply_detail_orders.append(ArInvoiceReturnDetailOrder.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def modified_item(self):
        return self._modified_item

    @modified_item.setter
    def modified_item(self, value):
        self._modified_item = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def return_order_type(self):
        return self._return_order_type

    @return_order_type.setter
    def return_order_type(self, value):
        self._return_order_type = value
    @property
    def return_reason_type(self):
        return self._return_reason_type

    @return_reason_type.setter
    def return_reason_type(self, value):
        self._return_reason_type = value
    @property
    def tracking_no(self):
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, value):
        self._tracking_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_invoice_return_apply_detail_orders:
            if isinstance(self.ar_invoice_return_apply_detail_orders, list):
                for i in range(0, len(self.ar_invoice_return_apply_detail_orders)):
                    element = self.ar_invoice_return_apply_detail_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ar_invoice_return_apply_detail_orders[i] = element.to_alipay_dict()
            if hasattr(self.ar_invoice_return_apply_detail_orders, 'to_alipay_dict'):
                params['ar_invoice_return_apply_detail_orders'] = self.ar_invoice_return_apply_detail_orders.to_alipay_dict()
            else:
                params['ar_invoice_return_apply_detail_orders'] = self.ar_invoice_return_apply_detail_orders
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.modified_item:
            if hasattr(self.modified_item, 'to_alipay_dict'):
                params['modified_item'] = self.modified_item.to_alipay_dict()
            else:
                params['modified_item'] = self.modified_item
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.return_order_type:
            if hasattr(self.return_order_type, 'to_alipay_dict'):
                params['return_order_type'] = self.return_order_type.to_alipay_dict()
            else:
                params['return_order_type'] = self.return_order_type
        if self.return_reason_type:
            if hasattr(self.return_reason_type, 'to_alipay_dict'):
                params['return_reason_type'] = self.return_reason_type.to_alipay_dict()
            else:
                params['return_reason_type'] = self.return_reason_type
        if self.tracking_no:
            if hasattr(self.tracking_no, 'to_alipay_dict'):
                params['tracking_no'] = self.tracking_no.to_alipay_dict()
            else:
                params['tracking_no'] = self.tracking_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInvoicereturnCreateModel()
        if 'ar_invoice_return_apply_detail_orders' in d:
            o.ar_invoice_return_apply_detail_orders = d['ar_invoice_return_apply_detail_orders']
        if 'memo' in d:
            o.memo = d['memo']
        if 'modified_item' in d:
            o.modified_item = d['modified_item']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'return_order_type' in d:
            o.return_order_type = d['return_order_type']
        if 'return_reason_type' in d:
            o.return_reason_type = d['return_reason_type']
        if 'tracking_no' in d:
            o.tracking_no = d['tracking_no']
        return o


