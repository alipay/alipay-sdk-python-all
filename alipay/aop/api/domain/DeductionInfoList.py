#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeductionInfoList(object):

    def __init__(self):
        self._can_one_time_buy = None
        self._item_type = None
        self._merchant_discount_amount = None
        self._merchant_no_fund_amount = None
        self._other_discount_amount = None
        self._platform_discount_amount = None
        self._receipt_amount = None
        self._source_amount = None
        self._source_certificate_code = None
        self._source_certificate_id = None
        self._source_order_id = None
        self._source_selling_price = None
        self._source_sku_id = None
        self._source_sku_name = None
        self._source_user_pay_amount = None
        self._use_order_no = None

    @property
    def can_one_time_buy(self):
        return self._can_one_time_buy

    @can_one_time_buy.setter
    def can_one_time_buy(self, value):
        self._can_one_time_buy = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def merchant_discount_amount(self):
        return self._merchant_discount_amount

    @merchant_discount_amount.setter
    def merchant_discount_amount(self, value):
        self._merchant_discount_amount = value
    @property
    def merchant_no_fund_amount(self):
        return self._merchant_no_fund_amount

    @merchant_no_fund_amount.setter
    def merchant_no_fund_amount(self, value):
        self._merchant_no_fund_amount = value
    @property
    def other_discount_amount(self):
        return self._other_discount_amount

    @other_discount_amount.setter
    def other_discount_amount(self, value):
        self._other_discount_amount = value
    @property
    def platform_discount_amount(self):
        return self._platform_discount_amount

    @platform_discount_amount.setter
    def platform_discount_amount(self, value):
        self._platform_discount_amount = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def source_amount(self):
        return self._source_amount

    @source_amount.setter
    def source_amount(self, value):
        self._source_amount = value
    @property
    def source_certificate_code(self):
        return self._source_certificate_code

    @source_certificate_code.setter
    def source_certificate_code(self, value):
        self._source_certificate_code = value
    @property
    def source_certificate_id(self):
        return self._source_certificate_id

    @source_certificate_id.setter
    def source_certificate_id(self, value):
        self._source_certificate_id = value
    @property
    def source_order_id(self):
        return self._source_order_id

    @source_order_id.setter
    def source_order_id(self, value):
        self._source_order_id = value
    @property
    def source_selling_price(self):
        return self._source_selling_price

    @source_selling_price.setter
    def source_selling_price(self, value):
        self._source_selling_price = value
    @property
    def source_sku_id(self):
        return self._source_sku_id

    @source_sku_id.setter
    def source_sku_id(self, value):
        self._source_sku_id = value
    @property
    def source_sku_name(self):
        return self._source_sku_name

    @source_sku_name.setter
    def source_sku_name(self, value):
        self._source_sku_name = value
    @property
    def source_user_pay_amount(self):
        return self._source_user_pay_amount

    @source_user_pay_amount.setter
    def source_user_pay_amount(self, value):
        self._source_user_pay_amount = value
    @property
    def use_order_no(self):
        return self._use_order_no

    @use_order_no.setter
    def use_order_no(self, value):
        self._use_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_one_time_buy:
            if hasattr(self.can_one_time_buy, 'to_alipay_dict'):
                params['can_one_time_buy'] = self.can_one_time_buy.to_alipay_dict()
            else:
                params['can_one_time_buy'] = self.can_one_time_buy
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.merchant_discount_amount:
            if hasattr(self.merchant_discount_amount, 'to_alipay_dict'):
                params['merchant_discount_amount'] = self.merchant_discount_amount.to_alipay_dict()
            else:
                params['merchant_discount_amount'] = self.merchant_discount_amount
        if self.merchant_no_fund_amount:
            if hasattr(self.merchant_no_fund_amount, 'to_alipay_dict'):
                params['merchant_no_fund_amount'] = self.merchant_no_fund_amount.to_alipay_dict()
            else:
                params['merchant_no_fund_amount'] = self.merchant_no_fund_amount
        if self.other_discount_amount:
            if hasattr(self.other_discount_amount, 'to_alipay_dict'):
                params['other_discount_amount'] = self.other_discount_amount.to_alipay_dict()
            else:
                params['other_discount_amount'] = self.other_discount_amount
        if self.platform_discount_amount:
            if hasattr(self.platform_discount_amount, 'to_alipay_dict'):
                params['platform_discount_amount'] = self.platform_discount_amount.to_alipay_dict()
            else:
                params['platform_discount_amount'] = self.platform_discount_amount
        if self.receipt_amount:
            if hasattr(self.receipt_amount, 'to_alipay_dict'):
                params['receipt_amount'] = self.receipt_amount.to_alipay_dict()
            else:
                params['receipt_amount'] = self.receipt_amount
        if self.source_amount:
            if hasattr(self.source_amount, 'to_alipay_dict'):
                params['source_amount'] = self.source_amount.to_alipay_dict()
            else:
                params['source_amount'] = self.source_amount
        if self.source_certificate_code:
            if hasattr(self.source_certificate_code, 'to_alipay_dict'):
                params['source_certificate_code'] = self.source_certificate_code.to_alipay_dict()
            else:
                params['source_certificate_code'] = self.source_certificate_code
        if self.source_certificate_id:
            if hasattr(self.source_certificate_id, 'to_alipay_dict'):
                params['source_certificate_id'] = self.source_certificate_id.to_alipay_dict()
            else:
                params['source_certificate_id'] = self.source_certificate_id
        if self.source_order_id:
            if hasattr(self.source_order_id, 'to_alipay_dict'):
                params['source_order_id'] = self.source_order_id.to_alipay_dict()
            else:
                params['source_order_id'] = self.source_order_id
        if self.source_selling_price:
            if hasattr(self.source_selling_price, 'to_alipay_dict'):
                params['source_selling_price'] = self.source_selling_price.to_alipay_dict()
            else:
                params['source_selling_price'] = self.source_selling_price
        if self.source_sku_id:
            if hasattr(self.source_sku_id, 'to_alipay_dict'):
                params['source_sku_id'] = self.source_sku_id.to_alipay_dict()
            else:
                params['source_sku_id'] = self.source_sku_id
        if self.source_sku_name:
            if hasattr(self.source_sku_name, 'to_alipay_dict'):
                params['source_sku_name'] = self.source_sku_name.to_alipay_dict()
            else:
                params['source_sku_name'] = self.source_sku_name
        if self.source_user_pay_amount:
            if hasattr(self.source_user_pay_amount, 'to_alipay_dict'):
                params['source_user_pay_amount'] = self.source_user_pay_amount.to_alipay_dict()
            else:
                params['source_user_pay_amount'] = self.source_user_pay_amount
        if self.use_order_no:
            if hasattr(self.use_order_no, 'to_alipay_dict'):
                params['use_order_no'] = self.use_order_no.to_alipay_dict()
            else:
                params['use_order_no'] = self.use_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeductionInfoList()
        if 'can_one_time_buy' in d:
            o.can_one_time_buy = d['can_one_time_buy']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'merchant_discount_amount' in d:
            o.merchant_discount_amount = d['merchant_discount_amount']
        if 'merchant_no_fund_amount' in d:
            o.merchant_no_fund_amount = d['merchant_no_fund_amount']
        if 'other_discount_amount' in d:
            o.other_discount_amount = d['other_discount_amount']
        if 'platform_discount_amount' in d:
            o.platform_discount_amount = d['platform_discount_amount']
        if 'receipt_amount' in d:
            o.receipt_amount = d['receipt_amount']
        if 'source_amount' in d:
            o.source_amount = d['source_amount']
        if 'source_certificate_code' in d:
            o.source_certificate_code = d['source_certificate_code']
        if 'source_certificate_id' in d:
            o.source_certificate_id = d['source_certificate_id']
        if 'source_order_id' in d:
            o.source_order_id = d['source_order_id']
        if 'source_selling_price' in d:
            o.source_selling_price = d['source_selling_price']
        if 'source_sku_id' in d:
            o.source_sku_id = d['source_sku_id']
        if 'source_sku_name' in d:
            o.source_sku_name = d['source_sku_name']
        if 'source_user_pay_amount' in d:
            o.source_user_pay_amount = d['source_user_pay_amount']
        if 'use_order_no' in d:
            o.use_order_no = d['use_order_no']
        return o


