#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPayafterusePeriodCloseModel(object):

    def __init__(self):
        self._auth_id = None
        self._out_period_no = None

    @property
    def auth_id(self):
        return self._auth_id

    @auth_id.setter
    def auth_id(self, value):
        self._auth_id = value
    @property
    def out_period_no(self):
        return self._out_period_no

    @out_period_no.setter
    def out_period_no(self, value):
        self._out_period_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_id:
            if hasattr(self.auth_id, 'to_alipay_dict'):
                params['auth_id'] = self.auth_id.to_alipay_dict()
            else:
                params['auth_id'] = self.auth_id
        if self.out_period_no:
            if hasattr(self.out_period_no, 'to_alipay_dict'):
                params['out_period_no'] = self.out_period_no.to_alipay_dict()
            else:
                params['out_period_no'] = self.out_period_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPayafterusePeriodCloseModel()
        if 'auth_id' in d:
            o.auth_id = d['auth_id']
        if 'out_period_no' in d:
            o.out_period_no = d['out_period_no']
        return o


