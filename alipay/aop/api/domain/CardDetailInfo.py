#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardDetailInfo(object):

    def __init__(self):
        self._balance = None
        self._card_bg_image = None
        self._card_logo = None
        self._card_name = None
        self._card_no = None
        self._origin_amount = None
        self._valid_end_date = None
        self._valid_start_date = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def card_bg_image(self):
        return self._card_bg_image

    @card_bg_image.setter
    def card_bg_image(self, value):
        self._card_bg_image = value
    @property
    def card_logo(self):
        return self._card_logo

    @card_logo.setter
    def card_logo(self, value):
        self._card_logo = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def origin_amount(self):
        return self._origin_amount

    @origin_amount.setter
    def origin_amount(self, value):
        self._origin_amount = value
    @property
    def valid_end_date(self):
        return self._valid_end_date

    @valid_end_date.setter
    def valid_end_date(self, value):
        self._valid_end_date = value
    @property
    def valid_start_date(self):
        return self._valid_start_date

    @valid_start_date.setter
    def valid_start_date(self, value):
        self._valid_start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.card_bg_image:
            if hasattr(self.card_bg_image, 'to_alipay_dict'):
                params['card_bg_image'] = self.card_bg_image.to_alipay_dict()
            else:
                params['card_bg_image'] = self.card_bg_image
        if self.card_logo:
            if hasattr(self.card_logo, 'to_alipay_dict'):
                params['card_logo'] = self.card_logo.to_alipay_dict()
            else:
                params['card_logo'] = self.card_logo
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.origin_amount:
            if hasattr(self.origin_amount, 'to_alipay_dict'):
                params['origin_amount'] = self.origin_amount.to_alipay_dict()
            else:
                params['origin_amount'] = self.origin_amount
        if self.valid_end_date:
            if hasattr(self.valid_end_date, 'to_alipay_dict'):
                params['valid_end_date'] = self.valid_end_date.to_alipay_dict()
            else:
                params['valid_end_date'] = self.valid_end_date
        if self.valid_start_date:
            if hasattr(self.valid_start_date, 'to_alipay_dict'):
                params['valid_start_date'] = self.valid_start_date.to_alipay_dict()
            else:
                params['valid_start_date'] = self.valid_start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardDetailInfo()
        if 'balance' in d:
            o.balance = d['balance']
        if 'card_bg_image' in d:
            o.card_bg_image = d['card_bg_image']
        if 'card_logo' in d:
            o.card_logo = d['card_logo']
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'origin_amount' in d:
            o.origin_amount = d['origin_amount']
        if 'valid_end_date' in d:
            o.valid_end_date = d['valid_end_date']
        if 'valid_start_date' in d:
            o.valid_start_date = d['valid_start_date']
        return o


