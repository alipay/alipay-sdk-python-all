#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NfcPointRefreshVoiceResource(object):

    def __init__(self):
        self._device_type = None
        self._voice_position = None
        self._voice_url = None

    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def voice_position(self):
        return self._voice_position

    @voice_position.setter
    def voice_position(self, value):
        self._voice_position = value
    @property
    def voice_url(self):
        return self._voice_url

    @voice_url.setter
    def voice_url(self, value):
        self._voice_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.voice_position:
            if hasattr(self.voice_position, 'to_alipay_dict'):
                params['voice_position'] = self.voice_position.to_alipay_dict()
            else:
                params['voice_position'] = self.voice_position
        if self.voice_url:
            if hasattr(self.voice_url, 'to_alipay_dict'):
                params['voice_url'] = self.voice_url.to_alipay_dict()
            else:
                params['voice_url'] = self.voice_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NfcPointRefreshVoiceResource()
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'voice_position' in d:
            o.voice_position = d['voice_position']
        if 'voice_url' in d:
            o.voice_url = d['voice_url']
        return o


