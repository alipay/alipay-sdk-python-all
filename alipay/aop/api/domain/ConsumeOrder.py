#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumeOrder(object):

    def __init__(self):
        self._bill_amount = None
        self._bill_type = None
        self._biz_app_id = None
        self._biz_env_id = None
        self._biz_env_name = None
        self._biz_mth = None
        self._currency = None
        self._discount_amount = None
        self._fee_item_code = None
        self._fee_item_name = None
        self._nonpayment_amount = None
        self._order_no = None
        self._origin_bill_amount = None
        self._product_code = None
        self._product_name = None
        self._real_amount = None
        self._spec_instance_id = None
        self._wallet_source = None
        self._wallet_source_id = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
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
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def biz_env_name(self):
        return self._biz_env_name

    @biz_env_name.setter
    def biz_env_name(self, value):
        self._biz_env_name = value
    @property
    def biz_mth(self):
        return self._biz_mth

    @biz_mth.setter
    def biz_mth(self, value):
        self._biz_mth = value
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
    def fee_item_code(self):
        return self._fee_item_code

    @fee_item_code.setter
    def fee_item_code(self, value):
        self._fee_item_code = value
    @property
    def fee_item_name(self):
        return self._fee_item_name

    @fee_item_name.setter
    def fee_item_name(self, value):
        self._fee_item_name = value
    @property
    def nonpayment_amount(self):
        return self._nonpayment_amount

    @nonpayment_amount.setter
    def nonpayment_amount(self, value):
        self._nonpayment_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def origin_bill_amount(self):
        return self._origin_bill_amount

    @origin_bill_amount.setter
    def origin_bill_amount(self, value):
        self._origin_bill_amount = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def spec_instance_id(self):
        return self._spec_instance_id

    @spec_instance_id.setter
    def spec_instance_id(self, value):
        self._spec_instance_id = value
    @property
    def wallet_source(self):
        return self._wallet_source

    @wallet_source.setter
    def wallet_source(self, value):
        self._wallet_source = value
    @property
    def wallet_source_id(self):
        return self._wallet_source_id

    @wallet_source_id.setter
    def wallet_source_id(self, value):
        self._wallet_source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
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
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.biz_env_name:
            if hasattr(self.biz_env_name, 'to_alipay_dict'):
                params['biz_env_name'] = self.biz_env_name.to_alipay_dict()
            else:
                params['biz_env_name'] = self.biz_env_name
        if self.biz_mth:
            if hasattr(self.biz_mth, 'to_alipay_dict'):
                params['biz_mth'] = self.biz_mth.to_alipay_dict()
            else:
                params['biz_mth'] = self.biz_mth
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
        if self.fee_item_code:
            if hasattr(self.fee_item_code, 'to_alipay_dict'):
                params['fee_item_code'] = self.fee_item_code.to_alipay_dict()
            else:
                params['fee_item_code'] = self.fee_item_code
        if self.fee_item_name:
            if hasattr(self.fee_item_name, 'to_alipay_dict'):
                params['fee_item_name'] = self.fee_item_name.to_alipay_dict()
            else:
                params['fee_item_name'] = self.fee_item_name
        if self.nonpayment_amount:
            if hasattr(self.nonpayment_amount, 'to_alipay_dict'):
                params['nonpayment_amount'] = self.nonpayment_amount.to_alipay_dict()
            else:
                params['nonpayment_amount'] = self.nonpayment_amount
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.origin_bill_amount:
            if hasattr(self.origin_bill_amount, 'to_alipay_dict'):
                params['origin_bill_amount'] = self.origin_bill_amount.to_alipay_dict()
            else:
                params['origin_bill_amount'] = self.origin_bill_amount
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.spec_instance_id:
            if hasattr(self.spec_instance_id, 'to_alipay_dict'):
                params['spec_instance_id'] = self.spec_instance_id.to_alipay_dict()
            else:
                params['spec_instance_id'] = self.spec_instance_id
        if self.wallet_source:
            if hasattr(self.wallet_source, 'to_alipay_dict'):
                params['wallet_source'] = self.wallet_source.to_alipay_dict()
            else:
                params['wallet_source'] = self.wallet_source
        if self.wallet_source_id:
            if hasattr(self.wallet_source_id, 'to_alipay_dict'):
                params['wallet_source_id'] = self.wallet_source_id.to_alipay_dict()
            else:
                params['wallet_source_id'] = self.wallet_source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumeOrder()
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'biz_env_name' in d:
            o.biz_env_name = d['biz_env_name']
        if 'biz_mth' in d:
            o.biz_mth = d['biz_mth']
        if 'currency' in d:
            o.currency = d['currency']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'fee_item_code' in d:
            o.fee_item_code = d['fee_item_code']
        if 'fee_item_name' in d:
            o.fee_item_name = d['fee_item_name']
        if 'nonpayment_amount' in d:
            o.nonpayment_amount = d['nonpayment_amount']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'origin_bill_amount' in d:
            o.origin_bill_amount = d['origin_bill_amount']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'spec_instance_id' in d:
            o.spec_instance_id = d['spec_instance_id']
        if 'wallet_source' in d:
            o.wallet_source = d['wallet_source']
        if 'wallet_source_id' in d:
            o.wallet_source_id = d['wallet_source_id']
        return o


