#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayAgentVoiceUploadModel(object):

    def __init__(self):
        self._agent_voice_sid = None
        self._agreement_no = None
        self._base_64_audio_data = None
        self._device_name = None
        self._scene = None
        self._voice_data_type = None
        self._voice_verify_step = None

    @property
    def agent_voice_sid(self):
        return self._agent_voice_sid

    @agent_voice_sid.setter
    def agent_voice_sid(self, value):
        self._agent_voice_sid = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def base_64_audio_data(self):
        return self._base_64_audio_data

    @base_64_audio_data.setter
    def base_64_audio_data(self, value):
        self._base_64_audio_data = value
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
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
        if self.agent_voice_sid:
            if hasattr(self.agent_voice_sid, 'to_alipay_dict'):
                params['agent_voice_sid'] = self.agent_voice_sid.to_alipay_dict()
            else:
                params['agent_voice_sid'] = self.agent_voice_sid
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.base_64_audio_data:
            if hasattr(self.base_64_audio_data, 'to_alipay_dict'):
                params['base_64_audio_data'] = self.base_64_audio_data.to_alipay_dict()
            else:
                params['base_64_audio_data'] = self.base_64_audio_data
        if self.device_name:
            if hasattr(self.device_name, 'to_alipay_dict'):
                params['device_name'] = self.device_name.to_alipay_dict()
            else:
                params['device_name'] = self.device_name
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
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
        o = AlipayPayAgentVoiceUploadModel()
        if 'agent_voice_sid' in d:
            o.agent_voice_sid = d['agent_voice_sid']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'base_64_audio_data' in d:
            o.base_64_audio_data = d['base_64_audio_data']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'scene' in d:
            o.scene = d['scene']
        if 'voice_data_type' in d:
            o.voice_data_type = d['voice_data_type']
        if 'voice_verify_step' in d:
            o.voice_verify_step = d['voice_verify_step']
        return o


