#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EventAttrDTO import EventAttrDTO


class DetectEvent(object):

    def __init__(self):
        self._event_attrs = None
        self._event_code = None

    @property
    def event_attrs(self):
        return self._event_attrs

    @event_attrs.setter
    def event_attrs(self, value):
        if isinstance(value, list):
            self._event_attrs = list()
            for i in value:
                if isinstance(i, EventAttrDTO):
                    self._event_attrs.append(i)
                else:
                    self._event_attrs.append(EventAttrDTO.from_alipay_dict(i))
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_attrs:
            if isinstance(self.event_attrs, list):
                for i in range(0, len(self.event_attrs)):
                    element = self.event_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.event_attrs[i] = element.to_alipay_dict()
            if hasattr(self.event_attrs, 'to_alipay_dict'):
                params['event_attrs'] = self.event_attrs.to_alipay_dict()
            else:
                params['event_attrs'] = self.event_attrs
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DetectEvent()
        if 'event_attrs' in d:
            o.event_attrs = d['event_attrs']
        if 'event_code' in d:
            o.event_code = d['event_code']
        return o


