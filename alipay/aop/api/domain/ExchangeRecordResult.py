#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FieldInfoResult import FieldInfoResult


class ExchangeRecordResult(object):

    def __init__(self):
        self._cert_status = None
        self._fields = None

    @property
    def cert_status(self):
        return self._cert_status

    @cert_status.setter
    def cert_status(self, value):
        self._cert_status = value
    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, value):
        if isinstance(value, list):
            self._fields = list()
            for i in value:
                if isinstance(i, FieldInfoResult):
                    self._fields.append(i)
                else:
                    self._fields.append(FieldInfoResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.cert_status:
            if hasattr(self.cert_status, 'to_alipay_dict'):
                params['cert_status'] = self.cert_status.to_alipay_dict()
            else:
                params['cert_status'] = self.cert_status
        if self.fields:
            if isinstance(self.fields, list):
                for i in range(0, len(self.fields)):
                    element = self.fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fields[i] = element.to_alipay_dict()
            if hasattr(self.fields, 'to_alipay_dict'):
                params['fields'] = self.fields.to_alipay_dict()
            else:
                params['fields'] = self.fields
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExchangeRecordResult()
        if 'cert_status' in d:
            o.cert_status = d['cert_status']
        if 'fields' in d:
            o.fields = d['fields']
        return o


