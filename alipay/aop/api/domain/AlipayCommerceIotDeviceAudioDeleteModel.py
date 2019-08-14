#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotDeviceAudioDeleteModel(object):

    def __init__(self):
        self._audio_id = None
        self._biz_tid = None

    @property
    def audio_id(self):
        return self._audio_id

    @audio_id.setter
    def audio_id(self, value):
        self._audio_id = value
    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value


    def to_alipay_dict(self):
        params = dict()
        if self.audio_id:
            if hasattr(self.audio_id, 'to_alipay_dict'):
                params['audio_id'] = self.audio_id.to_alipay_dict()
            else:
                params['audio_id'] = self.audio_id
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDeviceAudioDeleteModel()
        if 'audio_id' in d:
            o.audio_id = d['audio_id']
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        return o


