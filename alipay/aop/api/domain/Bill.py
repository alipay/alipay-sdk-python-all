#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Bill(object):

    def __init__(self):
        self._bill_date = None
        self._bill_status = None
        self._bill_type = None
        self._biz_app_id = None
        self._currency = None
        self._discount_amount = None
        self._env_id = None
        self._env_name = None
        self._fee_item_name = None
        self._fee_item_unit = None
        self._original_unit_amount = None
        self._owed_amount = None
        self._paid_amount = None
        self._product_name = None
        self._trade_amount = None
        self._trade_total_amount = None
        self._usage = None

    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def env_name(self):
        return self._env_name

    @env_name.setter
    def env_name(self, value):
        self._env_name = value
    @property
    def fee_item_name(self):
        return self._fee_item_name

    @fee_item_name.setter
    def fee_item_name(self, value):
        self._fee_item_name = value
    @property
    def fee_item_unit(self):
        return self._fee_item_unit

    @fee_item_unit.setter
    def fee_item_unit(self, value):
        self._fee_item_unit = value
    @property
    def original_unit_amount(self):
        return self._original_unit_amount

    @original_unit_amount.setter
    def original_unit_amount(self, value):
        self._original_unit_amount = value
    @property
    def owed_amount(self):
        return self._owed_amount

    @owed_amount.setter
    def owed_amount(self, value):
        self._owed_amount = value
    @property
    def paid_amount(self):
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        self._paid_amount = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_total_amount(self):
        return self._trade_total_amount

    @trade_total_amount.setter
    def trade_total_amount(self, value):
        self._trade_total_amount = value
    @property
    def usage(self):
        return self._usage

    @usage.setter
    def usage(self, value):
        self._usage = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.bill_status:
            if hasattr(self.bill_status, 'to_alipay_dict'):
                params['bill_status'] = self.bill_status.to_alipay_dict()
            else:
                params['bill_status'] = self.bill_status
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.env_id:
            if hasattr(self.env_id, 'to_alipay_dict'):
                params['env_id'] = self.env_id.to_alipay_dict()
            else:
                params['env_id'] = self.env_id
        if self.env_name:
            if hasattr(self.env_name, 'to_alipay_dict'):
                params['env_name'] = self.env_name.to_alipay_dict()
            else:
                params['env_name'] = self.env_name
        if self.fee_item_name:
            if hasattr(self.fee_item_name, 'to_alipay_dict'):
                params['fee_item_name'] = self.fee_item_name.to_alipay_dict()
            else:
                params['fee_item_name'] = self.fee_item_name
        if self.fee_item_unit:
            if hasattr(self.fee_item_unit, 'to_alipay_dict'):
                params['fee_item_unit'] = self.fee_item_unit.to_alipay_dict()
            else:
                params['fee_item_unit'] = self.fee_item_unit
        if self.original_unit_amount:
            if hasattr(self.original_unit_amount, 'to_alipay_dict'):
                params['original_unit_amount'] = self.original_unit_amount.to_alipay_dict()
            else:
                params['original_unit_amount'] = self.original_unit_amount
        if self.owed_amount:
            if hasattr(self.owed_amount, 'to_alipay_dict'):
                params['owed_amount'] = self.owed_amount.to_alipay_dict()
            else:
                params['owed_amount'] = self.owed_amount
        if self.paid_amount:
            if hasattr(self.paid_amount, 'to_alipay_dict'):
                params['paid_amount'] = self.paid_amount.to_alipay_dict()
            else:
                params['paid_amount'] = self.paid_amount
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_total_amount:
            if hasattr(self.trade_total_amount, 'to_alipay_dict'):
                params['trade_total_amount'] = self.trade_total_amount.to_alipay_dict()
            else:
                params['trade_total_amount'] = self.trade_total_amount
        if self.usage:
            if hasattr(self.usage, 'to_alipay_dict'):
                params['usage'] = self.usage.to_alipay_dict()
            else:
                params['usage'] = self.usage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Bill()
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'bill_status' in d:
            o.bill_status = d['bill_status']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'currency' in d:
            o.currency = d['currency']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'env_name' in d:
            o.env_name = d['env_name']
        if 'fee_item_name' in d:
            o.fee_item_name = d['fee_item_name']
        if 'fee_item_unit' in d:
            o.fee_item_unit = d['fee_item_unit']
        if 'original_unit_amount' in d:
            o.original_unit_amount = d['original_unit_amount']
        if 'owed_amount' in d:
            o.owed_amount = d['owed_amount']
        if 'paid_amount' in d:
            o.paid_amount = d['paid_amount']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_total_amount' in d:
            o.trade_total_amount = d['trade_total_amount']
        if 'usage' in d:
            o.usage = d['usage']
        return o


