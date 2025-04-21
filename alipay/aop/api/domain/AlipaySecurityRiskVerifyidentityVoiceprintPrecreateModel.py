#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskVerifyidentityVoiceprintPrecreateModel(object):

    def __init__(self):
        self._base_64_audio_data = None
        self._device_id = None
        self._device_name = None
        self._register_info = None
        self._register_token = None
        self._voice_text = None

    @property
    def base_64_audio_data(self):
        return self._base_64_audio_data

    @base_64_audio_data.setter
    def base_64_audio_data(self, value):
        self._base_64_audio_data = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def register_info(self):
        return self._register_info

    @register_info.setter
    def register_info(self, value):
        self._register_info = value
    @property
    def register_token(self):
        return self._register_token

    @register_token.setter
    def register_token(self, value):
        self._register_token = value
    @property
    def voice_text(self):
        return self._voice_text

    @voice_text.setter
    def voice_text(self, value):
        self._voice_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_64_audio_data:
            if hasattr(self.base_64_audio_data, 'to_alipay_dict'):
                params['base_64_audio_data'] = self.base_64_audio_data.to_alipay_dict()
            else:
                params['base_64_audio_data'] = self.base_64_audio_data
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_name:
            if hasattr(self.device_name, 'to_alipay_dict'):
                params['device_name'] = self.device_name.to_alipay_dict()
            else:
                params['device_name'] = self.device_name
        if self.register_info:
            if hasattr(self.register_info, 'to_alipay_dict'):
                params['register_info'] = self.register_info.to_alipay_dict()
            else:
                params['register_info'] = self.register_info
        if self.register_token:
            if hasattr(self.register_token, 'to_alipay_dict'):
                params['register_token'] = self.register_token.to_alipay_dict()
            else:
                params['register_token'] = self.register_token
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
        o = AlipaySecurityRiskVerifyidentityVoiceprintPrecreateModel()
        if 'base_64_audio_data' in d:
            o.base_64_audio_data = d['base_64_audio_data']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'register_info' in d:
            o.register_info = d['register_info']
        if 'register_token' in d:
            o.register_token = d['register_token']
        if 'voice_text' in d:
            o.voice_text = d['voice_text']
        return o


