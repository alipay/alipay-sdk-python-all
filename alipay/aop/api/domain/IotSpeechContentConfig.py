#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotSpeechContentConfig(object):

    def __init__(self):
        self._speech_content = None

    @property
    def speech_content(self):
        return self._speech_content

    @speech_content.setter
    def speech_content(self, value):
        self._speech_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.speech_content:
            if hasattr(self.speech_content, 'to_alipay_dict'):
                params['speech_content'] = self.speech_content.to_alipay_dict()
            else:
                params['speech_content'] = self.speech_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotSpeechContentConfig()
        if 'speech_content' in d:
            o.speech_content = d['speech_content']
        return o


