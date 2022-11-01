#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GiftCardTemplate(object):

    def __init__(self):
        self._business_params = None
        self._denomination = None
        self._effective_end_date = None
        self._effective_period = None
        self._effective_start_date = None
        self._end_date = None
        self._gift_card_template_name = None
        self._price = None
        self._settle_account_no = None
        self._start_date = None
        self._stock_num = None
        self._valid_date = None
        self._valid_period = None
        self._valid_type = None

    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        self._business_params = value
    @property
    def denomination(self):
        return self._denomination

    @denomination.setter
    def denomination(self, value):
        self._denomination = value
    @property
    def effective_end_date(self):
        return self._effective_end_date

    @effective_end_date.setter
    def effective_end_date(self, value):
        self._effective_end_date = value
    @property
    def effective_period(self):
        return self._effective_period

    @effective_period.setter
    def effective_period(self, value):
        self._effective_period = value
    @property
    def effective_start_date(self):
        return self._effective_start_date

    @effective_start_date.setter
    def effective_start_date(self, value):
        self._effective_start_date = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def gift_card_template_name(self):
        return self._gift_card_template_name

    @gift_card_template_name.setter
    def gift_card_template_name(self, value):
        self._gift_card_template_name = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def settle_account_no(self):
        return self._settle_account_no

    @settle_account_no.setter
    def settle_account_no(self, value):
        self._settle_account_no = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def valid_date(self):
        return self._valid_date

    @valid_date.setter
    def valid_date(self, value):
        self._valid_date = value
    @property
    def valid_period(self):
        return self._valid_period

    @valid_period.setter
    def valid_period(self, value):
        self._valid_period = value
    @property
    def valid_type(self):
        return self._valid_type

    @valid_type.setter
    def valid_type(self, value):
        self._valid_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.denomination:
            if hasattr(self.denomination, 'to_alipay_dict'):
                params['denomination'] = self.denomination.to_alipay_dict()
            else:
                params['denomination'] = self.denomination
        if self.effective_end_date:
            if hasattr(self.effective_end_date, 'to_alipay_dict'):
                params['effective_end_date'] = self.effective_end_date.to_alipay_dict()
            else:
                params['effective_end_date'] = self.effective_end_date
        if self.effective_period:
            if hasattr(self.effective_period, 'to_alipay_dict'):
                params['effective_period'] = self.effective_period.to_alipay_dict()
            else:
                params['effective_period'] = self.effective_period
        if self.effective_start_date:
            if hasattr(self.effective_start_date, 'to_alipay_dict'):
                params['effective_start_date'] = self.effective_start_date.to_alipay_dict()
            else:
                params['effective_start_date'] = self.effective_start_date
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.gift_card_template_name:
            if hasattr(self.gift_card_template_name, 'to_alipay_dict'):
                params['gift_card_template_name'] = self.gift_card_template_name.to_alipay_dict()
            else:
                params['gift_card_template_name'] = self.gift_card_template_name
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.settle_account_no:
            if hasattr(self.settle_account_no, 'to_alipay_dict'):
                params['settle_account_no'] = self.settle_account_no.to_alipay_dict()
            else:
                params['settle_account_no'] = self.settle_account_no
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        if self.valid_date:
            if hasattr(self.valid_date, 'to_alipay_dict'):
                params['valid_date'] = self.valid_date.to_alipay_dict()
            else:
                params['valid_date'] = self.valid_date
        if self.valid_period:
            if hasattr(self.valid_period, 'to_alipay_dict'):
                params['valid_period'] = self.valid_period.to_alipay_dict()
            else:
                params['valid_period'] = self.valid_period
        if self.valid_type:
            if hasattr(self.valid_type, 'to_alipay_dict'):
                params['valid_type'] = self.valid_type.to_alipay_dict()
            else:
                params['valid_type'] = self.valid_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftCardTemplate()
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'denomination' in d:
            o.denomination = d['denomination']
        if 'effective_end_date' in d:
            o.effective_end_date = d['effective_end_date']
        if 'effective_period' in d:
            o.effective_period = d['effective_period']
        if 'effective_start_date' in d:
            o.effective_start_date = d['effective_start_date']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'gift_card_template_name' in d:
            o.gift_card_template_name = d['gift_card_template_name']
        if 'price' in d:
            o.price = d['price']
        if 'settle_account_no' in d:
            o.settle_account_no = d['settle_account_no']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        if 'valid_date' in d:
            o.valid_date = d['valid_date']
        if 'valid_period' in d:
            o.valid_period = d['valid_period']
        if 'valid_type' in d:
            o.valid_type = d['valid_type']
        return o


