#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DataSecCheckResult(object):

    def __init__(self):
        self._check_date = None
        self._data_id = None
        self._data_status = None

    @property
    def check_date(self):
        return self._check_date

    @check_date.setter
    def check_date(self, value):
        self._check_date = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def data_status(self):
        return self._data_status

    @data_status.setter
    def data_status(self, value):
        self._data_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_date:
            if hasattr(self.check_date, 'to_alipay_dict'):
                params['check_date'] = self.check_date.to_alipay_dict()
            else:
                params['check_date'] = self.check_date
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.data_status:
            if hasattr(self.data_status, 'to_alipay_dict'):
                params['data_status'] = self.data_status.to_alipay_dict()
            else:
                params['data_status'] = self.data_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataSecCheckResult()
        if 'check_date' in d:
            o.check_date = d['check_date']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'data_status' in d:
            o.data_status = d['data_status']
        return o


