#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherDeductThresholdInfo import VoucherDeductThresholdInfo


class SpecialVoucherInfo(object):

    def __init__(self):
        self._floor_amount = None
        self._special_amount = None
        self._voucher_deduct_threshold_info = None

    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value
    @property
    def special_amount(self):
        return self._special_amount

    @special_amount.setter
    def special_amount(self, value):
        self._special_amount = value
    @property
    def voucher_deduct_threshold_info(self):
        return self._voucher_deduct_threshold_info

    @voucher_deduct_threshold_info.setter
    def voucher_deduct_threshold_info(self, value):
        if isinstance(value, VoucherDeductThresholdInfo):
            self._voucher_deduct_threshold_info = value
        else:
            self._voucher_deduct_threshold_info = VoucherDeductThresholdInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        if self.special_amount:
            if hasattr(self.special_amount, 'to_alipay_dict'):
                params['special_amount'] = self.special_amount.to_alipay_dict()
            else:
                params['special_amount'] = self.special_amount
        if self.voucher_deduct_threshold_info:
            if hasattr(self.voucher_deduct_threshold_info, 'to_alipay_dict'):
                params['voucher_deduct_threshold_info'] = self.voucher_deduct_threshold_info.to_alipay_dict()
            else:
                params['voucher_deduct_threshold_info'] = self.voucher_deduct_threshold_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecialVoucherInfo()
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        if 'special_amount' in d:
            o.special_amount = d['special_amount']
        if 'voucher_deduct_threshold_info' in d:
            o.voucher_deduct_threshold_info = d['voucher_deduct_threshold_info']
        return o


