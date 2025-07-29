#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AudioValueRequest(object):

    def __init__(self):
        self._audio_id = None
        self._audio_name = None
        self._audio_size = None
        self._audio_type = None

    @property
    def audio_id(self):
        return self._audio_id

    @audio_id.setter
    def audio_id(self, value):
        self._audio_id = value
    @property
    def audio_name(self):
        return self._audio_name

    @audio_name.setter
    def audio_name(self, value):
        self._audio_name = value
    @property
    def audio_size(self):
        return self._audio_size

    @audio_size.setter
    def audio_size(self, value):
        self._audio_size = value
    @property
    def audio_type(self):
        return self._audio_type

    @audio_type.setter
    def audio_type(self, value):
        self._audio_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.audio_id:
            if hasattr(self.audio_id, 'to_alipay_dict'):
                params['audio_id'] = self.audio_id.to_alipay_dict()
            else:
                params['audio_id'] = self.audio_id
        if self.audio_name:
            if hasattr(self.audio_name, 'to_alipay_dict'):
                params['audio_name'] = self.audio_name.to_alipay_dict()
            else:
                params['audio_name'] = self.audio_name
        if self.audio_size:
            if hasattr(self.audio_size, 'to_alipay_dict'):
                params['audio_size'] = self.audio_size.to_alipay_dict()
            else:
                params['audio_size'] = self.audio_size
        if self.audio_type:
            if hasattr(self.audio_type, 'to_alipay_dict'):
                params['audio_type'] = self.audio_type.to_alipay_dict()
            else:
                params['audio_type'] = self.audio_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AudioValueRequest()
        if 'audio_id' in d:
            o.audio_id = d['audio_id']
        if 'audio_name' in d:
            o.audio_name = d['audio_name']
        if 'audio_size' in d:
            o.audio_size = d['audio_size']
        if 'audio_type' in d:
            o.audio_type = d['audio_type']
        return o


