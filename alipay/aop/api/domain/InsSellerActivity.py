#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsSellerActivity(object):

    def __init__(self):
        self._biz_data = None
        self._join_time = None
        self._status = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def join_time(self):
        return self._join_time

    @join_time.setter
    def join_time(self, value):
        self._join_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.join_time:
            if hasattr(self.join_time, 'to_alipay_dict'):
                params['join_time'] = self.join_time.to_alipay_dict()
            else:
                params['join_time'] = self.join_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsSellerActivity()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'join_time' in d:
            o.join_time = d['join_time']
        if 'status' in d:
            o.status = d['status']
        return o


