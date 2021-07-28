#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomVoiceVO(object):

    def __init__(self):
        self._audio_id = None

    @property
    def audio_id(self):
        return self._audio_id

    @audio_id.setter
    def audio_id(self, value):
        self._audio_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.audio_id:
            if hasattr(self.audio_id, 'to_alipay_dict'):
                params['audio_id'] = self.audio_id.to_alipay_dict()
            else:
                params['audio_id'] = self.audio_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomVoiceVO()
        if 'audio_id' in d:
            o.audio_id = d['audio_id']
        return o


