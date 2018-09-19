#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaRiskDetail(object):

    def __init__(self):
        self._data_type = None
        self._extendinfo = None
        self._risk_code = None
        self._risk_type = None
        self._settlement = None
        self._statement = None
        self._status = None
        self._type = None
        self._update = None

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def extendinfo(self):
        return self._extendinfo

    @extendinfo.setter
    def extendinfo(self, value):
        self._extendinfo = value
    @property
    def risk_code(self):
        return self._risk_code

    @risk_code.setter
    def risk_code(self, value):
        self._risk_code = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value
    @property
    def settlement(self):
        return self._settlement

    @settlement.setter
    def settlement(self, value):
        self._settlement = value
    @property
    def statement(self):
        return self._statement

    @statement.setter
    def statement(self, value):
        self._statement = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def update(self):
        return self._update

    @update.setter
    def update(self, value):
        self._update = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.extendinfo:
            if hasattr(self.extendinfo, 'to_alipay_dict'):
                params['extendinfo'] = self.extendinfo.to_alipay_dict()
            else:
                params['extendinfo'] = self.extendinfo
        if self.risk_code:
            if hasattr(self.risk_code, 'to_alipay_dict'):
                params['risk_code'] = self.risk_code.to_alipay_dict()
            else:
                params['risk_code'] = self.risk_code
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        if self.settlement:
            if hasattr(self.settlement, 'to_alipay_dict'):
                params['settlement'] = self.settlement.to_alipay_dict()
            else:
                params['settlement'] = self.settlement
        if self.statement:
            if hasattr(self.statement, 'to_alipay_dict'):
                params['statement'] = self.statement.to_alipay_dict()
            else:
                params['statement'] = self.statement
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.update:
            if hasattr(self.update, 'to_alipay_dict'):
                params['update'] = self.update.to_alipay_dict()
            else:
                params['update'] = self.update
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaRiskDetail()
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'extendinfo' in d:
            o.extendinfo = d['extendinfo']
        if 'risk_code' in d:
            o.risk_code = d['risk_code']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        if 'settlement' in d:
            o.settlement = d['settlement']
        if 'statement' in d:
            o.statement = d['statement']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        if 'update' in d:
            o.update = d['update']
        return o


