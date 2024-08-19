#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIdeployShiftQueryModel(object):

    def __init__(self):
        self._end_time = None
        self._nebula_user_id = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def nebula_user_id(self):
        return self._nebula_user_id

    @nebula_user_id.setter
    def nebula_user_id(self, value):
        self._nebula_user_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.nebula_user_id:
            if hasattr(self.nebula_user_id, 'to_alipay_dict'):
                params['nebula_user_id'] = self.nebula_user_id.to_alipay_dict()
            else:
                params['nebula_user_id'] = self.nebula_user_id
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
        o = AlipayIserviceIdeployShiftQueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'nebula_user_id' in d:
            o.nebula_user_id = d['nebula_user_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


