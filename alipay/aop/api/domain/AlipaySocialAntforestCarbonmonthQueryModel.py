#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialAntforestCarbonmonthQueryModel(object):

    def __init__(self):
        self._carbon_type = None
        self._month = None
        self._user_id = None

    @property
    def carbon_type(self):
        return self._carbon_type

    @carbon_type.setter
    def carbon_type(self, value):
        if isinstance(value, list):
            self._carbon_type = list()
            for i in value:
                self._carbon_type.append(i)
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.carbon_type:
            if isinstance(self.carbon_type, list):
                for i in range(0, len(self.carbon_type)):
                    element = self.carbon_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.carbon_type[i] = element.to_alipay_dict()
            if hasattr(self.carbon_type, 'to_alipay_dict'):
                params['carbon_type'] = self.carbon_type.to_alipay_dict()
            else:
                params['carbon_type'] = self.carbon_type
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialAntforestCarbonmonthQueryModel()
        if 'carbon_type' in d:
            o.carbon_type = d['carbon_type']
        if 'month' in d:
            o.month = d['month']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


