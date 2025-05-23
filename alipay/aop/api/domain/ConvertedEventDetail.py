#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConvertedEventDetail(object):

    def __init__(self):
        self._converted_event = None
        self._converted_event_name = None

    @property
    def converted_event(self):
        return self._converted_event

    @converted_event.setter
    def converted_event(self, value):
        self._converted_event = value
    @property
    def converted_event_name(self):
        return self._converted_event_name

    @converted_event_name.setter
    def converted_event_name(self, value):
        self._converted_event_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.converted_event:
            if hasattr(self.converted_event, 'to_alipay_dict'):
                params['converted_event'] = self.converted_event.to_alipay_dict()
            else:
                params['converted_event'] = self.converted_event
        if self.converted_event_name:
            if hasattr(self.converted_event_name, 'to_alipay_dict'):
                params['converted_event_name'] = self.converted_event_name.to_alipay_dict()
            else:
                params['converted_event_name'] = self.converted_event_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConvertedEventDetail()
        if 'converted_event' in d:
            o.converted_event = d['converted_event']
        if 'converted_event_name' in d:
            o.converted_event_name = d['converted_event_name']
        return o


