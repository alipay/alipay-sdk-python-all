#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IcrowdUseContext(object):

    def __init__(self):
        self._debug = None
        self._owner = None
        self._scene_code = None
        self._show_delay = None

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, value):
        self._debug = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def show_delay(self):
        return self._show_delay

    @show_delay.setter
    def show_delay(self, value):
        self._show_delay = value


    def to_alipay_dict(self):
        params = dict()
        if self.debug:
            if hasattr(self.debug, 'to_alipay_dict'):
                params['debug'] = self.debug.to_alipay_dict()
            else:
                params['debug'] = self.debug
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.show_delay:
            if hasattr(self.show_delay, 'to_alipay_dict'):
                params['show_delay'] = self.show_delay.to_alipay_dict()
            else:
                params['show_delay'] = self.show_delay
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IcrowdUseContext()
        if 'debug' in d:
            o.debug = d['debug']
        if 'owner' in d:
            o.owner = d['owner']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'show_delay' in d:
            o.show_delay = d['show_delay']
        return o


