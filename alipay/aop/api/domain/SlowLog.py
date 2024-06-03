#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SlowLog(object):

    def __init__(self):
        self._client_ip = None
        self._collection_name = None
        self._cost = None
        self._execute_time = None
        self._function_name = None
        self._request_body = None
        self._row_count = None

    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def collection_name(self):
        return self._collection_name

    @collection_name.setter
    def collection_name(self, value):
        self._collection_name = value
    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value
    @property
    def execute_time(self):
        return self._execute_time

    @execute_time.setter
    def execute_time(self, value):
        self._execute_time = value
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value
    @property
    def request_body(self):
        return self._request_body

    @request_body.setter
    def request_body(self, value):
        self._request_body = value
    @property
    def row_count(self):
        return self._row_count

    @row_count.setter
    def row_count(self, value):
        self._row_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.collection_name:
            if hasattr(self.collection_name, 'to_alipay_dict'):
                params['collection_name'] = self.collection_name.to_alipay_dict()
            else:
                params['collection_name'] = self.collection_name
        if self.cost:
            if hasattr(self.cost, 'to_alipay_dict'):
                params['cost'] = self.cost.to_alipay_dict()
            else:
                params['cost'] = self.cost
        if self.execute_time:
            if hasattr(self.execute_time, 'to_alipay_dict'):
                params['execute_time'] = self.execute_time.to_alipay_dict()
            else:
                params['execute_time'] = self.execute_time
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        if self.request_body:
            if hasattr(self.request_body, 'to_alipay_dict'):
                params['request_body'] = self.request_body.to_alipay_dict()
            else:
                params['request_body'] = self.request_body
        if self.row_count:
            if hasattr(self.row_count, 'to_alipay_dict'):
                params['row_count'] = self.row_count.to_alipay_dict()
            else:
                params['row_count'] = self.row_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SlowLog()
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'collection_name' in d:
            o.collection_name = d['collection_name']
        if 'cost' in d:
            o.cost = d['cost']
        if 'execute_time' in d:
            o.execute_time = d['execute_time']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'request_body' in d:
            o.request_body = d['request_body']
        if 'row_count' in d:
            o.row_count = d['row_count']
        return o


