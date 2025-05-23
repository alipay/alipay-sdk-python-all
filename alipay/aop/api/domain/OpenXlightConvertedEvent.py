#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenXlightConvertedEvent(object):

    def __init__(self):
        self._event = None
        self._name = None

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.event:
            if hasattr(self.event, 'to_alipay_dict'):
                params['event'] = self.event.to_alipay_dict()
            else:
                params['event'] = self.event
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenXlightConvertedEvent()
        if 'event' in d:
            o.event = d['event']
        if 'name' in d:
            o.name = d['name']
        return o


