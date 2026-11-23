#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Object import Object


class GrandsecurityBizrisksOpinionAlarmQueryModel(object):

    def __init__(self):
        self._alarm_query = None
        self._end_time_str = None
        self._order_bykey = None
        self._request_id = None
        self._start_time_str = None
        self._teamhash_id = None

    @property
    def alarm_query(self):
        return self._alarm_query

    @alarm_query.setter
    def alarm_query(self, value):
        if isinstance(value, Object):
            self._alarm_query = value
        else:
            self._alarm_query = Object.from_alipay_dict(value)
    @property
    def end_time_str(self):
        return self._end_time_str

    @end_time_str.setter
    def end_time_str(self, value):
        self._end_time_str = value
    @property
    def order_bykey(self):
        return self._order_bykey

    @order_bykey.setter
    def order_bykey(self, value):
        self._order_bykey = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def start_time_str(self):
        return self._start_time_str

    @start_time_str.setter
    def start_time_str(self, value):
        self._start_time_str = value
    @property
    def teamhash_id(self):
        return self._teamhash_id

    @teamhash_id.setter
    def teamhash_id(self, value):
        self._teamhash_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alarm_query:
            if hasattr(self.alarm_query, 'to_alipay_dict'):
                params['alarm_query'] = self.alarm_query.to_alipay_dict()
            else:
                params['alarm_query'] = self.alarm_query
        if self.end_time_str:
            if hasattr(self.end_time_str, 'to_alipay_dict'):
                params['end_time_str'] = self.end_time_str.to_alipay_dict()
            else:
                params['end_time_str'] = self.end_time_str
        if self.order_bykey:
            if hasattr(self.order_bykey, 'to_alipay_dict'):
                params['order_bykey'] = self.order_bykey.to_alipay_dict()
            else:
                params['order_bykey'] = self.order_bykey
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.start_time_str:
            if hasattr(self.start_time_str, 'to_alipay_dict'):
                params['start_time_str'] = self.start_time_str.to_alipay_dict()
            else:
                params['start_time_str'] = self.start_time_str
        if self.teamhash_id:
            if hasattr(self.teamhash_id, 'to_alipay_dict'):
                params['teamhash_id'] = self.teamhash_id.to_alipay_dict()
            else:
                params['teamhash_id'] = self.teamhash_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GrandsecurityBizrisksOpinionAlarmQueryModel()
        if 'alarm_query' in d:
            o.alarm_query = d['alarm_query']
        if 'end_time_str' in d:
            o.end_time_str = d['end_time_str']
        if 'order_bykey' in d:
            o.order_bykey = d['order_bykey']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'start_time_str' in d:
            o.start_time_str = d['start_time_str']
        if 'teamhash_id' in d:
            o.teamhash_id = d['teamhash_id']
        return o


