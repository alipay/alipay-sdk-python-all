#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthFieldDTO import AuthFieldDTO


class AuthFieldResponse(object):

    def __init__(self):
        self._records = None

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if isinstance(value, list):
            self._records = list()
            for i in value:
                if isinstance(i, AuthFieldDTO):
                    self._records.append(i)
                else:
                    self._records.append(AuthFieldDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.records:
            if isinstance(self.records, list):
                for i in range(0, len(self.records)):
                    element = self.records[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.records[i] = element.to_alipay_dict()
            if hasattr(self.records, 'to_alipay_dict'):
                params['records'] = self.records.to_alipay_dict()
            else:
                params['records'] = self.records
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthFieldResponse()
        if 'records' in d:
            o.records = d['records']
        return o


