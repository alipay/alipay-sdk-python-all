#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantIndirectAccountNotifyModel(object):

    def __init__(self):
        self._amount = None
        self._mrchind_app_id = None
        self._out_biz_no = None
        self._out_merchant_no = None
        self._pay_channel = None
        self._payer_bank_type = None
        self._payer_total_amount_on_the_merchant = None
        self._payer_total_count_on_the_merchant = None
        self._payer_user_no = None
        self._shop_code = None
        self._shop_name = None
        self._smid = None
        self._third_party_merchant_no = None
        self._third_party_trade_no = None
        self._total_amount = None
        self._total_count = None
        self._trade_time = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def mrchind_app_id(self):
        return self._mrchind_app_id

    @mrchind_app_id.setter
    def mrchind_app_id(self, value):
        self._mrchind_app_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_merchant_no(self):
        return self._out_merchant_no

    @out_merchant_no.setter
    def out_merchant_no(self, value):
        self._out_merchant_no = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def payer_bank_type(self):
        return self._payer_bank_type

    @payer_bank_type.setter
    def payer_bank_type(self, value):
        self._payer_bank_type = value
    @property
    def payer_total_amount_on_the_merchant(self):
        return self._payer_total_amount_on_the_merchant

    @payer_total_amount_on_the_merchant.setter
    def payer_total_amount_on_the_merchant(self, value):
        self._payer_total_amount_on_the_merchant = value
    @property
    def payer_total_count_on_the_merchant(self):
        return self._payer_total_count_on_the_merchant

    @payer_total_count_on_the_merchant.setter
    def payer_total_count_on_the_merchant(self, value):
        self._payer_total_count_on_the_merchant = value
    @property
    def payer_user_no(self):
        return self._payer_user_no

    @payer_user_no.setter
    def payer_user_no(self, value):
        self._payer_user_no = value
    @property
    def shop_code(self):
        return self._shop_code

    @shop_code.setter
    def shop_code(self, value):
        self._shop_code = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def third_party_merchant_no(self):
        return self._third_party_merchant_no

    @third_party_merchant_no.setter
    def third_party_merchant_no(self, value):
        self._third_party_merchant_no = value
    @property
    def third_party_trade_no(self):
        return self._third_party_trade_no

    @third_party_trade_no.setter
    def third_party_trade_no(self, value):
        self._third_party_trade_no = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.mrchind_app_id:
            if hasattr(self.mrchind_app_id, 'to_alipay_dict'):
                params['mrchind_app_id'] = self.mrchind_app_id.to_alipay_dict()
            else:
                params['mrchind_app_id'] = self.mrchind_app_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_merchant_no:
            if hasattr(self.out_merchant_no, 'to_alipay_dict'):
                params['out_merchant_no'] = self.out_merchant_no.to_alipay_dict()
            else:
                params['out_merchant_no'] = self.out_merchant_no
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.payer_bank_type:
            if hasattr(self.payer_bank_type, 'to_alipay_dict'):
                params['payer_bank_type'] = self.payer_bank_type.to_alipay_dict()
            else:
                params['payer_bank_type'] = self.payer_bank_type
        if self.payer_total_amount_on_the_merchant:
            if hasattr(self.payer_total_amount_on_the_merchant, 'to_alipay_dict'):
                params['payer_total_amount_on_the_merchant'] = self.payer_total_amount_on_the_merchant.to_alipay_dict()
            else:
                params['payer_total_amount_on_the_merchant'] = self.payer_total_amount_on_the_merchant
        if self.payer_total_count_on_the_merchant:
            if hasattr(self.payer_total_count_on_the_merchant, 'to_alipay_dict'):
                params['payer_total_count_on_the_merchant'] = self.payer_total_count_on_the_merchant.to_alipay_dict()
            else:
                params['payer_total_count_on_the_merchant'] = self.payer_total_count_on_the_merchant
        if self.payer_user_no:
            if hasattr(self.payer_user_no, 'to_alipay_dict'):
                params['payer_user_no'] = self.payer_user_no.to_alipay_dict()
            else:
                params['payer_user_no'] = self.payer_user_no
        if self.shop_code:
            if hasattr(self.shop_code, 'to_alipay_dict'):
                params['shop_code'] = self.shop_code.to_alipay_dict()
            else:
                params['shop_code'] = self.shop_code
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.third_party_merchant_no:
            if hasattr(self.third_party_merchant_no, 'to_alipay_dict'):
                params['third_party_merchant_no'] = self.third_party_merchant_no.to_alipay_dict()
            else:
                params['third_party_merchant_no'] = self.third_party_merchant_no
        if self.third_party_trade_no:
            if hasattr(self.third_party_trade_no, 'to_alipay_dict'):
                params['third_party_trade_no'] = self.third_party_trade_no.to_alipay_dict()
            else:
                params['third_party_trade_no'] = self.third_party_trade_no
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantIndirectAccountNotifyModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'mrchind_app_id' in d:
            o.mrchind_app_id = d['mrchind_app_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_merchant_no' in d:
            o.out_merchant_no = d['out_merchant_no']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'payer_bank_type' in d:
            o.payer_bank_type = d['payer_bank_type']
        if 'payer_total_amount_on_the_merchant' in d:
            o.payer_total_amount_on_the_merchant = d['payer_total_amount_on_the_merchant']
        if 'payer_total_count_on_the_merchant' in d:
            o.payer_total_count_on_the_merchant = d['payer_total_count_on_the_merchant']
        if 'payer_user_no' in d:
            o.payer_user_no = d['payer_user_no']
        if 'shop_code' in d:
            o.shop_code = d['shop_code']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'smid' in d:
            o.smid = d['smid']
        if 'third_party_merchant_no' in d:
            o.third_party_merchant_no = d['third_party_merchant_no']
        if 'third_party_trade_no' in d:
            o.third_party_trade_no = d['third_party_trade_no']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        return o


