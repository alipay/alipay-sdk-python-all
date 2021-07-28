#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InputScheduleLine(object):

    def __init__(self):
        self._direction = None
        self._ext_param = None
        self._line_id = None
        self._time_span = None

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def line_id(self):
        return self._line_id

    @line_id.setter
    def line_id(self, value):
        self._line_id = value
    @property
    def time_span(self):
        return self._time_span

    @time_span.setter
    def time_span(self, value):
        self._time_span = value


    def to_alipay_dict(self):
        params = dict()
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.line_id:
            if hasattr(self.line_id, 'to_alipay_dict'):
                params['line_id'] = self.line_id.to_alipay_dict()
            else:
                params['line_id'] = self.line_id
        if self.time_span:
            if hasattr(self.time_span, 'to_alipay_dict'):
                params['time_span'] = self.time_span.to_alipay_dict()
            else:
                params['time_span'] = self.time_span
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputScheduleLine()
        if 'direction' in d:
            o.direction = d['direction']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'time_span' in d:
            o.time_span = d['time_span']
        return o


