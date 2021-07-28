#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfarmUserDonationRecord(object):

    def __init__(self):
        self._charity_time = None
        self._donation_amount = None

    @property
    def charity_time(self):
        return self._charity_time

    @charity_time.setter
    def charity_time(self, value):
        self._charity_time = value
    @property
    def donation_amount(self):
        return self._donation_amount

    @donation_amount.setter
    def donation_amount(self, value):
        self._donation_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.charity_time:
            if hasattr(self.charity_time, 'to_alipay_dict'):
                params['charity_time'] = self.charity_time.to_alipay_dict()
            else:
                params['charity_time'] = self.charity_time
        if self.donation_amount:
            if hasattr(self.donation_amount, 'to_alipay_dict'):
                params['donation_amount'] = self.donation_amount.to_alipay_dict()
            else:
                params['donation_amount'] = self.donation_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfarmUserDonationRecord()
        if 'charity_time' in d:
            o.charity_time = d['charity_time']
        if 'donation_amount' in d:
            o.donation_amount = d['donation_amount']
        return o


