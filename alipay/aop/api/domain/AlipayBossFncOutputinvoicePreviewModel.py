#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.InvoiceBillItem import InvoiceBillItem
from alipay.aop.api.domain.OutputApplyInvoiceDetailOrder import OutputApplyInvoiceDetailOrder
from alipay.aop.api.domain.InvoiceApplyOpenApi import InvoiceApplyOpenApi


class AlipayBossFncOutputinvoicePreviewModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_no = None
        self._invoice_amt = None
        self._invoice_bill_items = None
        self._invoice_note = None
        self._mail_id = None
        self._memo = None
        self._operator = None
        self._output_apply_invoice_detail_orders = None
        self._output_invoice_apply_orders = None
        self._render_without_rule = None
        self._source = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def invoice_amt(self):
        return self._invoice_amt

    @invoice_amt.setter
    def invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoice_amt = value
        else:
            self._invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoice_bill_items(self):
        return self._invoice_bill_items

    @invoice_bill_items.setter
    def invoice_bill_items(self, value):
        if isinstance(value, list):
            self._invoice_bill_items = list()
            for i in value:
                if isinstance(i, InvoiceBillItem):
                    self._invoice_bill_items.append(i)
                else:
                    self._invoice_bill_items.append(InvoiceBillItem.from_alipay_dict(i))
    @property
    def invoice_note(self):
        return self._invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self._invoice_note = value
    @property
    def mail_id(self):
        return self._mail_id

    @mail_id.setter
    def mail_id(self, value):
        self._mail_id = value
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
    def output_apply_invoice_detail_orders(self):
        return self._output_apply_invoice_detail_orders

    @output_apply_invoice_detail_orders.setter
    def output_apply_invoice_detail_orders(self, value):
        if isinstance(value, list):
            self._output_apply_invoice_detail_orders = list()
            for i in value:
                if isinstance(i, OutputApplyInvoiceDetailOrder):
                    self._output_apply_invoice_detail_orders.append(i)
                else:
                    self._output_apply_invoice_detail_orders.append(OutputApplyInvoiceDetailOrder.from_alipay_dict(i))
    @property
    def output_invoice_apply_orders(self):
        return self._output_invoice_apply_orders

    @output_invoice_apply_orders.setter
    def output_invoice_apply_orders(self, value):
        if isinstance(value, list):
            self._output_invoice_apply_orders = list()
            for i in value:
                if isinstance(i, InvoiceApplyOpenApi):
                    self._output_invoice_apply_orders.append(i)
                else:
                    self._output_invoice_apply_orders.append(InvoiceApplyOpenApi.from_alipay_dict(i))
    @property
    def render_without_rule(self):
        return self._render_without_rule

    @render_without_rule.setter
    def render_without_rule(self, value):
        self._render_without_rule = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
        if self.invoice_bill_items:
            if isinstance(self.invoice_bill_items, list):
                for i in range(0, len(self.invoice_bill_items)):
                    element = self.invoice_bill_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_bill_items[i] = element.to_alipay_dict()
            if hasattr(self.invoice_bill_items, 'to_alipay_dict'):
                params['invoice_bill_items'] = self.invoice_bill_items.to_alipay_dict()
            else:
                params['invoice_bill_items'] = self.invoice_bill_items
        if self.invoice_note:
            if hasattr(self.invoice_note, 'to_alipay_dict'):
                params['invoice_note'] = self.invoice_note.to_alipay_dict()
            else:
                params['invoice_note'] = self.invoice_note
        if self.mail_id:
            if hasattr(self.mail_id, 'to_alipay_dict'):
                params['mail_id'] = self.mail_id.to_alipay_dict()
            else:
                params['mail_id'] = self.mail_id
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
        if self.output_apply_invoice_detail_orders:
            if isinstance(self.output_apply_invoice_detail_orders, list):
                for i in range(0, len(self.output_apply_invoice_detail_orders)):
                    element = self.output_apply_invoice_detail_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.output_apply_invoice_detail_orders[i] = element.to_alipay_dict()
            if hasattr(self.output_apply_invoice_detail_orders, 'to_alipay_dict'):
                params['output_apply_invoice_detail_orders'] = self.output_apply_invoice_detail_orders.to_alipay_dict()
            else:
                params['output_apply_invoice_detail_orders'] = self.output_apply_invoice_detail_orders
        if self.output_invoice_apply_orders:
            if isinstance(self.output_invoice_apply_orders, list):
                for i in range(0, len(self.output_invoice_apply_orders)):
                    element = self.output_invoice_apply_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.output_invoice_apply_orders[i] = element.to_alipay_dict()
            if hasattr(self.output_invoice_apply_orders, 'to_alipay_dict'):
                params['output_invoice_apply_orders'] = self.output_invoice_apply_orders.to_alipay_dict()
            else:
                params['output_invoice_apply_orders'] = self.output_invoice_apply_orders
        if self.render_without_rule:
            if hasattr(self.render_without_rule, 'to_alipay_dict'):
                params['render_without_rule'] = self.render_without_rule.to_alipay_dict()
            else:
                params['render_without_rule'] = self.render_without_rule
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncOutputinvoicePreviewModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_bill_items' in d:
            o.invoice_bill_items = d['invoice_bill_items']
        if 'invoice_note' in d:
            o.invoice_note = d['invoice_note']
        if 'mail_id' in d:
            o.mail_id = d['mail_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'output_apply_invoice_detail_orders' in d:
            o.output_apply_invoice_detail_orders = d['output_apply_invoice_detail_orders']
        if 'output_invoice_apply_orders' in d:
            o.output_invoice_apply_orders = d['output_invoice_apply_orders']
        if 'render_without_rule' in d:
            o.render_without_rule = d['render_without_rule']
        if 'source' in d:
            o.source = d['source']
        return o


