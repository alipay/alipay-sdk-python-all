#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpAdminPenaltyPunishDetailsInfo(object):

    def __init__(self):
        self._category = None
        self._date = None
        self._money = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.money:
            if hasattr(self.money, 'to_alipay_dict'):
                params['money'] = self.money.to_alipay_dict()
            else:
                params['money'] = self.money
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpAdminPenaltyPunishDetailsInfo()
        if 'category' in d:
            o.category = d['category']
        if 'date' in d:
            o.date = d['date']
        if 'money' in d:
            o.money = d['money']
        return o


