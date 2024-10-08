#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MsgSceneDTO(object):

    def __init__(self):
        self._biz_scene = None
        self._need_push = None
        self._send_time = None
        self._template_type = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def need_push(self):
        return self._need_push

    @need_push.setter
    def need_push(self, value):
        self._need_push = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.need_push:
            if hasattr(self.need_push, 'to_alipay_dict'):
                params['need_push'] = self.need_push.to_alipay_dict()
            else:
                params['need_push'] = self.need_push
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        if self.template_type:
            if hasattr(self.template_type, 'to_alipay_dict'):
                params['template_type'] = self.template_type.to_alipay_dict()
            else:
                params['template_type'] = self.template_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MsgSceneDTO()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'need_push' in d:
            o.need_push = d['need_push']
        if 'send_time' in d:
            o.send_time = d['send_time']
        if 'template_type' in d:
            o.template_type = d['template_type']
        return o


