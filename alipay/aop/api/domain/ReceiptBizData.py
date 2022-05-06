#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReceiptDiscountInfo import ReceiptDiscountInfo
from alipay.aop.api.domain.ReceiptSku import ReceiptSku


class ReceiptBizData(object):

    def __init__(self):
        self._actual_pay_amount = None
        self._actual_pay_time = None
        self._change_amount = None
        self._currency = None
        self._fetch_num = None
        self._invoice_entry = None
        self._merchant_discount_amount = None
        self._merchant_name = None
        self._origin_amount = None
        self._other_discount_info = None
        self._out_biz_id = None
        self._out_trade_id = None
        self._pay_status = None
        self._platform_discount_amount = None
        self._shop_address = None
        self._shop_contract = None
        self._shop_name = None
        self._shop_type = None
        self._skus = None
        self._trade_id = None
        self._trade_source = None

    @property
    def actual_pay_amount(self):
        return self._actual_pay_amount

    @actual_pay_amount.setter
    def actual_pay_amount(self, value):
        self._actual_pay_amount = value
    @property
    def actual_pay_time(self):
        return self._actual_pay_time

    @actual_pay_time.setter
    def actual_pay_time(self, value):
        self._actual_pay_time = value
    @property
    def change_amount(self):
        return self._change_amount

    @change_amount.setter
    def change_amount(self, value):
        self._change_amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def fetch_num(self):
        return self._fetch_num

    @fetch_num.setter
    def fetch_num(self, value):
        self._fetch_num = value
    @property
    def invoice_entry(self):
        return self._invoice_entry

    @invoice_entry.setter
    def invoice_entry(self, value):
        self._invoice_entry = value
    @property
    def merchant_discount_amount(self):
        return self._merchant_discount_amount

    @merchant_discount_amount.setter
    def merchant_discount_amount(self, value):
        self._merchant_discount_amount = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def origin_amount(self):
        return self._origin_amount

    @origin_amount.setter
    def origin_amount(self, value):
        self._origin_amount = value
    @property
    def other_discount_info(self):
        return self._other_discount_info

    @other_discount_info.setter
    def other_discount_info(self, value):
        if isinstance(value, list):
            self._other_discount_info = list()
            for i in value:
                if isinstance(i, ReceiptDiscountInfo):
                    self._other_discount_info.append(i)
                else:
                    self._other_discount_info.append(ReceiptDiscountInfo.from_alipay_dict(i))
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def out_trade_id(self):
        return self._out_trade_id

    @out_trade_id.setter
    def out_trade_id(self, value):
        self._out_trade_id = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def platform_discount_amount(self):
        return self._platform_discount_amount

    @platform_discount_amount.setter
    def platform_discount_amount(self, value):
        self._platform_discount_amount = value
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        self._shop_address = value
    @property
    def shop_contract(self):
        return self._shop_contract

    @shop_contract.setter
    def shop_contract(self, value):
        self._shop_contract = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, ReceiptSku):
                    self._skus.append(i)
                else:
                    self._skus.append(ReceiptSku.from_alipay_dict(i))
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value
    @property
    def trade_source(self):
        return self._trade_source

    @trade_source.setter
    def trade_source(self, value):
        self._trade_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_pay_amount:
            if hasattr(self.actual_pay_amount, 'to_alipay_dict'):
                params['actual_pay_amount'] = self.actual_pay_amount.to_alipay_dict()
            else:
                params['actual_pay_amount'] = self.actual_pay_amount
        if self.actual_pay_time:
            if hasattr(self.actual_pay_time, 'to_alipay_dict'):
                params['actual_pay_time'] = self.actual_pay_time.to_alipay_dict()
            else:
                params['actual_pay_time'] = self.actual_pay_time
        if self.change_amount:
            if hasattr(self.change_amount, 'to_alipay_dict'):
                params['change_amount'] = self.change_amount.to_alipay_dict()
            else:
                params['change_amount'] = self.change_amount
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.fetch_num:
            if hasattr(self.fetch_num, 'to_alipay_dict'):
                params['fetch_num'] = self.fetch_num.to_alipay_dict()
            else:
                params['fetch_num'] = self.fetch_num
        if self.invoice_entry:
            if hasattr(self.invoice_entry, 'to_alipay_dict'):
                params['invoice_entry'] = self.invoice_entry.to_alipay_dict()
            else:
                params['invoice_entry'] = self.invoice_entry
        if self.merchant_discount_amount:
            if hasattr(self.merchant_discount_amount, 'to_alipay_dict'):
                params['merchant_discount_amount'] = self.merchant_discount_amount.to_alipay_dict()
            else:
                params['merchant_discount_amount'] = self.merchant_discount_amount
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.origin_amount:
            if hasattr(self.origin_amount, 'to_alipay_dict'):
                params['origin_amount'] = self.origin_amount.to_alipay_dict()
            else:
                params['origin_amount'] = self.origin_amount
        if self.other_discount_info:
            if isinstance(self.other_discount_info, list):
                for i in range(0, len(self.other_discount_info)):
                    element = self.other_discount_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_discount_info[i] = element.to_alipay_dict()
            if hasattr(self.other_discount_info, 'to_alipay_dict'):
                params['other_discount_info'] = self.other_discount_info.to_alipay_dict()
            else:
                params['other_discount_info'] = self.other_discount_info
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.out_trade_id:
            if hasattr(self.out_trade_id, 'to_alipay_dict'):
                params['out_trade_id'] = self.out_trade_id.to_alipay_dict()
            else:
                params['out_trade_id'] = self.out_trade_id
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.platform_discount_amount:
            if hasattr(self.platform_discount_amount, 'to_alipay_dict'):
                params['platform_discount_amount'] = self.platform_discount_amount.to_alipay_dict()
            else:
                params['platform_discount_amount'] = self.platform_discount_amount
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = self.shop_address.to_alipay_dict()
            else:
                params['shop_address'] = self.shop_address
        if self.shop_contract:
            if hasattr(self.shop_contract, 'to_alipay_dict'):
                params['shop_contract'] = self.shop_contract.to_alipay_dict()
            else:
                params['shop_contract'] = self.shop_contract
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        if self.skus:
            if isinstance(self.skus, list):
                for i in range(0, len(self.skus)):
                    element = self.skus[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skus[i] = element.to_alipay_dict()
            if hasattr(self.skus, 'to_alipay_dict'):
                params['skus'] = self.skus.to_alipay_dict()
            else:
                params['skus'] = self.skus
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        if self.trade_source:
            if hasattr(self.trade_source, 'to_alipay_dict'):
                params['trade_source'] = self.trade_source.to_alipay_dict()
            else:
                params['trade_source'] = self.trade_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReceiptBizData()
        if 'actual_pay_amount' in d:
            o.actual_pay_amount = d['actual_pay_amount']
        if 'actual_pay_time' in d:
            o.actual_pay_time = d['actual_pay_time']
        if 'change_amount' in d:
            o.change_amount = d['change_amount']
        if 'currency' in d:
            o.currency = d['currency']
        if 'fetch_num' in d:
            o.fetch_num = d['fetch_num']
        if 'invoice_entry' in d:
            o.invoice_entry = d['invoice_entry']
        if 'merchant_discount_amount' in d:
            o.merchant_discount_amount = d['merchant_discount_amount']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'origin_amount' in d:
            o.origin_amount = d['origin_amount']
        if 'other_discount_info' in d:
            o.other_discount_info = d['other_discount_info']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'out_trade_id' in d:
            o.out_trade_id = d['out_trade_id']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'platform_discount_amount' in d:
            o.platform_discount_amount = d['platform_discount_amount']
        if 'shop_address' in d:
            o.shop_address = d['shop_address']
        if 'shop_contract' in d:
            o.shop_contract = d['shop_contract']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'skus' in d:
            o.skus = d['skus']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        if 'trade_source' in d:
            o.trade_source = d['trade_source']
        return o


