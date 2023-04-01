#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherExchangeGoodsInfo import VoucherExchangeGoodsInfo
from alipay.aop.api.domain.VoucherDeductThresholdInfo import VoucherDeductThresholdInfo


class ExchangeVoucherInfo(object):

    def __init__(self):
        self._amount = None
        self._biz_type = None
        self._exchange_goods_info = None
        self._floor_amount = None
        self._voucher_deduct_threshold_info = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def exchange_goods_info(self):
        return self._exchange_goods_info

    @exchange_goods_info.setter
    def exchange_goods_info(self, value):
        if isinstance(value, VoucherExchangeGoodsInfo):
            self._exchange_goods_info = value
        else:
            self._exchange_goods_info = VoucherExchangeGoodsInfo.from_alipay_dict(value)
    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value
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
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.exchange_goods_info:
            if hasattr(self.exchange_goods_info, 'to_alipay_dict'):
                params['exchange_goods_info'] = self.exchange_goods_info.to_alipay_dict()
            else:
                params['exchange_goods_info'] = self.exchange_goods_info
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
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
        o = ExchangeVoucherInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'exchange_goods_info' in d:
            o.exchange_goods_info = d['exchange_goods_info']
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        if 'voucher_deduct_threshold_info' in d:
            o.voucher_deduct_threshold_info = d['voucher_deduct_threshold_info']
        return o


