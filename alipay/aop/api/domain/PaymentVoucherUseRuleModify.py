#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaymentVoucherAvailableGoodsModify import PaymentVoucherAvailableGoodsModify
from alipay.aop.api.domain.PaymentVoucherAvailableMerchantModify import PaymentVoucherAvailableMerchantModify
from alipay.aop.api.domain.PaymentVoucherValidPeriodModify import PaymentVoucherValidPeriodModify


class PaymentVoucherUseRuleModify(object):

    def __init__(self):
        self._available_app_ids = None
        self._available_goods = None
        self._available_merchant = None
        self._available_store_ids = None
        self._voucher_valid_period = None

    @property
    def available_app_ids(self):
        return self._available_app_ids

    @available_app_ids.setter
    def available_app_ids(self, value):
        self._available_app_ids = value
    @property
    def available_goods(self):
        return self._available_goods

    @available_goods.setter
    def available_goods(self, value):
        if isinstance(value, PaymentVoucherAvailableGoodsModify):
            self._available_goods = value
        else:
            self._available_goods = PaymentVoucherAvailableGoodsModify.from_alipay_dict(value)
    @property
    def available_merchant(self):
        return self._available_merchant

    @available_merchant.setter
    def available_merchant(self, value):
        if isinstance(value, PaymentVoucherAvailableMerchantModify):
            self._available_merchant = value
        else:
            self._available_merchant = PaymentVoucherAvailableMerchantModify.from_alipay_dict(value)
    @property
    def available_store_ids(self):
        return self._available_store_ids

    @available_store_ids.setter
    def available_store_ids(self, value):
        self._available_store_ids = value
    @property
    def voucher_valid_period(self):
        return self._voucher_valid_period

    @voucher_valid_period.setter
    def voucher_valid_period(self, value):
        if isinstance(value, PaymentVoucherValidPeriodModify):
            self._voucher_valid_period = value
        else:
            self._voucher_valid_period = PaymentVoucherValidPeriodModify.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.available_app_ids:
            if hasattr(self.available_app_ids, 'to_alipay_dict'):
                params['available_app_ids'] = self.available_app_ids.to_alipay_dict()
            else:
                params['available_app_ids'] = self.available_app_ids
        if self.available_goods:
            if hasattr(self.available_goods, 'to_alipay_dict'):
                params['available_goods'] = self.available_goods.to_alipay_dict()
            else:
                params['available_goods'] = self.available_goods
        if self.available_merchant:
            if hasattr(self.available_merchant, 'to_alipay_dict'):
                params['available_merchant'] = self.available_merchant.to_alipay_dict()
            else:
                params['available_merchant'] = self.available_merchant
        if self.available_store_ids:
            if hasattr(self.available_store_ids, 'to_alipay_dict'):
                params['available_store_ids'] = self.available_store_ids.to_alipay_dict()
            else:
                params['available_store_ids'] = self.available_store_ids
        if self.voucher_valid_period:
            if hasattr(self.voucher_valid_period, 'to_alipay_dict'):
                params['voucher_valid_period'] = self.voucher_valid_period.to_alipay_dict()
            else:
                params['voucher_valid_period'] = self.voucher_valid_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentVoucherUseRuleModify()
        if 'available_app_ids' in d:
            o.available_app_ids = d['available_app_ids']
        if 'available_goods' in d:
            o.available_goods = d['available_goods']
        if 'available_merchant' in d:
            o.available_merchant = d['available_merchant']
        if 'available_store_ids' in d:
            o.available_store_ids = d['available_store_ids']
        if 'voucher_valid_period' in d:
            o.voucher_valid_period = d['voucher_valid_period']
        return o


