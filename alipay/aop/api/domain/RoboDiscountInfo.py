#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoboExtendInfo import RoboExtendInfo


class RoboDiscountInfo(object):

    def __init__(self):
        self._amount = None
        self._description = None
        self._extend_info = None
        self._key = None
        self._type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
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
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
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
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
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
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
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
        o = RoboDiscountInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'description' in d:
            o.description = d['description']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'key' in d:
            o.key = d['key']
        if 'type' in d:
            o.type = d['type']
        return o


