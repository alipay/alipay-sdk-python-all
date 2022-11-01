#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankActivityInfo(object):

    def __init__(self):
        self._bind_card = None
        self._card_name = None
        self._discount_desc = None
        self._logo = None

    @property
    def bind_card(self):
        return self._bind_card

    @bind_card.setter
    def bind_card(self, value):
        self._bind_card = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def discount_desc(self):
        return self._discount_desc

    @discount_desc.setter
    def discount_desc(self, value):
        self._discount_desc = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_card:
            if hasattr(self.bind_card, 'to_alipay_dict'):
                params['bind_card'] = self.bind_card.to_alipay_dict()
            else:
                params['bind_card'] = self.bind_card
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.discount_desc:
            if hasattr(self.discount_desc, 'to_alipay_dict'):
                params['discount_desc'] = self.discount_desc.to_alipay_dict()
            else:
                params['discount_desc'] = self.discount_desc
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankActivityInfo()
        if 'bind_card' in d:
            o.bind_card = d['bind_card']
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'discount_desc' in d:
            o.discount_desc = d['discount_desc']
        if 'logo' in d:
            o.logo = d['logo']
        return o


