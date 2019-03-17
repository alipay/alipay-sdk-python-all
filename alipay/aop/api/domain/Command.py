#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Command(object):

    def __init__(self):
        self._commander = None
        self._content = None
        self._executor = None
        self._key = None

    @property
    def commander(self):
        return self._commander

    @commander.setter
    def commander(self, value):
        self._commander = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def executor(self):
        return self._executor

    @executor.setter
    def executor(self, value):
        self._executor = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value


    def to_alipay_dict(self):
        params = dict()
        if self.commander:
            if hasattr(self.commander, 'to_alipay_dict'):
                params['commander'] = self.commander.to_alipay_dict()
            else:
                params['commander'] = self.commander
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.executor:
            if hasattr(self.executor, 'to_alipay_dict'):
                params['executor'] = self.executor.to_alipay_dict()
            else:
                params['executor'] = self.executor
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Command()
        if 'commander' in d:
            o.commander = d['commander']
        if 'content' in d:
            o.content = d['content']
        if 'executor' in d:
            o.executor = d['executor']
        if 'key' in d:
            o.key = d['key']
        return o


