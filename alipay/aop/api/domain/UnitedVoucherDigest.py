#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnitedVoucherDigest(object):

    def __init__(self):
        self._budget_close = None
        self._ceiling_amount = None
        self._discount_type = None
        self._from_amount = None
        self._prize_id = None
        self._reduction_ratio = None
        self._show_order = None
        self._to_amount = None
        self._voucher_biz_code = None

    @property
    def budget_close(self):
        return self._budget_close

    @budget_close.setter
    def budget_close(self, value):
        self._budget_close = value
    @property
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def from_amount(self):
        return self._from_amount

    @from_amount.setter
    def from_amount(self, value):
        self._from_amount = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def reduction_ratio(self):
        return self._reduction_ratio

    @reduction_ratio.setter
    def reduction_ratio(self, value):
        self._reduction_ratio = value
    @property
    def show_order(self):
        return self._show_order

    @show_order.setter
    def show_order(self, value):
        self._show_order = value
    @property
    def to_amount(self):
        return self._to_amount

    @to_amount.setter
    def to_amount(self, value):
        self._to_amount = value
    @property
    def voucher_biz_code(self):
        return self._voucher_biz_code

    @voucher_biz_code.setter
    def voucher_biz_code(self, value):
        self._voucher_biz_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget_close:
            if hasattr(self.budget_close, 'to_alipay_dict'):
                params['budget_close'] = self.budget_close.to_alipay_dict()
            else:
                params['budget_close'] = self.budget_close
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        if self.from_amount:
            if hasattr(self.from_amount, 'to_alipay_dict'):
                params['from_amount'] = self.from_amount.to_alipay_dict()
            else:
                params['from_amount'] = self.from_amount
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.reduction_ratio:
            if hasattr(self.reduction_ratio, 'to_alipay_dict'):
                params['reduction_ratio'] = self.reduction_ratio.to_alipay_dict()
            else:
                params['reduction_ratio'] = self.reduction_ratio
        if self.show_order:
            if hasattr(self.show_order, 'to_alipay_dict'):
                params['show_order'] = self.show_order.to_alipay_dict()
            else:
                params['show_order'] = self.show_order
        if self.to_amount:
            if hasattr(self.to_amount, 'to_alipay_dict'):
                params['to_amount'] = self.to_amount.to_alipay_dict()
            else:
                params['to_amount'] = self.to_amount
        if self.voucher_biz_code:
            if hasattr(self.voucher_biz_code, 'to_alipay_dict'):
                params['voucher_biz_code'] = self.voucher_biz_code.to_alipay_dict()
            else:
                params['voucher_biz_code'] = self.voucher_biz_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnitedVoucherDigest()
        if 'budget_close' in d:
            o.budget_close = d['budget_close']
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        if 'from_amount' in d:
            o.from_amount = d['from_amount']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'reduction_ratio' in d:
            o.reduction_ratio = d['reduction_ratio']
        if 'show_order' in d:
            o.show_order = d['show_order']
        if 'to_amount' in d:
            o.to_amount = d['to_amount']
        if 'voucher_biz_code' in d:
            o.voucher_biz_code = d['voucher_biz_code']
        return o


