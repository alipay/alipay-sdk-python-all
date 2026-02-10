#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpCoMemberInfo(object):

    def __init__(self):
        self._build_date = None
        self._crn = None
        self._industry = None
        self._legal_representative = None
        self._name = None
        self._province = None
        self._register_capital = None
        self._register_capital_text = None

    @property
    def build_date(self):
        return self._build_date

    @build_date.setter
    def build_date(self, value):
        self._build_date = value
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
        self._industry = value
    @property
    def legal_representative(self):
        return self._legal_representative

    @legal_representative.setter
    def legal_representative(self, value):
        self._legal_representative = value
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
    def register_capital(self):
        return self._register_capital

    @register_capital.setter
    def register_capital(self, value):
        self._register_capital = value
    @property
    def register_capital_text(self):
        return self._register_capital_text

    @register_capital_text.setter
    def register_capital_text(self, value):
        self._register_capital_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.build_date:
            if hasattr(self.build_date, 'to_alipay_dict'):
                params['build_date'] = self.build_date.to_alipay_dict()
            else:
                params['build_date'] = self.build_date
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
        if self.legal_representative:
            if hasattr(self.legal_representative, 'to_alipay_dict'):
                params['legal_representative'] = self.legal_representative.to_alipay_dict()
            else:
                params['legal_representative'] = self.legal_representative
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
        if self.register_capital:
            if hasattr(self.register_capital, 'to_alipay_dict'):
                params['register_capital'] = self.register_capital.to_alipay_dict()
            else:
                params['register_capital'] = self.register_capital
        if self.register_capital_text:
            if hasattr(self.register_capital_text, 'to_alipay_dict'):
                params['register_capital_text'] = self.register_capital_text.to_alipay_dict()
            else:
                params['register_capital_text'] = self.register_capital_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpCoMemberInfo()
        if 'build_date' in d:
            o.build_date = d['build_date']
        if 'crn' in d:
            o.crn = d['crn']
        if 'industry' in d:
            o.industry = d['industry']
        if 'legal_representative' in d:
            o.legal_representative = d['legal_representative']
        if 'name' in d:
            o.name = d['name']
        if 'province' in d:
            o.province = d['province']
        if 'register_capital' in d:
            o.register_capital = d['register_capital']
        if 'register_capital_text' in d:
            o.register_capital_text = d['register_capital_text']
        return o


