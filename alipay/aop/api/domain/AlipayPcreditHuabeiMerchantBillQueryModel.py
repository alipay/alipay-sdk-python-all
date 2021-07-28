#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiMerchantBillQueryModel(object):

    def __init__(self):
        self._aggr_id = None
        self._end_time = None
        self._start_time = None

    @property
    def aggr_id(self):
        return self._aggr_id

    @aggr_id.setter
    def aggr_id(self, value):
        self._aggr_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggr_id:
            if hasattr(self.aggr_id, 'to_alipay_dict'):
                params['aggr_id'] = self.aggr_id.to_alipay_dict()
            else:
                params['aggr_id'] = self.aggr_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiMerchantBillQueryModel()
        if 'aggr_id' in d:
            o.aggr_id = d['aggr_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


