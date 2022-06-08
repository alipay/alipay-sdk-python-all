#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundExtInfo(object):

    def __init__(self):
        self._fund_identity = None
        self._fund_identity_type = None

    @property
    def fund_identity(self):
        return self._fund_identity

    @fund_identity.setter
    def fund_identity(self, value):
        self._fund_identity = value
    @property
    def fund_identity_type(self):
        return self._fund_identity_type

    @fund_identity_type.setter
    def fund_identity_type(self, value):
        self._fund_identity_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_identity:
            if hasattr(self.fund_identity, 'to_alipay_dict'):
                params['fund_identity'] = self.fund_identity.to_alipay_dict()
            else:
                params['fund_identity'] = self.fund_identity
        if self.fund_identity_type:
            if hasattr(self.fund_identity_type, 'to_alipay_dict'):
                params['fund_identity_type'] = self.fund_identity_type.to_alipay_dict()
            else:
                params['fund_identity_type'] = self.fund_identity_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundExtInfo()
        if 'fund_identity' in d:
            o.fund_identity = d['fund_identity']
        if 'fund_identity_type' in d:
            o.fund_identity_type = d['fund_identity_type']
        return o


