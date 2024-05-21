#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NbChatChunk(object):

    def __init__(self):
        self._payload = None
        self._type = None

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        self._payload = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.payload:
            if hasattr(self.payload, 'to_alipay_dict'):
                params['payload'] = self.payload.to_alipay_dict()
            else:
                params['payload'] = self.payload
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
        o = NbChatChunk()
        if 'payload' in d:
            o.payload = d['payload']
        if 'type' in d:
            o.type = d['type']
        return o


