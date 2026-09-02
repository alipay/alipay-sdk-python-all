#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsVoiceSceneData(object):

    def __init__(self):
        self._biz_date = None
        self._dim_key = None
        self._dim_type = None
        self._dispatch_count = None
        self._play_success_count = None
        self._scene_type = None
        self._voice_template_id = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def dim_key(self):
        return self._dim_key

    @dim_key.setter
    def dim_key(self, value):
        self._dim_key = value
    @property
    def dim_type(self):
        return self._dim_type

    @dim_type.setter
    def dim_type(self, value):
        self._dim_type = value
    @property
    def dispatch_count(self):
        return self._dispatch_count

    @dispatch_count.setter
    def dispatch_count(self, value):
        self._dispatch_count = value
    @property
    def play_success_count(self):
        return self._play_success_count

    @play_success_count.setter
    def play_success_count(self, value):
        self._play_success_count = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def voice_template_id(self):
        return self._voice_template_id

    @voice_template_id.setter
    def voice_template_id(self, value):
        self._voice_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.dim_key:
            if hasattr(self.dim_key, 'to_alipay_dict'):
                params['dim_key'] = self.dim_key.to_alipay_dict()
            else:
                params['dim_key'] = self.dim_key
        if self.dim_type:
            if hasattr(self.dim_type, 'to_alipay_dict'):
                params['dim_type'] = self.dim_type.to_alipay_dict()
            else:
                params['dim_type'] = self.dim_type
        if self.dispatch_count:
            if hasattr(self.dispatch_count, 'to_alipay_dict'):
                params['dispatch_count'] = self.dispatch_count.to_alipay_dict()
            else:
                params['dispatch_count'] = self.dispatch_count
        if self.play_success_count:
            if hasattr(self.play_success_count, 'to_alipay_dict'):
                params['play_success_count'] = self.play_success_count.to_alipay_dict()
            else:
                params['play_success_count'] = self.play_success_count
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.voice_template_id:
            if hasattr(self.voice_template_id, 'to_alipay_dict'):
                params['voice_template_id'] = self.voice_template_id.to_alipay_dict()
            else:
                params['voice_template_id'] = self.voice_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsVoiceSceneData()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'dim_key' in d:
            o.dim_key = d['dim_key']
        if 'dim_type' in d:
            o.dim_type = d['dim_type']
        if 'dispatch_count' in d:
            o.dispatch_count = d['dispatch_count']
        if 'play_success_count' in d:
            o.play_success_count = d['play_success_count']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'voice_template_id' in d:
            o.voice_template_id = d['voice_template_id']
        return o


