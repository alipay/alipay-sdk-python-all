#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreativityFatigue(object):

    def __init__(self):
        self._content_id = None
        self._content_type = None
        self._fatigue_id = None
        self._space_id = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def fatigue_id(self):
        return self._fatigue_id

    @fatigue_id.setter
    def fatigue_id(self, value):
        self._fatigue_id = value
    @property
    def space_id(self):
        return self._space_id

    @space_id.setter
    def space_id(self, value):
        self._space_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.fatigue_id:
            if hasattr(self.fatigue_id, 'to_alipay_dict'):
                params['fatigue_id'] = self.fatigue_id.to_alipay_dict()
            else:
                params['fatigue_id'] = self.fatigue_id
        if self.space_id:
            if hasattr(self.space_id, 'to_alipay_dict'):
                params['space_id'] = self.space_id.to_alipay_dict()
            else:
                params['space_id'] = self.space_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreativityFatigue()
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'fatigue_id' in d:
            o.fatigue_id = d['fatigue_id']
        if 'space_id' in d:
            o.space_id = d['space_id']
        return o


