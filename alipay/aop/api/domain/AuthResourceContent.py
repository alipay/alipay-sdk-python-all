#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthResourceContent(object):

    def __init__(self):
        self._award_amount = None
        self._group_type = None

    @property
    def award_amount(self):
        return self._award_amount

    @award_amount.setter
    def award_amount(self, value):
        self._award_amount = value
    @property
    def group_type(self):
        return self._group_type

    @group_type.setter
    def group_type(self, value):
        self._group_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.award_amount:
            if hasattr(self.award_amount, 'to_alipay_dict'):
                params['award_amount'] = self.award_amount.to_alipay_dict()
            else:
                params['award_amount'] = self.award_amount
        if self.group_type:
            if hasattr(self.group_type, 'to_alipay_dict'):
                params['group_type'] = self.group_type.to_alipay_dict()
            else:
                params['group_type'] = self.group_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthResourceContent()
        if 'award_amount' in d:
            o.award_amount = d['award_amount']
        if 'group_type' in d:
            o.group_type = d['group_type']
        return o


