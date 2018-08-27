#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelRateBatchqueryModel(object):

    def __init__(self):
        self._currencies = None
        self._extend_param = None
        self._user_id = None

    @property
    def currencies(self):
        return self._currencies

    @currencies.setter
    def currencies(self, value):
        if isinstance(value, list):
            self._currencies = list()
            for i in value:
                self._currencies.append(i)
    @property
    def extend_param(self):
        return self._extend_param

    @extend_param.setter
    def extend_param(self, value):
        self._extend_param = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.currencies:
            if isinstance(self.currencies, list):
                for i in range(0, len(self.currencies)):
                    element = self.currencies[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.currencies[i] = element.to_alipay_dict()
            if hasattr(self.currencies, 'to_alipay_dict'):
                params['currencies'] = self.currencies.to_alipay_dict()
            else:
                params['currencies'] = self.currencies
        if self.extend_param:
            if hasattr(self.extend_param, 'to_alipay_dict'):
                params['extend_param'] = self.extend_param.to_alipay_dict()
            else:
                params['extend_param'] = self.extend_param
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
        o = AlipayOverseasTravelRateBatchqueryModel()
        if 'currencies' in d:
            o.currencies = d['currencies']
        if 'extend_param' in d:
            o.extend_param = d['extend_param']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


