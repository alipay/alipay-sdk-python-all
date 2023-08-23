#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RcvLineDto(object):

    def __init__(self):
        self._expense_month = None
        self._item_name = None
        self._po_line_id = None
        self._po_line_num = None
        self._rcv_line_id = None
        self._rcv_line_num = None
        self._received_amount = None

    @property
    def expense_month(self):
        return self._expense_month

    @expense_month.setter
    def expense_month(self, value):
        self._expense_month = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def po_line_id(self):
        return self._po_line_id

    @po_line_id.setter
    def po_line_id(self, value):
        self._po_line_id = value
    @property
    def po_line_num(self):
        return self._po_line_num

    @po_line_num.setter
    def po_line_num(self, value):
        self._po_line_num = value
    @property
    def rcv_line_id(self):
        return self._rcv_line_id

    @rcv_line_id.setter
    def rcv_line_id(self, value):
        self._rcv_line_id = value
    @property
    def rcv_line_num(self):
        return self._rcv_line_num

    @rcv_line_num.setter
    def rcv_line_num(self, value):
        self._rcv_line_num = value
    @property
    def received_amount(self):
        return self._received_amount

    @received_amount.setter
    def received_amount(self, value):
        self._received_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.expense_month:
            if hasattr(self.expense_month, 'to_alipay_dict'):
                params['expense_month'] = self.expense_month.to_alipay_dict()
            else:
                params['expense_month'] = self.expense_month
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.po_line_id:
            if hasattr(self.po_line_id, 'to_alipay_dict'):
                params['po_line_id'] = self.po_line_id.to_alipay_dict()
            else:
                params['po_line_id'] = self.po_line_id
        if self.po_line_num:
            if hasattr(self.po_line_num, 'to_alipay_dict'):
                params['po_line_num'] = self.po_line_num.to_alipay_dict()
            else:
                params['po_line_num'] = self.po_line_num
        if self.rcv_line_id:
            if hasattr(self.rcv_line_id, 'to_alipay_dict'):
                params['rcv_line_id'] = self.rcv_line_id.to_alipay_dict()
            else:
                params['rcv_line_id'] = self.rcv_line_id
        if self.rcv_line_num:
            if hasattr(self.rcv_line_num, 'to_alipay_dict'):
                params['rcv_line_num'] = self.rcv_line_num.to_alipay_dict()
            else:
                params['rcv_line_num'] = self.rcv_line_num
        if self.received_amount:
            if hasattr(self.received_amount, 'to_alipay_dict'):
                params['received_amount'] = self.received_amount.to_alipay_dict()
            else:
                params['received_amount'] = self.received_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RcvLineDto()
        if 'expense_month' in d:
            o.expense_month = d['expense_month']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'po_line_id' in d:
            o.po_line_id = d['po_line_id']
        if 'po_line_num' in d:
            o.po_line_num = d['po_line_num']
        if 'rcv_line_id' in d:
            o.rcv_line_id = d['rcv_line_id']
        if 'rcv_line_num' in d:
            o.rcv_line_num = d['rcv_line_num']
        if 'received_amount' in d:
            o.received_amount = d['received_amount']
        return o


