#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockOpenPromoConsultModel(object):

    def __init__(self):
        self._amount = None
        self._check_available_camp = None
        self._fix_price_send = None
        self._front_ctl_rec_context = None
        self._interest_id = None
        self._open_id = None
        self._prize_id = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def check_available_camp(self):
        return self._check_available_camp

    @check_available_camp.setter
    def check_available_camp(self, value):
        self._check_available_camp = value
    @property
    def fix_price_send(self):
        return self._fix_price_send

    @fix_price_send.setter
    def fix_price_send(self, value):
        self._fix_price_send = value
    @property
    def front_ctl_rec_context(self):
        return self._front_ctl_rec_context

    @front_ctl_rec_context.setter
    def front_ctl_rec_context(self, value):
        self._front_ctl_rec_context = value
    @property
    def interest_id(self):
        return self._interest_id

    @interest_id.setter
    def interest_id(self, value):
        self._interest_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.check_available_camp:
            if hasattr(self.check_available_camp, 'to_alipay_dict'):
                params['check_available_camp'] = self.check_available_camp.to_alipay_dict()
            else:
                params['check_available_camp'] = self.check_available_camp
        if self.fix_price_send:
            if hasattr(self.fix_price_send, 'to_alipay_dict'):
                params['fix_price_send'] = self.fix_price_send.to_alipay_dict()
            else:
                params['fix_price_send'] = self.fix_price_send
        if self.front_ctl_rec_context:
            if hasattr(self.front_ctl_rec_context, 'to_alipay_dict'):
                params['front_ctl_rec_context'] = self.front_ctl_rec_context.to_alipay_dict()
            else:
                params['front_ctl_rec_context'] = self.front_ctl_rec_context
        if self.interest_id:
            if hasattr(self.interest_id, 'to_alipay_dict'):
                params['interest_id'] = self.interest_id.to_alipay_dict()
            else:
                params['interest_id'] = self.interest_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockOpenPromoConsultModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'check_available_camp' in d:
            o.check_available_camp = d['check_available_camp']
        if 'fix_price_send' in d:
            o.fix_price_send = d['fix_price_send']
        if 'front_ctl_rec_context' in d:
            o.front_ctl_rec_context = d['front_ctl_rec_context']
        if 'interest_id' in d:
            o.interest_id = d['interest_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


