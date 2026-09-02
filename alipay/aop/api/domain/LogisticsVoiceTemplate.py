#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsVoiceTemplate(object):

    def __init__(self):
        self._expire_time = None
        self._scene_type = None
        self._status = None
        self._voice_content_url = None
        self._voice_template_id = None
        self._voice_template_name = None
        self._voice_text = None

    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def voice_content_url(self):
        return self._voice_content_url

    @voice_content_url.setter
    def voice_content_url(self, value):
        self._voice_content_url = value
    @property
    def voice_template_id(self):
        return self._voice_template_id

    @voice_template_id.setter
    def voice_template_id(self, value):
        self._voice_template_id = value
    @property
    def voice_template_name(self):
        return self._voice_template_name

    @voice_template_name.setter
    def voice_template_name(self, value):
        self._voice_template_name = value
    @property
    def voice_text(self):
        return self._voice_text

    @voice_text.setter
    def voice_text(self, value):
        self._voice_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.voice_content_url:
            if hasattr(self.voice_content_url, 'to_alipay_dict'):
                params['voice_content_url'] = self.voice_content_url.to_alipay_dict()
            else:
                params['voice_content_url'] = self.voice_content_url
        if self.voice_template_id:
            if hasattr(self.voice_template_id, 'to_alipay_dict'):
                params['voice_template_id'] = self.voice_template_id.to_alipay_dict()
            else:
                params['voice_template_id'] = self.voice_template_id
        if self.voice_template_name:
            if hasattr(self.voice_template_name, 'to_alipay_dict'):
                params['voice_template_name'] = self.voice_template_name.to_alipay_dict()
            else:
                params['voice_template_name'] = self.voice_template_name
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
        o = LogisticsVoiceTemplate()
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'status' in d:
            o.status = d['status']
        if 'voice_content_url' in d:
            o.voice_content_url = d['voice_content_url']
        if 'voice_template_id' in d:
            o.voice_template_id = d['voice_template_id']
        if 'voice_template_name' in d:
            o.voice_template_name = d['voice_template_name']
        if 'voice_text' in d:
            o.voice_text = d['voice_text']
        return o


