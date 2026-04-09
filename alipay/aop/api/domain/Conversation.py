#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Conversation(object):

    def __init__(self):
        self._content = None
        self._create_time = None
        self._role = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Conversation()
        if 'content' in d:
            o.content = d['content']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'role' in d:
            o.role = d['role']
        return o


