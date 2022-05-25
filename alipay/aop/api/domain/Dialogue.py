#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Dialogue(object):

    def __init__(self):
        self._begin = None
        self._end = None
        self._pid = None
        self._role = None
        self._text = None

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        self._begin = value
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin:
            if hasattr(self.begin, 'to_alipay_dict'):
                params['begin'] = self.begin.to_alipay_dict()
            else:
                params['begin'] = self.begin
        if self.end:
            if hasattr(self.end, 'to_alipay_dict'):
                params['end'] = self.end.to_alipay_dict()
            else:
                params['end'] = self.end
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Dialogue()
        if 'begin' in d:
            o.begin = d['begin']
        if 'end' in d:
            o.end = d['end']
        if 'pid' in d:
            o.pid = d['pid']
        if 'role' in d:
            o.role = d['role']
        if 'text' in d:
            o.text = d['text']
        return o


