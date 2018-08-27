#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsInvoiceApplyItem(object):

    def __init__(self):
        self._apply_scope = None
        self._expense_type = None
        self._ins_biz_no = None
        self._ins_biz_type = None

    @property
    def apply_scope(self):
        return self._apply_scope

    @apply_scope.setter
    def apply_scope(self, value):
        self._apply_scope = value
    @property
    def expense_type(self):
        return self._expense_type

    @expense_type.setter
    def expense_type(self, value):
        self._expense_type = value
    @property
    def ins_biz_no(self):
        return self._ins_biz_no

    @ins_biz_no.setter
    def ins_biz_no(self, value):
        self._ins_biz_no = value
    @property
    def ins_biz_type(self):
        return self._ins_biz_type

    @ins_biz_type.setter
    def ins_biz_type(self, value):
        self._ins_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_scope:
            if hasattr(self.apply_scope, 'to_alipay_dict'):
                params['apply_scope'] = self.apply_scope.to_alipay_dict()
            else:
                params['apply_scope'] = self.apply_scope
        if self.expense_type:
            if hasattr(self.expense_type, 'to_alipay_dict'):
                params['expense_type'] = self.expense_type.to_alipay_dict()
            else:
                params['expense_type'] = self.expense_type
        if self.ins_biz_no:
            if hasattr(self.ins_biz_no, 'to_alipay_dict'):
                params['ins_biz_no'] = self.ins_biz_no.to_alipay_dict()
            else:
                params['ins_biz_no'] = self.ins_biz_no
        if self.ins_biz_type:
            if hasattr(self.ins_biz_type, 'to_alipay_dict'):
                params['ins_biz_type'] = self.ins_biz_type.to_alipay_dict()
            else:
                params['ins_biz_type'] = self.ins_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsInvoiceApplyItem()
        if 'apply_scope' in d:
            o.apply_scope = d['apply_scope']
        if 'expense_type' in d:
            o.expense_type = d['expense_type']
        if 'ins_biz_no' in d:
            o.ins_biz_no = d['ins_biz_no']
        if 'ins_biz_type' in d:
            o.ins_biz_type = d['ins_biz_type']
        return o


