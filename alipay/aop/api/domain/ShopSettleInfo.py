#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopBankCard import ShopBankCard


class ShopSettleInfo(object):

    def __init__(self):
        self._account = None
        self._bank_cards = None
        self._type = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def bank_cards(self):
        return self._bank_cards

    @bank_cards.setter
    def bank_cards(self, value):
        if isinstance(value, ShopBankCard):
            self._bank_cards = value
        else:
            self._bank_cards = ShopBankCard.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.bank_cards:
            if hasattr(self.bank_cards, 'to_alipay_dict'):
                params['bank_cards'] = self.bank_cards.to_alipay_dict()
            else:
                params['bank_cards'] = self.bank_cards
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopSettleInfo()
        if 'account' in d:
            o.account = d['account']
        if 'bank_cards' in d:
            o.bank_cards = d['bank_cards']
        if 'type' in d:
            o.type = d['type']
        return o


