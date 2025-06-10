#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Solution(object):

    def __init__(self):
        self._available_pause_days = None
        self._code = None
        self._name = None
        self._need_notes = None

    @property
    def available_pause_days(self):
        return self._available_pause_days

    @available_pause_days.setter
    def available_pause_days(self, value):
        if isinstance(value, list):
            self._available_pause_days = list()
            for i in value:
                self._available_pause_days.append(i)
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def need_notes(self):
        return self._need_notes

    @need_notes.setter
    def need_notes(self, value):
        self._need_notes = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_pause_days:
            if isinstance(self.available_pause_days, list):
                for i in range(0, len(self.available_pause_days)):
                    element = self.available_pause_days[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_pause_days[i] = element.to_alipay_dict()
            if hasattr(self.available_pause_days, 'to_alipay_dict'):
                params['available_pause_days'] = self.available_pause_days.to_alipay_dict()
            else:
                params['available_pause_days'] = self.available_pause_days
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.need_notes:
            if hasattr(self.need_notes, 'to_alipay_dict'):
                params['need_notes'] = self.need_notes.to_alipay_dict()
            else:
                params['need_notes'] = self.need_notes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Solution()
        if 'available_pause_days' in d:
            o.available_pause_days = d['available_pause_days']
        if 'code' in d:
            o.code = d['code']
        if 'name' in d:
            o.name = d['name']
        if 'need_notes' in d:
            o.need_notes = d['need_notes']
        return o


