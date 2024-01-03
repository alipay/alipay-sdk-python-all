#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PunishedInfo(object):

    def __init__(self):
        self._card_num = None
        self._case_code = None
        self._case_status = None
        self._court_name = None
        self._exec_money = None
        self._name = None
        self._province = None
        self._reg_case_date = None
        self._type = None

    @property
    def card_num(self):
        return self._card_num

    @card_num.setter
    def card_num(self, value):
        self._card_num = value
    @property
    def case_code(self):
        return self._case_code

    @case_code.setter
    def case_code(self, value):
        self._case_code = value
    @property
    def case_status(self):
        return self._case_status

    @case_status.setter
    def case_status(self, value):
        self._case_status = value
    @property
    def court_name(self):
        return self._court_name

    @court_name.setter
    def court_name(self, value):
        self._court_name = value
    @property
    def exec_money(self):
        return self._exec_money

    @exec_money.setter
    def exec_money(self, value):
        self._exec_money = value
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
        self._province = value
    @property
    def reg_case_date(self):
        return self._reg_case_date

    @reg_case_date.setter
    def reg_case_date(self, value):
        self._reg_case_date = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_num:
            if hasattr(self.card_num, 'to_alipay_dict'):
                params['card_num'] = self.card_num.to_alipay_dict()
            else:
                params['card_num'] = self.card_num
        if self.case_code:
            if hasattr(self.case_code, 'to_alipay_dict'):
                params['case_code'] = self.case_code.to_alipay_dict()
            else:
                params['case_code'] = self.case_code
        if self.case_status:
            if hasattr(self.case_status, 'to_alipay_dict'):
                params['case_status'] = self.case_status.to_alipay_dict()
            else:
                params['case_status'] = self.case_status
        if self.court_name:
            if hasattr(self.court_name, 'to_alipay_dict'):
                params['court_name'] = self.court_name.to_alipay_dict()
            else:
                params['court_name'] = self.court_name
        if self.exec_money:
            if hasattr(self.exec_money, 'to_alipay_dict'):
                params['exec_money'] = self.exec_money.to_alipay_dict()
            else:
                params['exec_money'] = self.exec_money
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
        if self.reg_case_date:
            if hasattr(self.reg_case_date, 'to_alipay_dict'):
                params['reg_case_date'] = self.reg_case_date.to_alipay_dict()
            else:
                params['reg_case_date'] = self.reg_case_date
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
        o = PunishedInfo()
        if 'card_num' in d:
            o.card_num = d['card_num']
        if 'case_code' in d:
            o.case_code = d['case_code']
        if 'case_status' in d:
            o.case_status = d['case_status']
        if 'court_name' in d:
            o.court_name = d['court_name']
        if 'exec_money' in d:
            o.exec_money = d['exec_money']
        if 'name' in d:
            o.name = d['name']
        if 'province' in d:
            o.province = d['province']
        if 'reg_case_date' in d:
            o.reg_case_date = d['reg_case_date']
        if 'type' in d:
            o.type = d['type']
        return o


