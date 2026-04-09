#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopBankCard import ShopBankCard


class ShopSettleInfo(object):

    def __init__(self):
        self._account = None
        self._account_type = None
        self._bank_cards = None
        self._payee_account_no = None
        self._payee_identity_back_pic = None
        self._payee_identity_front_pic = None
        self._shop_front_pic = None
        self._type = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
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
    def payee_account_no(self):
        return self._payee_account_no

    @payee_account_no.setter
    def payee_account_no(self, value):
        self._payee_account_no = value
    @property
    def payee_identity_back_pic(self):
        return self._payee_identity_back_pic

    @payee_identity_back_pic.setter
    def payee_identity_back_pic(self, value):
        self._payee_identity_back_pic = value
    @property
    def payee_identity_front_pic(self):
        return self._payee_identity_front_pic

    @payee_identity_front_pic.setter
    def payee_identity_front_pic(self, value):
        self._payee_identity_front_pic = value
    @property
    def shop_front_pic(self):
        return self._shop_front_pic

    @shop_front_pic.setter
    def shop_front_pic(self, value):
        self._shop_front_pic = value
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
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.bank_cards:
            if hasattr(self.bank_cards, 'to_alipay_dict'):
                params['bank_cards'] = self.bank_cards.to_alipay_dict()
            else:
                params['bank_cards'] = self.bank_cards
        if self.payee_account_no:
            if hasattr(self.payee_account_no, 'to_alipay_dict'):
                params['payee_account_no'] = self.payee_account_no.to_alipay_dict()
            else:
                params['payee_account_no'] = self.payee_account_no
        if self.payee_identity_back_pic:
            if hasattr(self.payee_identity_back_pic, 'to_alipay_dict'):
                params['payee_identity_back_pic'] = self.payee_identity_back_pic.to_alipay_dict()
            else:
                params['payee_identity_back_pic'] = self.payee_identity_back_pic
        if self.payee_identity_front_pic:
            if hasattr(self.payee_identity_front_pic, 'to_alipay_dict'):
                params['payee_identity_front_pic'] = self.payee_identity_front_pic.to_alipay_dict()
            else:
                params['payee_identity_front_pic'] = self.payee_identity_front_pic
        if self.shop_front_pic:
            if hasattr(self.shop_front_pic, 'to_alipay_dict'):
                params['shop_front_pic'] = self.shop_front_pic.to_alipay_dict()
            else:
                params['shop_front_pic'] = self.shop_front_pic
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
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'bank_cards' in d:
            o.bank_cards = d['bank_cards']
        if 'payee_account_no' in d:
            o.payee_account_no = d['payee_account_no']
        if 'payee_identity_back_pic' in d:
            o.payee_identity_back_pic = d['payee_identity_back_pic']
        if 'payee_identity_front_pic' in d:
            o.payee_identity_front_pic = d['payee_identity_front_pic']
        if 'shop_front_pic' in d:
            o.shop_front_pic = d['shop_front_pic']
        if 'type' in d:
            o.type = d['type']
        return o


