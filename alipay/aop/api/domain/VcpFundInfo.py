#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VcpFundInfo(object):

    def __init__(self):
        self._display_account = None
        self._fund_account = None
        self._fund_type = None

    @property
    def display_account(self):
        return self._display_account

    @display_account.setter
    def display_account(self, value):
        self._display_account = value
    @property
    def fund_account(self):
        return self._fund_account

    @fund_account.setter
    def fund_account(self, value):
        self._fund_account = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.display_account:
            if hasattr(self.display_account, 'to_alipay_dict'):
                params['display_account'] = self.display_account.to_alipay_dict()
            else:
                params['display_account'] = self.display_account
        if self.fund_account:
            if hasattr(self.fund_account, 'to_alipay_dict'):
                params['fund_account'] = self.fund_account.to_alipay_dict()
            else:
                params['fund_account'] = self.fund_account
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VcpFundInfo()
        if 'display_account' in d:
            o.display_account = d['display_account']
        if 'fund_account' in d:
            o.fund_account = d['fund_account']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        return o


