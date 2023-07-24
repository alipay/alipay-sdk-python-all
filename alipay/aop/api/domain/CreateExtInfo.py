#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditRateNoAuth import CreditRateNoAuth
from alipay.aop.api.domain.CreditRatePartialAuth import CreditRatePartialAuth
from alipay.aop.api.domain.Dowsure import Dowsure


class CreateExtInfo(object):

    def __init__(self):
        self._cr_no_auth = None
        self._cr_partial_auth = None
        self._dowsure = None

    @property
    def cr_no_auth(self):
        return self._cr_no_auth

    @cr_no_auth.setter
    def cr_no_auth(self, value):
        if isinstance(value, CreditRateNoAuth):
            self._cr_no_auth = value
        else:
            self._cr_no_auth = CreditRateNoAuth.from_alipay_dict(value)
    @property
    def cr_partial_auth(self):
        return self._cr_partial_auth

    @cr_partial_auth.setter
    def cr_partial_auth(self, value):
        if isinstance(value, CreditRatePartialAuth):
            self._cr_partial_auth = value
        else:
            self._cr_partial_auth = CreditRatePartialAuth.from_alipay_dict(value)
    @property
    def dowsure(self):
        return self._dowsure

    @dowsure.setter
    def dowsure(self, value):
        if isinstance(value, Dowsure):
            self._dowsure = value
        else:
            self._dowsure = Dowsure.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.cr_no_auth:
            if hasattr(self.cr_no_auth, 'to_alipay_dict'):
                params['cr_no_auth'] = self.cr_no_auth.to_alipay_dict()
            else:
                params['cr_no_auth'] = self.cr_no_auth
        if self.cr_partial_auth:
            if hasattr(self.cr_partial_auth, 'to_alipay_dict'):
                params['cr_partial_auth'] = self.cr_partial_auth.to_alipay_dict()
            else:
                params['cr_partial_auth'] = self.cr_partial_auth
        if self.dowsure:
            if hasattr(self.dowsure, 'to_alipay_dict'):
                params['dowsure'] = self.dowsure.to_alipay_dict()
            else:
                params['dowsure'] = self.dowsure
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreateExtInfo()
        if 'cr_no_auth' in d:
            o.cr_no_auth = d['cr_no_auth']
        if 'cr_partial_auth' in d:
            o.cr_partial_auth = d['cr_partial_auth']
        if 'dowsure' in d:
            o.dowsure = d['dowsure']
        return o


