#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParkingMembershipInfo(object):

    def __init__(self):
        self._membership_balance = None
        self._membership_type = None

    @property
    def membership_balance(self):
        return self._membership_balance

    @membership_balance.setter
    def membership_balance(self, value):
        self._membership_balance = value
    @property
    def membership_type(self):
        return self._membership_type

    @membership_type.setter
    def membership_type(self, value):
        self._membership_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.membership_balance:
            if hasattr(self.membership_balance, 'to_alipay_dict'):
                params['membership_balance'] = self.membership_balance.to_alipay_dict()
            else:
                params['membership_balance'] = self.membership_balance
        if self.membership_type:
            if hasattr(self.membership_type, 'to_alipay_dict'):
                params['membership_type'] = self.membership_type.to_alipay_dict()
            else:
                params['membership_type'] = self.membership_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParkingMembershipInfo()
        if 'membership_balance' in d:
            o.membership_balance = d['membership_balance']
        if 'membership_type' in d:
            o.membership_type = d['membership_type']
        return o


