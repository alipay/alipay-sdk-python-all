#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomerDefineVoucherInfo import CustomerDefineVoucherInfo
from alipay.aop.api.domain.DiscountVoucherInfo import DiscountVoucherInfo
from alipay.aop.api.domain.ExchangeVoucherInfo import ExchangeVoucherInfo
from alipay.aop.api.domain.FixVoucherInfo import FixVoucherInfo
from alipay.aop.api.domain.SpecialVoucherInfo import SpecialVoucherInfo


class VoucherDeductInfo(object):

    def __init__(self):
        self._customer_define_voucher_info = None
        self._discount_voucher_info = None
        self._exchange_voucher_info = None
        self._fix_voucher_info = None
        self._special_voucher_info = None
        self._voucher_type = None

    @property
    def customer_define_voucher_info(self):
        return self._customer_define_voucher_info

    @customer_define_voucher_info.setter
    def customer_define_voucher_info(self, value):
        if isinstance(value, CustomerDefineVoucherInfo):
            self._customer_define_voucher_info = value
        else:
            self._customer_define_voucher_info = CustomerDefineVoucherInfo.from_alipay_dict(value)
    @property
    def discount_voucher_info(self):
        return self._discount_voucher_info

    @discount_voucher_info.setter
    def discount_voucher_info(self, value):
        if isinstance(value, DiscountVoucherInfo):
            self._discount_voucher_info = value
        else:
            self._discount_voucher_info = DiscountVoucherInfo.from_alipay_dict(value)
    @property
    def exchange_voucher_info(self):
        return self._exchange_voucher_info

    @exchange_voucher_info.setter
    def exchange_voucher_info(self, value):
        if isinstance(value, ExchangeVoucherInfo):
            self._exchange_voucher_info = value
        else:
            self._exchange_voucher_info = ExchangeVoucherInfo.from_alipay_dict(value)
    @property
    def fix_voucher_info(self):
        return self._fix_voucher_info

    @fix_voucher_info.setter
    def fix_voucher_info(self, value):
        if isinstance(value, FixVoucherInfo):
            self._fix_voucher_info = value
        else:
            self._fix_voucher_info = FixVoucherInfo.from_alipay_dict(value)
    @property
    def special_voucher_info(self):
        return self._special_voucher_info

    @special_voucher_info.setter
    def special_voucher_info(self, value):
        if isinstance(value, SpecialVoucherInfo):
            self._special_voucher_info = value
        else:
            self._special_voucher_info = SpecialVoucherInfo.from_alipay_dict(value)
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_define_voucher_info:
            if hasattr(self.customer_define_voucher_info, 'to_alipay_dict'):
                params['customer_define_voucher_info'] = self.customer_define_voucher_info.to_alipay_dict()
            else:
                params['customer_define_voucher_info'] = self.customer_define_voucher_info
        if self.discount_voucher_info:
            if hasattr(self.discount_voucher_info, 'to_alipay_dict'):
                params['discount_voucher_info'] = self.discount_voucher_info.to_alipay_dict()
            else:
                params['discount_voucher_info'] = self.discount_voucher_info
        if self.exchange_voucher_info:
            if hasattr(self.exchange_voucher_info, 'to_alipay_dict'):
                params['exchange_voucher_info'] = self.exchange_voucher_info.to_alipay_dict()
            else:
                params['exchange_voucher_info'] = self.exchange_voucher_info
        if self.fix_voucher_info:
            if hasattr(self.fix_voucher_info, 'to_alipay_dict'):
                params['fix_voucher_info'] = self.fix_voucher_info.to_alipay_dict()
            else:
                params['fix_voucher_info'] = self.fix_voucher_info
        if self.special_voucher_info:
            if hasattr(self.special_voucher_info, 'to_alipay_dict'):
                params['special_voucher_info'] = self.special_voucher_info.to_alipay_dict()
            else:
                params['special_voucher_info'] = self.special_voucher_info
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherDeductInfo()
        if 'customer_define_voucher_info' in d:
            o.customer_define_voucher_info = d['customer_define_voucher_info']
        if 'discount_voucher_info' in d:
            o.discount_voucher_info = d['discount_voucher_info']
        if 'exchange_voucher_info' in d:
            o.exchange_voucher_info = d['exchange_voucher_info']
        if 'fix_voucher_info' in d:
            o.fix_voucher_info = d['fix_voucher_info']
        if 'special_voucher_info' in d:
            o.special_voucher_info = d['special_voucher_info']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


