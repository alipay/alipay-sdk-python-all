#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CoordinateInfo(object):

    def __init__(self):
        self._content = None
        self._end_x = None
        self._end_y = None
        self._start_x = None
        self._start_y = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def end_x(self):
        return self._end_x

    @end_x.setter
    def end_x(self, value):
        self._end_x = value
    @property
    def end_y(self):
        return self._end_y

    @end_y.setter
    def end_y(self, value):
        self._end_y = value
    @property
    def start_x(self):
        return self._start_x

    @start_x.setter
    def start_x(self, value):
        self._start_x = value
    @property
    def start_y(self):
        return self._start_y

    @start_y.setter
    def start_y(self, value):
        self._start_y = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.end_x:
            if hasattr(self.end_x, 'to_alipay_dict'):
                params['end_x'] = self.end_x.to_alipay_dict()
            else:
                params['end_x'] = self.end_x
        if self.end_y:
            if hasattr(self.end_y, 'to_alipay_dict'):
                params['end_y'] = self.end_y.to_alipay_dict()
            else:
                params['end_y'] = self.end_y
        if self.start_x:
            if hasattr(self.start_x, 'to_alipay_dict'):
                params['start_x'] = self.start_x.to_alipay_dict()
            else:
                params['start_x'] = self.start_x
        if self.start_y:
            if hasattr(self.start_y, 'to_alipay_dict'):
                params['start_y'] = self.start_y.to_alipay_dict()
            else:
                params['start_y'] = self.start_y
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CoordinateInfo()
        if 'content' in d:
            o.content = d['content']
        if 'end_x' in d:
            o.end_x = d['end_x']
        if 'end_y' in d:
            o.end_y = d['end_y']
        if 'start_x' in d:
            o.start_x = d['start_x']
        if 'start_y' in d:
            o.start_y = d['start_y']
        return o


