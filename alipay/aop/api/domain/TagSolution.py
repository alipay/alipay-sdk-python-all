#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TagSolution(object):

    def __init__(self):
        self._code = None
        self._name = None
        self._need_notes = None

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
        o = TagSolution()
        if 'code' in d:
            o.code = d['code']
        if 'name' in d:
            o.name = d['name']
        if 'need_notes' in d:
            o.need_notes = d['need_notes']
        return o


