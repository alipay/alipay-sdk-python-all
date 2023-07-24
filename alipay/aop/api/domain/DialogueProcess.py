#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DialogueProcess(object):

    def __init__(self):
        self._actor = None
        self._content = None
        self._time = None
        self._type = None

    @property
    def actor(self):
        return self._actor

    @actor.setter
    def actor(self, value):
        self._actor = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.actor:
            if hasattr(self.actor, 'to_alipay_dict'):
                params['actor'] = self.actor.to_alipay_dict()
            else:
                params['actor'] = self.actor
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DialogueProcess()
        if 'actor' in d:
            o.actor = d['actor']
        if 'content' in d:
            o.content = d['content']
        if 'time' in d:
            o.time = d['time']
        if 'type' in d:
            o.type = d['type']
        return o


