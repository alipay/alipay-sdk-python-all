#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotnspplaycenterActivityVoucherInfo(object):

    def __init__(self):
        self._item_logo = None
        self._merchant_logo = None
        self._merchant_name = None
        self._original_amount = None
        self._prize_id = None
        self._reduction_amount = None
        self._threshold_amount_text = None
        self._unit = None
        self._voucher_id = None
        self._voucher_name = None
        self._voucher_type = None

    @property
    def item_logo(self):
        return self._item_logo

    @item_logo.setter
    def item_logo(self, value):
        self._item_logo = value
    @property
    def merchant_logo(self):
        return self._merchant_logo

    @merchant_logo.setter
    def merchant_logo(self, value):
        self._merchant_logo = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def original_amount(self):
        return self._original_amount

    @original_amount.setter
    def original_amount(self, value):
        self._original_amount = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def reduction_amount(self):
        return self._reduction_amount

    @reduction_amount.setter
    def reduction_amount(self, value):
        self._reduction_amount = value
    @property
    def threshold_amount_text(self):
        return self._threshold_amount_text

    @threshold_amount_text.setter
    def threshold_amount_text(self, value):
        self._threshold_amount_text = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_logo:
            if hasattr(self.item_logo, 'to_alipay_dict'):
                params['item_logo'] = self.item_logo.to_alipay_dict()
            else:
                params['item_logo'] = self.item_logo
        if self.merchant_logo:
            if hasattr(self.merchant_logo, 'to_alipay_dict'):
                params['merchant_logo'] = self.merchant_logo.to_alipay_dict()
            else:
                params['merchant_logo'] = self.merchant_logo
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.original_amount:
            if hasattr(self.original_amount, 'to_alipay_dict'):
                params['original_amount'] = self.original_amount.to_alipay_dict()
            else:
                params['original_amount'] = self.original_amount
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.reduction_amount:
            if hasattr(self.reduction_amount, 'to_alipay_dict'):
                params['reduction_amount'] = self.reduction_amount.to_alipay_dict()
            else:
                params['reduction_amount'] = self.reduction_amount
        if self.threshold_amount_text:
            if hasattr(self.threshold_amount_text, 'to_alipay_dict'):
                params['threshold_amount_text'] = self.threshold_amount_text.to_alipay_dict()
            else:
                params['threshold_amount_text'] = self.threshold_amount_text
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotnspplaycenterActivityVoucherInfo()
        if 'item_logo' in d:
            o.item_logo = d['item_logo']
        if 'merchant_logo' in d:
            o.merchant_logo = d['merchant_logo']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'original_amount' in d:
            o.original_amount = d['original_amount']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'reduction_amount' in d:
            o.reduction_amount = d['reduction_amount']
        if 'threshold_amount_text' in d:
            o.threshold_amount_text = d['threshold_amount_text']
        if 'unit' in d:
            o.unit = d['unit']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


