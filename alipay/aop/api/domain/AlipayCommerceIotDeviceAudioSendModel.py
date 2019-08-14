#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotDeviceAudioSendModel(object):

    def __init__(self):
        self._audio_id = None
        self._audio_rule = None
        self._biz_tid = None
        self._play_type = None

    @property
    def audio_id(self):
        return self._audio_id

    @audio_id.setter
    def audio_id(self, value):
        self._audio_id = value
    @property
    def audio_rule(self):
        return self._audio_rule

    @audio_rule.setter
    def audio_rule(self, value):
        self._audio_rule = value
    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def play_type(self):
        return self._play_type

    @play_type.setter
    def play_type(self, value):
        self._play_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.audio_id:
            if hasattr(self.audio_id, 'to_alipay_dict'):
                params['audio_id'] = self.audio_id.to_alipay_dict()
            else:
                params['audio_id'] = self.audio_id
        if self.audio_rule:
            if hasattr(self.audio_rule, 'to_alipay_dict'):
                params['audio_rule'] = self.audio_rule.to_alipay_dict()
            else:
                params['audio_rule'] = self.audio_rule
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.play_type:
            if hasattr(self.play_type, 'to_alipay_dict'):
                params['play_type'] = self.play_type.to_alipay_dict()
            else:
                params['play_type'] = self.play_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDeviceAudioSendModel()
        if 'audio_id' in d:
            o.audio_id = d['audio_id']
        if 'audio_rule' in d:
            o.audio_rule = d['audio_rule']
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'play_type' in d:
            o.play_type = d['play_type']
        return o


