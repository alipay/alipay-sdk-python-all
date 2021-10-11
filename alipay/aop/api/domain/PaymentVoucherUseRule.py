#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaymentVoucherAvailableGoods import PaymentVoucherAvailableGoods
from alipay.aop.api.domain.PaymentVoucherAvailableMerchant import PaymentVoucherAvailableMerchant
from alipay.aop.api.domain.PaymentFixVoucher import PaymentFixVoucher
from alipay.aop.api.domain.PaymentVoucherValidPeriod import PaymentVoucherValidPeriod


class PaymentVoucherUseRule(object):

    def __init__(self):
        self._available_app_ids = None
        self._available_goods = None
        self._available_merchant = None
        self._available_store_ids = None
        self._fix_voucher = None
        self._unavailable_goods_ids = None
        self._use_mode = None
        self._use_url = None
        self._voucher_quantity_limit_per_user = None
        self._voucher_quantity_limit_per_user_period_type = None
        self._voucher_valid_period = None

    @property
    def available_app_ids(self):
        return self._available_app_ids

    @available_app_ids.setter
    def available_app_ids(self, value):
        if isinstance(value, list):
            self._available_app_ids = list()
            for i in value:
                self._available_app_ids.append(i)
    @property
    def available_goods(self):
        return self._available_goods

    @available_goods.setter
    def available_goods(self, value):
        if isinstance(value, PaymentVoucherAvailableGoods):
            self._available_goods = value
        else:
            self._available_goods = PaymentVoucherAvailableGoods.from_alipay_dict(value)
    @property
    def available_merchant(self):
        return self._available_merchant

    @available_merchant.setter
    def available_merchant(self, value):
        if isinstance(value, PaymentVoucherAvailableMerchant):
            self._available_merchant = value
        else:
            self._available_merchant = PaymentVoucherAvailableMerchant.from_alipay_dict(value)
    @property
    def available_store_ids(self):
        return self._available_store_ids

    @available_store_ids.setter
    def available_store_ids(self, value):
        if isinstance(value, list):
            self._available_store_ids = list()
            for i in value:
                self._available_store_ids.append(i)
    @property
    def fix_voucher(self):
        return self._fix_voucher

    @fix_voucher.setter
    def fix_voucher(self, value):
        if isinstance(value, PaymentFixVoucher):
            self._fix_voucher = value
        else:
            self._fix_voucher = PaymentFixVoucher.from_alipay_dict(value)
    @property
    def unavailable_goods_ids(self):
        return self._unavailable_goods_ids

    @unavailable_goods_ids.setter
    def unavailable_goods_ids(self, value):
        if isinstance(value, list):
            self._unavailable_goods_ids = list()
            for i in value:
                self._unavailable_goods_ids.append(i)
    @property
    def use_mode(self):
        return self._use_mode

    @use_mode.setter
    def use_mode(self, value):
        self._use_mode = value
    @property
    def use_url(self):
        return self._use_url

    @use_url.setter
    def use_url(self, value):
        self._use_url = value
    @property
    def voucher_quantity_limit_per_user(self):
        return self._voucher_quantity_limit_per_user

    @voucher_quantity_limit_per_user.setter
    def voucher_quantity_limit_per_user(self, value):
        self._voucher_quantity_limit_per_user = value
    @property
    def voucher_quantity_limit_per_user_period_type(self):
        return self._voucher_quantity_limit_per_user_period_type

    @voucher_quantity_limit_per_user_period_type.setter
    def voucher_quantity_limit_per_user_period_type(self, value):
        self._voucher_quantity_limit_per_user_period_type = value
    @property
    def voucher_valid_period(self):
        return self._voucher_valid_period

    @voucher_valid_period.setter
    def voucher_valid_period(self, value):
        if isinstance(value, PaymentVoucherValidPeriod):
            self._voucher_valid_period = value
        else:
            self._voucher_valid_period = PaymentVoucherValidPeriod.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.available_app_ids:
            if isinstance(self.available_app_ids, list):
                for i in range(0, len(self.available_app_ids)):
                    element = self.available_app_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_app_ids[i] = element.to_alipay_dict()
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
            if isinstance(self.available_store_ids, list):
                for i in range(0, len(self.available_store_ids)):
                    element = self.available_store_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_store_ids[i] = element.to_alipay_dict()
            if hasattr(self.available_store_ids, 'to_alipay_dict'):
                params['available_store_ids'] = self.available_store_ids.to_alipay_dict()
            else:
                params['available_store_ids'] = self.available_store_ids
        if self.fix_voucher:
            if hasattr(self.fix_voucher, 'to_alipay_dict'):
                params['fix_voucher'] = self.fix_voucher.to_alipay_dict()
            else:
                params['fix_voucher'] = self.fix_voucher
        if self.unavailable_goods_ids:
            if isinstance(self.unavailable_goods_ids, list):
                for i in range(0, len(self.unavailable_goods_ids)):
                    element = self.unavailable_goods_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.unavailable_goods_ids[i] = element.to_alipay_dict()
            if hasattr(self.unavailable_goods_ids, 'to_alipay_dict'):
                params['unavailable_goods_ids'] = self.unavailable_goods_ids.to_alipay_dict()
            else:
                params['unavailable_goods_ids'] = self.unavailable_goods_ids
        if self.use_mode:
            if hasattr(self.use_mode, 'to_alipay_dict'):
                params['use_mode'] = self.use_mode.to_alipay_dict()
            else:
                params['use_mode'] = self.use_mode
        if self.use_url:
            if hasattr(self.use_url, 'to_alipay_dict'):
                params['use_url'] = self.use_url.to_alipay_dict()
            else:
                params['use_url'] = self.use_url
        if self.voucher_quantity_limit_per_user:
            if hasattr(self.voucher_quantity_limit_per_user, 'to_alipay_dict'):
                params['voucher_quantity_limit_per_user'] = self.voucher_quantity_limit_per_user.to_alipay_dict()
            else:
                params['voucher_quantity_limit_per_user'] = self.voucher_quantity_limit_per_user
        if self.voucher_quantity_limit_per_user_period_type:
            if hasattr(self.voucher_quantity_limit_per_user_period_type, 'to_alipay_dict'):
                params['voucher_quantity_limit_per_user_period_type'] = self.voucher_quantity_limit_per_user_period_type.to_alipay_dict()
            else:
                params['voucher_quantity_limit_per_user_period_type'] = self.voucher_quantity_limit_per_user_period_type
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
        o = PaymentVoucherUseRule()
        if 'available_app_ids' in d:
            o.available_app_ids = d['available_app_ids']
        if 'available_goods' in d:
            o.available_goods = d['available_goods']
        if 'available_merchant' in d:
            o.available_merchant = d['available_merchant']
        if 'available_store_ids' in d:
            o.available_store_ids = d['available_store_ids']
        if 'fix_voucher' in d:
            o.fix_voucher = d['fix_voucher']
        if 'unavailable_goods_ids' in d:
            o.unavailable_goods_ids = d['unavailable_goods_ids']
        if 'use_mode' in d:
            o.use_mode = d['use_mode']
        if 'use_url' in d:
            o.use_url = d['use_url']
        if 'voucher_quantity_limit_per_user' in d:
            o.voucher_quantity_limit_per_user = d['voucher_quantity_limit_per_user']
        if 'voucher_quantity_limit_per_user_period_type' in d:
            o.voucher_quantity_limit_per_user_period_type = d['voucher_quantity_limit_per_user_period_type']
        if 'voucher_valid_period' in d:
            o.voucher_valid_period = d['voucher_valid_period']
        return o


