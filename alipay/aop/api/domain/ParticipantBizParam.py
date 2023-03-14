#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParticipantBizParam(object):

    def __init__(self):
        self._fund_ratio = None
        self._fund_type = None

    @property
    def fund_ratio(self):
        return self._fund_ratio

    @fund_ratio.setter
    def fund_ratio(self, value):
        self._fund_ratio = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_ratio:
            if hasattr(self.fund_ratio, 'to_alipay_dict'):
                params['fund_ratio'] = self.fund_ratio.to_alipay_dict()
            else:
                params['fund_ratio'] = self.fund_ratio
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
        o = ParticipantBizParam()
        if 'fund_ratio' in d:
            o.fund_ratio = d['fund_ratio']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        return o


