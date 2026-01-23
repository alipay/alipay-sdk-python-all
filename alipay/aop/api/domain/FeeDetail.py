#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoboExtendInfo import RoboExtendInfo


class FeeDetail(object):

    def __init__(self):
        self._amount = None
        self._desc = None
        self._extend_info = None
        self._type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        if isinstance(value, list):
            self._extend_info = list()
            for i in value:
                if isinstance(i, RoboExtendInfo):
                    self._extend_info.append(i)
                else:
                    self._extend_info.append(RoboExtendInfo.from_alipay_dict(i))
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.extend_info:
            if isinstance(self.extend_info, list):
                for i in range(0, len(self.extend_info)):
                    element = self.extend_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extend_info[i] = element.to_alipay_dict()
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FeeDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'desc' in d:
            o.desc = d['desc']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'type' in d:
            o.type = d['type']
        return o


