#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotDeviceAudioSyncModel(object):

    def __init__(self):
        self._biz_tid = None
        self._trade_id = None
        self._trade_type = None
        self._voice_content = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value
    @property
    def voice_content(self):
        return self._voice_content

    @voice_content.setter
    def voice_content(self, value):
        self._voice_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        if self.voice_content:
            if hasattr(self.voice_content, 'to_alipay_dict'):
                params['voice_content'] = self.voice_content.to_alipay_dict()
            else:
                params['voice_content'] = self.voice_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDeviceAudioSyncModel()
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        if 'voice_content' in d:
            o.voice_content = d['voice_content']
        return o


