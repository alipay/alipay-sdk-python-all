#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPriceDetail(object):

    def __init__(self):
        self._buyout_price = None
        self._deposit_price = None
        self._finish_real_rent_price = None
        self._initial_rent_price = None
        self._period_num = None
        self._period_real_rent_price = None
        self._pre_authorization_amount = None
        self._real_pay_amount = None
        self._rent_end_time = None
        self._rent_start_time = None

    @property
    def buyout_price(self):
        return self._buyout_price

    @buyout_price.setter
    def buyout_price(self, value):
        self._buyout_price = value
    @property
    def deposit_price(self):
        return self._deposit_price

    @deposit_price.setter
    def deposit_price(self, value):
        self._deposit_price = value
    @property
    def finish_real_rent_price(self):
        return self._finish_real_rent_price

    @finish_real_rent_price.setter
    def finish_real_rent_price(self, value):
        self._finish_real_rent_price = value
    @property
    def initial_rent_price(self):
        return self._initial_rent_price

    @initial_rent_price.setter
    def initial_rent_price(self, value):
        self._initial_rent_price = value
    @property
    def period_num(self):
        return self._period_num

    @period_num.setter
    def period_num(self, value):
        self._period_num = value
    @property
    def period_real_rent_price(self):
        return self._period_real_rent_price

    @period_real_rent_price.setter
    def period_real_rent_price(self, value):
        self._period_real_rent_price = value
    @property
    def pre_authorization_amount(self):
        return self._pre_authorization_amount

    @pre_authorization_amount.setter
    def pre_authorization_amount(self, value):
        self._pre_authorization_amount = value
    @property
    def real_pay_amount(self):
        return self._real_pay_amount

    @real_pay_amount.setter
    def real_pay_amount(self, value):
        self._real_pay_amount = value
    @property
    def rent_end_time(self):
        return self._rent_end_time

    @rent_end_time.setter
    def rent_end_time(self, value):
        self._rent_end_time = value
    @property
    def rent_start_time(self):
        return self._rent_start_time

    @rent_start_time.setter
    def rent_start_time(self, value):
        self._rent_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyout_price:
            if hasattr(self.buyout_price, 'to_alipay_dict'):
                params['buyout_price'] = self.buyout_price.to_alipay_dict()
            else:
                params['buyout_price'] = self.buyout_price
        if self.deposit_price:
            if hasattr(self.deposit_price, 'to_alipay_dict'):
                params['deposit_price'] = self.deposit_price.to_alipay_dict()
            else:
                params['deposit_price'] = self.deposit_price
        if self.finish_real_rent_price:
            if hasattr(self.finish_real_rent_price, 'to_alipay_dict'):
                params['finish_real_rent_price'] = self.finish_real_rent_price.to_alipay_dict()
            else:
                params['finish_real_rent_price'] = self.finish_real_rent_price
        if self.initial_rent_price:
            if hasattr(self.initial_rent_price, 'to_alipay_dict'):
                params['initial_rent_price'] = self.initial_rent_price.to_alipay_dict()
            else:
                params['initial_rent_price'] = self.initial_rent_price
        if self.period_num:
            if hasattr(self.period_num, 'to_alipay_dict'):
                params['period_num'] = self.period_num.to_alipay_dict()
            else:
                params['period_num'] = self.period_num
        if self.period_real_rent_price:
            if hasattr(self.period_real_rent_price, 'to_alipay_dict'):
                params['period_real_rent_price'] = self.period_real_rent_price.to_alipay_dict()
            else:
                params['period_real_rent_price'] = self.period_real_rent_price
        if self.pre_authorization_amount:
            if hasattr(self.pre_authorization_amount, 'to_alipay_dict'):
                params['pre_authorization_amount'] = self.pre_authorization_amount.to_alipay_dict()
            else:
                params['pre_authorization_amount'] = self.pre_authorization_amount
        if self.real_pay_amount:
            if hasattr(self.real_pay_amount, 'to_alipay_dict'):
                params['real_pay_amount'] = self.real_pay_amount.to_alipay_dict()
            else:
                params['real_pay_amount'] = self.real_pay_amount
        if self.rent_end_time:
            if hasattr(self.rent_end_time, 'to_alipay_dict'):
                params['rent_end_time'] = self.rent_end_time.to_alipay_dict()
            else:
                params['rent_end_time'] = self.rent_end_time
        if self.rent_start_time:
            if hasattr(self.rent_start_time, 'to_alipay_dict'):
                params['rent_start_time'] = self.rent_start_time.to_alipay_dict()
            else:
                params['rent_start_time'] = self.rent_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPriceDetail()
        if 'buyout_price' in d:
            o.buyout_price = d['buyout_price']
        if 'deposit_price' in d:
            o.deposit_price = d['deposit_price']
        if 'finish_real_rent_price' in d:
            o.finish_real_rent_price = d['finish_real_rent_price']
        if 'initial_rent_price' in d:
            o.initial_rent_price = d['initial_rent_price']
        if 'period_num' in d:
            o.period_num = d['period_num']
        if 'period_real_rent_price' in d:
            o.period_real_rent_price = d['period_real_rent_price']
        if 'pre_authorization_amount' in d:
            o.pre_authorization_amount = d['pre_authorization_amount']
        if 'real_pay_amount' in d:
            o.real_pay_amount = d['real_pay_amount']
        if 'rent_end_time' in d:
            o.rent_end_time = d['rent_end_time']
        if 'rent_start_time' in d:
            o.rent_start_time = d['rent_start_time']
        return o


