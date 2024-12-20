#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayType import PayType


class AlipayMerchantTradeAccountNotifyModel(object):

    def __init__(self):
        self._cashier_id = None
        self._isv_app_id = None
        self._merchant_no = None
        self._out_biz_no = None
        self._payer_bank_type_list = None
        self._payer_total_amount = None
        self._payer_total_count = None
        self._payer_user_no = None
        self._payer_user_type = None
        self._shop_id = None
        self._shop_name = None
        self._sub_trade_channel = None
        self._third_party_merchant_no = None
        self._third_party_trade_no = None
        self._total_amount = None
        self._total_count = None
        self._trade_amount = None
        self._trade_channel = None
        self._trade_time = None

    @property
    def cashier_id(self):
        return self._cashier_id

    @cashier_id.setter
    def cashier_id(self, value):
        self._cashier_id = value
    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value
    @property
    def merchant_no(self):
        return self._merchant_no

    @merchant_no.setter
    def merchant_no(self, value):
        self._merchant_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payer_bank_type_list(self):
        return self._payer_bank_type_list

    @payer_bank_type_list.setter
    def payer_bank_type_list(self, value):
        if isinstance(value, list):
            self._payer_bank_type_list = list()
            for i in value:
                if isinstance(i, PayType):
                    self._payer_bank_type_list.append(i)
                else:
                    self._payer_bank_type_list.append(PayType.from_alipay_dict(i))
    @property
    def payer_total_amount(self):
        return self._payer_total_amount

    @payer_total_amount.setter
    def payer_total_amount(self, value):
        self._payer_total_amount = value
    @property
    def payer_total_count(self):
        return self._payer_total_count

    @payer_total_count.setter
    def payer_total_count(self, value):
        self._payer_total_count = value
    @property
    def payer_user_no(self):
        return self._payer_user_no

    @payer_user_no.setter
    def payer_user_no(self, value):
        self._payer_user_no = value
    @property
    def payer_user_type(self):
        return self._payer_user_type

    @payer_user_type.setter
    def payer_user_type(self, value):
        self._payer_user_type = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def sub_trade_channel(self):
        return self._sub_trade_channel

    @sub_trade_channel.setter
    def sub_trade_channel(self, value):
        self._sub_trade_channel = value
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
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_channel(self):
        return self._trade_channel

    @trade_channel.setter
    def trade_channel(self, value):
        self._trade_channel = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.cashier_id:
            if hasattr(self.cashier_id, 'to_alipay_dict'):
                params['cashier_id'] = self.cashier_id.to_alipay_dict()
            else:
                params['cashier_id'] = self.cashier_id
        if self.isv_app_id:
            if hasattr(self.isv_app_id, 'to_alipay_dict'):
                params['isv_app_id'] = self.isv_app_id.to_alipay_dict()
            else:
                params['isv_app_id'] = self.isv_app_id
        if self.merchant_no:
            if hasattr(self.merchant_no, 'to_alipay_dict'):
                params['merchant_no'] = self.merchant_no.to_alipay_dict()
            else:
                params['merchant_no'] = self.merchant_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payer_bank_type_list:
            if isinstance(self.payer_bank_type_list, list):
                for i in range(0, len(self.payer_bank_type_list)):
                    element = self.payer_bank_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payer_bank_type_list[i] = element.to_alipay_dict()
            if hasattr(self.payer_bank_type_list, 'to_alipay_dict'):
                params['payer_bank_type_list'] = self.payer_bank_type_list.to_alipay_dict()
            else:
                params['payer_bank_type_list'] = self.payer_bank_type_list
        if self.payer_total_amount:
            if hasattr(self.payer_total_amount, 'to_alipay_dict'):
                params['payer_total_amount'] = self.payer_total_amount.to_alipay_dict()
            else:
                params['payer_total_amount'] = self.payer_total_amount
        if self.payer_total_count:
            if hasattr(self.payer_total_count, 'to_alipay_dict'):
                params['payer_total_count'] = self.payer_total_count.to_alipay_dict()
            else:
                params['payer_total_count'] = self.payer_total_count
        if self.payer_user_no:
            if hasattr(self.payer_user_no, 'to_alipay_dict'):
                params['payer_user_no'] = self.payer_user_no.to_alipay_dict()
            else:
                params['payer_user_no'] = self.payer_user_no
        if self.payer_user_type:
            if hasattr(self.payer_user_type, 'to_alipay_dict'):
                params['payer_user_type'] = self.payer_user_type.to_alipay_dict()
            else:
                params['payer_user_type'] = self.payer_user_type
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.sub_trade_channel:
            if hasattr(self.sub_trade_channel, 'to_alipay_dict'):
                params['sub_trade_channel'] = self.sub_trade_channel.to_alipay_dict()
            else:
                params['sub_trade_channel'] = self.sub_trade_channel
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
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_channel:
            if hasattr(self.trade_channel, 'to_alipay_dict'):
                params['trade_channel'] = self.trade_channel.to_alipay_dict()
            else:
                params['trade_channel'] = self.trade_channel
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
        o = AlipayMerchantTradeAccountNotifyModel()
        if 'cashier_id' in d:
            o.cashier_id = d['cashier_id']
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        if 'merchant_no' in d:
            o.merchant_no = d['merchant_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payer_bank_type_list' in d:
            o.payer_bank_type_list = d['payer_bank_type_list']
        if 'payer_total_amount' in d:
            o.payer_total_amount = d['payer_total_amount']
        if 'payer_total_count' in d:
            o.payer_total_count = d['payer_total_count']
        if 'payer_user_no' in d:
            o.payer_user_no = d['payer_user_no']
        if 'payer_user_type' in d:
            o.payer_user_type = d['payer_user_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'sub_trade_channel' in d:
            o.sub_trade_channel = d['sub_trade_channel']
        if 'third_party_merchant_no' in d:
            o.third_party_merchant_no = d['third_party_merchant_no']
        if 'third_party_trade_no' in d:
            o.third_party_trade_no = d['third_party_trade_no']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_channel' in d:
            o.trade_channel = d['trade_channel']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        return o


