#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member


class MybankCreditCreditriskGuarschemeQueryModel(object):

    def __init__(self):
        self._bsn_type = None
        self._sale_pd_code = None
        self._user = None

    @property
    def bsn_type(self):
        return self._bsn_type

    @bsn_type.setter
    def bsn_type(self, value):
        self._bsn_type = value
    @property
    def sale_pd_code(self):
        return self._sale_pd_code

    @sale_pd_code.setter
    def sale_pd_code(self, value):
        self._sale_pd_code = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, Member):
            self._user = value
        else:
            self._user = Member.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bsn_type:
            if hasattr(self.bsn_type, 'to_alipay_dict'):
                params['bsn_type'] = self.bsn_type.to_alipay_dict()
            else:
                params['bsn_type'] = self.bsn_type
        if self.sale_pd_code:
            if hasattr(self.sale_pd_code, 'to_alipay_dict'):
                params['sale_pd_code'] = self.sale_pd_code.to_alipay_dict()
            else:
                params['sale_pd_code'] = self.sale_pd_code
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditCreditriskGuarschemeQueryModel()
        if 'bsn_type' in d:
            o.bsn_type = d['bsn_type']
        if 'sale_pd_code' in d:
            o.sale_pd_code = d['sale_pd_code']
        if 'user' in d:
            o.user = d['user']
        return o


