#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceRiskAudioQueryModel(object):

    def __init__(self):
        self._checker = None
        self._request_id = None
        self._risk_type = None

    @property
    def checker(self):
        return self._checker

    @checker.setter
    def checker(self, value):
        self._checker = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        if isinstance(value, list):
            self._risk_type = list()
            for i in value:
                self._risk_type.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.checker:
            if hasattr(self.checker, 'to_alipay_dict'):
                params['checker'] = self.checker.to_alipay_dict()
            else:
                params['checker'] = self.checker
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.risk_type:
            if isinstance(self.risk_type, list):
                for i in range(0, len(self.risk_type)):
                    element = self.risk_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_type[i] = element.to_alipay_dict()
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceRiskAudioQueryModel()
        if 'checker' in d:
            o.checker = d['checker']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        return o


