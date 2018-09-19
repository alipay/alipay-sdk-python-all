#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceDatabusSendModel(object):

    def __init__(self):
        self._event_code = None
        self._event_payload = None
        self._payload_class = None
        self._topic = None

    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def event_payload(self):
        return self._event_payload

    @event_payload.setter
    def event_payload(self, value):
        self._event_payload = value
    @property
    def payload_class(self):
        return self._payload_class

    @payload_class.setter
    def payload_class(self, value):
        self._payload_class = value
    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, value):
        self._topic = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.event_payload:
            if hasattr(self.event_payload, 'to_alipay_dict'):
                params['event_payload'] = self.event_payload.to_alipay_dict()
            else:
                params['event_payload'] = self.event_payload
        if self.payload_class:
            if hasattr(self.payload_class, 'to_alipay_dict'):
                params['payload_class'] = self.payload_class.to_alipay_dict()
            else:
                params['payload_class'] = self.payload_class
        if self.topic:
            if hasattr(self.topic, 'to_alipay_dict'):
                params['topic'] = self.topic.to_alipay_dict()
            else:
                params['topic'] = self.topic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceDatabusSendModel()
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'event_payload' in d:
            o.event_payload = d['event_payload']
        if 'payload_class' in d:
            o.payload_class = d['payload_class']
        if 'topic' in d:
            o.topic = d['topic']
        return o


