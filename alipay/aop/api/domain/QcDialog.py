#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QcDialog(object):

    def __init__(self):
        self._content = None
        self._end_offset = None
        self._end_time = None
        self._index = None
        self._role = None
        self._start_offset = None
        self._start_time = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def end_offset(self):
        return self._end_offset

    @end_offset.setter
    def end_offset(self, value):
        self._end_offset = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def start_offset(self):
        return self._start_offset

    @start_offset.setter
    def start_offset(self, value):
        self._start_offset = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.end_offset:
            if hasattr(self.end_offset, 'to_alipay_dict'):
                params['end_offset'] = self.end_offset.to_alipay_dict()
            else:
                params['end_offset'] = self.end_offset
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.start_offset:
            if hasattr(self.start_offset, 'to_alipay_dict'):
                params['start_offset'] = self.start_offset.to_alipay_dict()
            else:
                params['start_offset'] = self.start_offset
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
        o = QcDialog()
        if 'content' in d:
            o.content = d['content']
        if 'end_offset' in d:
            o.end_offset = d['end_offset']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'index' in d:
            o.index = d['index']
        if 'role' in d:
            o.role = d['role']
        if 'start_offset' in d:
            o.start_offset = d['start_offset']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


