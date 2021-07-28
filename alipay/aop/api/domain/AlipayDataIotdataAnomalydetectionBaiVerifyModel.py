#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataIotdataAnomalydetectionBaiVerifyModel(object):

    def __init__(self):
        self._current_frame = None
        self._current_time = None
        self._previous_frame = None
        self._previous_time = None
        self._session_id = None

    @property
    def current_frame(self):
        return self._current_frame

    @current_frame.setter
    def current_frame(self, value):
        self._current_frame = value
    @property
    def current_time(self):
        return self._current_time

    @current_time.setter
    def current_time(self, value):
        self._current_time = value
    @property
    def previous_frame(self):
        return self._previous_frame

    @previous_frame.setter
    def previous_frame(self, value):
        self._previous_frame = value
    @property
    def previous_time(self):
        return self._previous_time

    @previous_time.setter
    def previous_time(self, value):
        self._previous_time = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_frame:
            if hasattr(self.current_frame, 'to_alipay_dict'):
                params['current_frame'] = self.current_frame.to_alipay_dict()
            else:
                params['current_frame'] = self.current_frame
        if self.current_time:
            if hasattr(self.current_time, 'to_alipay_dict'):
                params['current_time'] = self.current_time.to_alipay_dict()
            else:
                params['current_time'] = self.current_time
        if self.previous_frame:
            if hasattr(self.previous_frame, 'to_alipay_dict'):
                params['previous_frame'] = self.previous_frame.to_alipay_dict()
            else:
                params['previous_frame'] = self.previous_frame
        if self.previous_time:
            if hasattr(self.previous_time, 'to_alipay_dict'):
                params['previous_time'] = self.previous_time.to_alipay_dict()
            else:
                params['previous_time'] = self.previous_time
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataIotdataAnomalydetectionBaiVerifyModel()
        if 'current_frame' in d:
            o.current_frame = d['current_frame']
        if 'current_time' in d:
            o.current_time = d['current_time']
        if 'previous_frame' in d:
            o.previous_frame = d['previous_frame']
        if 'previous_time' in d:
            o.previous_time = d['previous_time']
        if 'session_id' in d:
            o.session_id = d['session_id']
        return o


