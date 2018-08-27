#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Scene import Scene


class CodeInfo(object):

    def __init__(self):
        self._goto_url = None
        self._scene = None

    @property
    def goto_url(self):
        return self._goto_url

    @goto_url.setter
    def goto_url(self, value):
        self._goto_url = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        if isinstance(value, Scene):
            self._scene = value
        else:
            self._scene = Scene.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.goto_url:
            if hasattr(self.goto_url, 'to_alipay_dict'):
                params['goto_url'] = self.goto_url.to_alipay_dict()
            else:
                params['goto_url'] = self.goto_url
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CodeInfo()
        if 'goto_url' in d:
            o.goto_url = d['goto_url']
        if 'scene' in d:
            o.scene = d['scene']
        return o


