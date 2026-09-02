#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupPurchaseBankCard import GroupPurchaseBankCard


class GroupPurchaseShopSettleInfo(object):

    def __init__(self):
        self._account = None
        self._bank_card = None
        self._type = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def bank_card(self):
        return self._bank_card

    @bank_card.setter
    def bank_card(self, value):
        if isinstance(value, GroupPurchaseBankCard):
            self._bank_card = value
        else:
            self._bank_card = GroupPurchaseBankCard.from_alipay_dict(value)
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
        if self.bank_card:
            if hasattr(self.bank_card, 'to_alipay_dict'):
                params['bank_card'] = self.bank_card.to_alipay_dict()
            else:
                params['bank_card'] = self.bank_card
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
        o = GroupPurchaseShopSettleInfo()
        if 'account' in d:
            o.account = d['account']
        if 'bank_card' in d:
            o.bank_card = d['bank_card']
        if 'type' in d:
            o.type = d['type']
        return o


