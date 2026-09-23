#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoiceContent(object):

    def __init__(self):
        self._speaker = None
        self._touchpoint_type = None
        self._voice_text = None

    @property
    def speaker(self):
        return self._speaker

    @speaker.setter
    def speaker(self, value):
        self._speaker = value
    @property
    def touchpoint_type(self):
        return self._touchpoint_type

    @touchpoint_type.setter
    def touchpoint_type(self, value):
        self._touchpoint_type = value
    @property
    def voice_text(self):
        return self._voice_text

    @voice_text.setter
    def voice_text(self, value):
        self._voice_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.speaker:
            if hasattr(self.speaker, 'to_alipay_dict'):
                params['speaker'] = self.speaker.to_alipay_dict()
            else:
                params['speaker'] = self.speaker
        if self.touchpoint_type:
            if hasattr(self.touchpoint_type, 'to_alipay_dict'):
                params['touchpoint_type'] = self.touchpoint_type.to_alipay_dict()
            else:
                params['touchpoint_type'] = self.touchpoint_type
        if self.voice_text:
            if hasattr(self.voice_text, 'to_alipay_dict'):
                params['voice_text'] = self.voice_text.to_alipay_dict()
            else:
                params['voice_text'] = self.voice_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoiceContent()
        if 'speaker' in d:
            o.speaker = d['speaker']
        if 'touchpoint_type' in d:
            o.touchpoint_type = d['touchpoint_type']
        if 'voice_text' in d:
            o.voice_text = d['voice_text']
        return o


