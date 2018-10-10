#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MallCardUpdate(object):

    def __init__(self):
        self._balance = None
        self._biz_card_no = None
        self._external_card_no = None
        self._level = None
        self._point = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def biz_card_no(self):
        return self._biz_card_no

    @biz_card_no.setter
    def biz_card_no(self, value):
        self._biz_card_no = value
    @property
    def external_card_no(self):
        return self._external_card_no

    @external_card_no.setter
    def external_card_no(self, value):
        self._external_card_no = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value


    def to_alipay_dict(self):
        params = dict()
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.biz_card_no:
            if hasattr(self.biz_card_no, 'to_alipay_dict'):
                params['biz_card_no'] = self.biz_card_no.to_alipay_dict()
            else:
                params['biz_card_no'] = self.biz_card_no
        if self.external_card_no:
            if hasattr(self.external_card_no, 'to_alipay_dict'):
                params['external_card_no'] = self.external_card_no.to_alipay_dict()
            else:
                params['external_card_no'] = self.external_card_no
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.point:
            if hasattr(self.point, 'to_alipay_dict'):
                params['point'] = self.point.to_alipay_dict()
            else:
                params['point'] = self.point
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MallCardUpdate()
        if 'balance' in d:
            o.balance = d['balance']
        if 'biz_card_no' in d:
            o.biz_card_no = d['biz_card_no']
        if 'external_card_no' in d:
            o.external_card_no = d['external_card_no']
        if 'level' in d:
            o.level = d['level']
        if 'point' in d:
            o.point = d['point']
        return o


