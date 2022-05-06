#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInspetprodSubscribeQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._channel = None
        self._encryption_mark_id = None
        self._mark_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def encryption_mark_id(self):
        return self._encryption_mark_id

    @encryption_mark_id.setter
    def encryption_mark_id(self, value):
        self._encryption_mark_id = value
    @property
    def mark_id(self):
        return self._mark_id

    @mark_id.setter
    def mark_id(self, value):
        self._mark_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.encryption_mark_id:
            if hasattr(self.encryption_mark_id, 'to_alipay_dict'):
                params['encryption_mark_id'] = self.encryption_mark_id.to_alipay_dict()
            else:
                params['encryption_mark_id'] = self.encryption_mark_id
        if self.mark_id:
            if hasattr(self.mark_id, 'to_alipay_dict'):
                params['mark_id'] = self.mark_id.to_alipay_dict()
            else:
                params['mark_id'] = self.mark_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInspetprodSubscribeQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'channel' in d:
            o.channel = d['channel']
        if 'encryption_mark_id' in d:
            o.encryption_mark_id = d['encryption_mark_id']
        if 'mark_id' in d:
            o.mark_id = d['mark_id']
        return o


