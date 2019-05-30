#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserInfoFromNJ(object):

    def __init__(self):
        self._company = None
        self._tel = None

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value
    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, value):
        self._tel = value


    def to_alipay_dict(self):
        params = dict()
        if self.company:
            if hasattr(self.company, 'to_alipay_dict'):
                params['company'] = self.company.to_alipay_dict()
            else:
                params['company'] = self.company
        if self.tel:
            if hasattr(self.tel, 'to_alipay_dict'):
                params['tel'] = self.tel.to_alipay_dict()
            else:
                params['tel'] = self.tel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserInfoFromNJ()
        if 'company' in d:
            o.company = d['company']
        if 'tel' in d:
            o.tel = d['tel']
        return o


