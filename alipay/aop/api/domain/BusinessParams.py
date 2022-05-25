#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessParams(object):

    def __init__(self):
        self._actual_order_time = None
        self._campus_card = None
        self._card_type = None
        self._enterprise_pay_amount = None
        self._enterprise_pay_info = None
        self._good_taxes = None

    @property
    def actual_order_time(self):
        return self._actual_order_time

    @actual_order_time.setter
    def actual_order_time(self, value):
        self._actual_order_time = value
    @property
    def campus_card(self):
        return self._campus_card

    @campus_card.setter
    def campus_card(self, value):
        self._campus_card = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def enterprise_pay_amount(self):
        return self._enterprise_pay_amount

    @enterprise_pay_amount.setter
    def enterprise_pay_amount(self, value):
        self._enterprise_pay_amount = value
    @property
    def enterprise_pay_info(self):
        return self._enterprise_pay_info

    @enterprise_pay_info.setter
    def enterprise_pay_info(self, value):
        self._enterprise_pay_info = value
    @property
    def good_taxes(self):
        return self._good_taxes

    @good_taxes.setter
    def good_taxes(self, value):
        self._good_taxes = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_order_time:
            if hasattr(self.actual_order_time, 'to_alipay_dict'):
                params['actual_order_time'] = self.actual_order_time.to_alipay_dict()
            else:
                params['actual_order_time'] = self.actual_order_time
        if self.campus_card:
            if hasattr(self.campus_card, 'to_alipay_dict'):
                params['campus_card'] = self.campus_card.to_alipay_dict()
            else:
                params['campus_card'] = self.campus_card
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.enterprise_pay_amount:
            if hasattr(self.enterprise_pay_amount, 'to_alipay_dict'):
                params['enterprise_pay_amount'] = self.enterprise_pay_amount.to_alipay_dict()
            else:
                params['enterprise_pay_amount'] = self.enterprise_pay_amount
        if self.enterprise_pay_info:
            if hasattr(self.enterprise_pay_info, 'to_alipay_dict'):
                params['enterprise_pay_info'] = self.enterprise_pay_info.to_alipay_dict()
            else:
                params['enterprise_pay_info'] = self.enterprise_pay_info
        if self.good_taxes:
            if hasattr(self.good_taxes, 'to_alipay_dict'):
                params['good_taxes'] = self.good_taxes.to_alipay_dict()
            else:
                params['good_taxes'] = self.good_taxes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessParams()
        if 'actual_order_time' in d:
            o.actual_order_time = d['actual_order_time']
        if 'campus_card' in d:
            o.campus_card = d['campus_card']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'enterprise_pay_amount' in d:
            o.enterprise_pay_amount = d['enterprise_pay_amount']
        if 'enterprise_pay_info' in d:
            o.enterprise_pay_info = d['enterprise_pay_info']
        if 'good_taxes' in d:
            o.good_taxes = d['good_taxes']
        return o


