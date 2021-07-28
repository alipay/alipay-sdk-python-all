#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherSendRule(object):

    def __init__(self):
        self._natural_person_limit = None
        self._phone_number_limit = None
        self._voucher_quantity = None
        self._voucher_single_restriction = None

    @property
    def natural_person_limit(self):
        return self._natural_person_limit

    @natural_person_limit.setter
    def natural_person_limit(self, value):
        self._natural_person_limit = value
    @property
    def phone_number_limit(self):
        return self._phone_number_limit

    @phone_number_limit.setter
    def phone_number_limit(self, value):
        self._phone_number_limit = value
    @property
    def voucher_quantity(self):
        return self._voucher_quantity

    @voucher_quantity.setter
    def voucher_quantity(self, value):
        self._voucher_quantity = value
    @property
    def voucher_single_restriction(self):
        return self._voucher_single_restriction

    @voucher_single_restriction.setter
    def voucher_single_restriction(self, value):
        self._voucher_single_restriction = value


    def to_alipay_dict(self):
        params = dict()
        if self.natural_person_limit:
            if hasattr(self.natural_person_limit, 'to_alipay_dict'):
                params['natural_person_limit'] = self.natural_person_limit.to_alipay_dict()
            else:
                params['natural_person_limit'] = self.natural_person_limit
        if self.phone_number_limit:
            if hasattr(self.phone_number_limit, 'to_alipay_dict'):
                params['phone_number_limit'] = self.phone_number_limit.to_alipay_dict()
            else:
                params['phone_number_limit'] = self.phone_number_limit
        if self.voucher_quantity:
            if hasattr(self.voucher_quantity, 'to_alipay_dict'):
                params['voucher_quantity'] = self.voucher_quantity.to_alipay_dict()
            else:
                params['voucher_quantity'] = self.voucher_quantity
        if self.voucher_single_restriction:
            if hasattr(self.voucher_single_restriction, 'to_alipay_dict'):
                params['voucher_single_restriction'] = self.voucher_single_restriction.to_alipay_dict()
            else:
                params['voucher_single_restriction'] = self.voucher_single_restriction
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherSendRule()
        if 'natural_person_limit' in d:
            o.natural_person_limit = d['natural_person_limit']
        if 'phone_number_limit' in d:
            o.phone_number_limit = d['phone_number_limit']
        if 'voucher_quantity' in d:
            o.voucher_quantity = d['voucher_quantity']
        if 'voucher_single_restriction' in d:
            o.voucher_single_restriction = d['voucher_single_restriction']
        return o


