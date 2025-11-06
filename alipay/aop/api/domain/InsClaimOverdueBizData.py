#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsClaimOverdueBizData(object):

    def __init__(self):
        self._buyer_phone = None
        self._game_account_phone = None
        self._overdue_bill_title = None
        self._seller_phone = None

    @property
    def buyer_phone(self):
        return self._buyer_phone

    @buyer_phone.setter
    def buyer_phone(self, value):
        self._buyer_phone = value
    @property
    def game_account_phone(self):
        return self._game_account_phone

    @game_account_phone.setter
    def game_account_phone(self, value):
        self._game_account_phone = value
    @property
    def overdue_bill_title(self):
        return self._overdue_bill_title

    @overdue_bill_title.setter
    def overdue_bill_title(self, value):
        self._overdue_bill_title = value
    @property
    def seller_phone(self):
        return self._seller_phone

    @seller_phone.setter
    def seller_phone(self, value):
        self._seller_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_phone:
            if hasattr(self.buyer_phone, 'to_alipay_dict'):
                params['buyer_phone'] = self.buyer_phone.to_alipay_dict()
            else:
                params['buyer_phone'] = self.buyer_phone
        if self.game_account_phone:
            if hasattr(self.game_account_phone, 'to_alipay_dict'):
                params['game_account_phone'] = self.game_account_phone.to_alipay_dict()
            else:
                params['game_account_phone'] = self.game_account_phone
        if self.overdue_bill_title:
            if hasattr(self.overdue_bill_title, 'to_alipay_dict'):
                params['overdue_bill_title'] = self.overdue_bill_title.to_alipay_dict()
            else:
                params['overdue_bill_title'] = self.overdue_bill_title
        if self.seller_phone:
            if hasattr(self.seller_phone, 'to_alipay_dict'):
                params['seller_phone'] = self.seller_phone.to_alipay_dict()
            else:
                params['seller_phone'] = self.seller_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsClaimOverdueBizData()
        if 'buyer_phone' in d:
            o.buyer_phone = d['buyer_phone']
        if 'game_account_phone' in d:
            o.game_account_phone = d['game_account_phone']
        if 'overdue_bill_title' in d:
            o.overdue_bill_title = d['overdue_bill_title']
        if 'seller_phone' in d:
            o.seller_phone = d['seller_phone']
        return o


