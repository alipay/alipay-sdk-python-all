#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApInvoiceBillLinkOrderRequest import ApInvoiceBillLinkOrderRequest
from alipay.aop.api.domain.ApInvoiceOrderRequest import ApInvoiceOrderRequest


class AlipayBossFncApinvoiceBatchAddModel(object):

    def __init__(self):
        self._ap_invoice_bill_link_orders = None
        self._ap_invoice_order_list = None
        self._memo = None
        self._operator = None
        self._operator_type = None
        self._personal_tax_loss_rate = None

    @property
    def ap_invoice_bill_link_orders(self):
        return self._ap_invoice_bill_link_orders

    @ap_invoice_bill_link_orders.setter
    def ap_invoice_bill_link_orders(self, value):
        if isinstance(value, list):
            self._ap_invoice_bill_link_orders = list()
            for i in value:
                if isinstance(i, ApInvoiceBillLinkOrderRequest):
                    self._ap_invoice_bill_link_orders.append(i)
                else:
                    self._ap_invoice_bill_link_orders.append(ApInvoiceBillLinkOrderRequest.from_alipay_dict(i))
    @property
    def ap_invoice_order_list(self):
        return self._ap_invoice_order_list

    @ap_invoice_order_list.setter
    def ap_invoice_order_list(self, value):
        if isinstance(value, list):
            self._ap_invoice_order_list = list()
            for i in value:
                if isinstance(i, ApInvoiceOrderRequest):
                    self._ap_invoice_order_list.append(i)
                else:
                    self._ap_invoice_order_list.append(ApInvoiceOrderRequest.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
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
    def personal_tax_loss_rate(self):
        return self._personal_tax_loss_rate

    @personal_tax_loss_rate.setter
    def personal_tax_loss_rate(self, value):
        self._personal_tax_loss_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.ap_invoice_bill_link_orders:
            if isinstance(self.ap_invoice_bill_link_orders, list):
                for i in range(0, len(self.ap_invoice_bill_link_orders)):
                    element = self.ap_invoice_bill_link_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ap_invoice_bill_link_orders[i] = element.to_alipay_dict()
            if hasattr(self.ap_invoice_bill_link_orders, 'to_alipay_dict'):
                params['ap_invoice_bill_link_orders'] = self.ap_invoice_bill_link_orders.to_alipay_dict()
            else:
                params['ap_invoice_bill_link_orders'] = self.ap_invoice_bill_link_orders
        if self.ap_invoice_order_list:
            if isinstance(self.ap_invoice_order_list, list):
                for i in range(0, len(self.ap_invoice_order_list)):
                    element = self.ap_invoice_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ap_invoice_order_list[i] = element.to_alipay_dict()
            if hasattr(self.ap_invoice_order_list, 'to_alipay_dict'):
                params['ap_invoice_order_list'] = self.ap_invoice_order_list.to_alipay_dict()
            else:
                params['ap_invoice_order_list'] = self.ap_invoice_order_list
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
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
        if self.personal_tax_loss_rate:
            if hasattr(self.personal_tax_loss_rate, 'to_alipay_dict'):
                params['personal_tax_loss_rate'] = self.personal_tax_loss_rate.to_alipay_dict()
            else:
                params['personal_tax_loss_rate'] = self.personal_tax_loss_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncApinvoiceBatchAddModel()
        if 'ap_invoice_bill_link_orders' in d:
            o.ap_invoice_bill_link_orders = d['ap_invoice_bill_link_orders']
        if 'ap_invoice_order_list' in d:
            o.ap_invoice_order_list = d['ap_invoice_order_list']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'personal_tax_loss_rate' in d:
            o.personal_tax_loss_rate = d['personal_tax_loss_rate']
        return o


