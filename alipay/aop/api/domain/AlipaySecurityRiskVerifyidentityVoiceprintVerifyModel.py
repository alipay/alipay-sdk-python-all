#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskVerifyidentityVoiceprintVerifyModel(object):

    def __init__(self):
        self._base_64_audio_data = None
        self._device_id = None
        self._device_name = None
        self._flow_data = None
        self._long_verify_session_id = None
        self._out_biz_id = None
        self._verify_session_id = None
        self._voice_data_type = None
        self._voice_verify_step = None

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
    def flow_data(self):
        return self._flow_data

    @flow_data.setter
    def flow_data(self, value):
        self._flow_data = value
    @property
    def long_verify_session_id(self):
        return self._long_verify_session_id

    @long_verify_session_id.setter
    def long_verify_session_id(self, value):
        self._long_verify_session_id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def verify_session_id(self):
        return self._verify_session_id

    @verify_session_id.setter
    def verify_session_id(self, value):
        self._verify_session_id = value
    @property
    def voice_data_type(self):
        return self._voice_data_type

    @voice_data_type.setter
    def voice_data_type(self, value):
        self._voice_data_type = value
    @property
    def voice_verify_step(self):
        return self._voice_verify_step

    @voice_verify_step.setter
    def voice_verify_step(self, value):
        self._voice_verify_step = value


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
        if self.flow_data:
            if hasattr(self.flow_data, 'to_alipay_dict'):
                params['flow_data'] = self.flow_data.to_alipay_dict()
            else:
                params['flow_data'] = self.flow_data
        if self.long_verify_session_id:
            if hasattr(self.long_verify_session_id, 'to_alipay_dict'):
                params['long_verify_session_id'] = self.long_verify_session_id.to_alipay_dict()
            else:
                params['long_verify_session_id'] = self.long_verify_session_id
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.verify_session_id:
            if hasattr(self.verify_session_id, 'to_alipay_dict'):
                params['verify_session_id'] = self.verify_session_id.to_alipay_dict()
            else:
                params['verify_session_id'] = self.verify_session_id
        if self.voice_data_type:
            if hasattr(self.voice_data_type, 'to_alipay_dict'):
                params['voice_data_type'] = self.voice_data_type.to_alipay_dict()
            else:
                params['voice_data_type'] = self.voice_data_type
        if self.voice_verify_step:
            if hasattr(self.voice_verify_step, 'to_alipay_dict'):
                params['voice_verify_step'] = self.voice_verify_step.to_alipay_dict()
            else:
                params['voice_verify_step'] = self.voice_verify_step
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskVerifyidentityVoiceprintVerifyModel()
        if 'base_64_audio_data' in d:
            o.base_64_audio_data = d['base_64_audio_data']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'flow_data' in d:
            o.flow_data = d['flow_data']
        if 'long_verify_session_id' in d:
            o.long_verify_session_id = d['long_verify_session_id']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'verify_session_id' in d:
            o.verify_session_id = d['verify_session_id']
        if 'voice_data_type' in d:
            o.voice_data_type = d['voice_data_type']
        if 'voice_verify_step' in d:
            o.voice_verify_step = d['voice_verify_step']
        return o


