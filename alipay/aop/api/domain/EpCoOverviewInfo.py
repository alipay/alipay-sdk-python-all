#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndustryCountInfo import IndustryCountInfo
from alipay.aop.api.domain.CityCountInfo import CityCountInfo


class EpCoOverviewInfo(object):

    def __init__(self):
        self._crn = None
        self._industry = None
        self._inv_amount = None
        self._inv_num = None
        self._member_num = None
        self._member_registered_capital = None
        self._name = None
        self._province = None
        self._root = None

    @property
    def crn(self):
        return self._crn

    @crn.setter
    def crn(self, value):
        self._crn = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        if isinstance(value, IndustryCountInfo):
            self._industry = value
        else:
            self._industry = IndustryCountInfo.from_alipay_dict(value)
    @property
    def inv_amount(self):
        return self._inv_amount

    @inv_amount.setter
    def inv_amount(self, value):
        self._inv_amount = value
    @property
    def inv_num(self):
        return self._inv_num

    @inv_num.setter
    def inv_num(self, value):
        self._inv_num = value
    @property
    def member_num(self):
        return self._member_num

    @member_num.setter
    def member_num(self, value):
        self._member_num = value
    @property
    def member_registered_capital(self):
        return self._member_registered_capital

    @member_registered_capital.setter
    def member_registered_capital(self, value):
        self._member_registered_capital = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        if isinstance(value, CityCountInfo):
            self._province = value
        else:
            self._province = CityCountInfo.from_alipay_dict(value)
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value


    def to_alipay_dict(self):
        params = dict()
        if self.crn:
            if hasattr(self.crn, 'to_alipay_dict'):
                params['crn'] = self.crn.to_alipay_dict()
            else:
                params['crn'] = self.crn
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.inv_amount:
            if hasattr(self.inv_amount, 'to_alipay_dict'):
                params['inv_amount'] = self.inv_amount.to_alipay_dict()
            else:
                params['inv_amount'] = self.inv_amount
        if self.inv_num:
            if hasattr(self.inv_num, 'to_alipay_dict'):
                params['inv_num'] = self.inv_num.to_alipay_dict()
            else:
                params['inv_num'] = self.inv_num
        if self.member_num:
            if hasattr(self.member_num, 'to_alipay_dict'):
                params['member_num'] = self.member_num.to_alipay_dict()
            else:
                params['member_num'] = self.member_num
        if self.member_registered_capital:
            if hasattr(self.member_registered_capital, 'to_alipay_dict'):
                params['member_registered_capital'] = self.member_registered_capital.to_alipay_dict()
            else:
                params['member_registered_capital'] = self.member_registered_capital
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.root:
            if hasattr(self.root, 'to_alipay_dict'):
                params['root'] = self.root.to_alipay_dict()
            else:
                params['root'] = self.root
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpCoOverviewInfo()
        if 'crn' in d:
            o.crn = d['crn']
        if 'industry' in d:
            o.industry = d['industry']
        if 'inv_amount' in d:
            o.inv_amount = d['inv_amount']
        if 'inv_num' in d:
            o.inv_num = d['inv_num']
        if 'member_num' in d:
            o.member_num = d['member_num']
        if 'member_registered_capital' in d:
            o.member_registered_capital = d['member_registered_capital']
        if 'name' in d:
            o.name = d['name']
        if 'province' in d:
            o.province = d['province']
        if 'root' in d:
            o.root = d['root']
        return o


