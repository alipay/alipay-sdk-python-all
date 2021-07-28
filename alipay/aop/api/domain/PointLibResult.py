#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PointLibResult(object):

    def __init__(self):
        self._balance = None
        self._library_id = None
        self._library_name = None
        self._status = None
        self._sum_point = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def library_id(self):
        return self._library_id

    @library_id.setter
    def library_id(self, value):
        self._library_id = value
    @property
    def library_name(self):
        return self._library_name

    @library_name.setter
    def library_name(self, value):
        self._library_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sum_point(self):
        return self._sum_point

    @sum_point.setter
    def sum_point(self, value):
        self._sum_point = value


    def to_alipay_dict(self):
        params = dict()
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.library_id:
            if hasattr(self.library_id, 'to_alipay_dict'):
                params['library_id'] = self.library_id.to_alipay_dict()
            else:
                params['library_id'] = self.library_id
        if self.library_name:
            if hasattr(self.library_name, 'to_alipay_dict'):
                params['library_name'] = self.library_name.to_alipay_dict()
            else:
                params['library_name'] = self.library_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sum_point:
            if hasattr(self.sum_point, 'to_alipay_dict'):
                params['sum_point'] = self.sum_point.to_alipay_dict()
            else:
                params['sum_point'] = self.sum_point
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PointLibResult()
        if 'balance' in d:
            o.balance = d['balance']
        if 'library_id' in d:
            o.library_id = d['library_id']
        if 'library_name' in d:
            o.library_name = d['library_name']
        if 'status' in d:
            o.status = d['status']
        if 'sum_point' in d:
            o.sum_point = d['sum_point']
        return o


