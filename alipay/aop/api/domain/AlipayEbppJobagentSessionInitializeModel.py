#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppJobagentSessionInitializeModel(object):

    def __init__(self):
        self._out_session_id = None
        self._scene_type = None

    @property
    def out_session_id(self):
        return self._out_session_id

    @out_session_id.setter
    def out_session_id(self, value):
        self._out_session_id = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_session_id:
            if hasattr(self.out_session_id, 'to_alipay_dict'):
                params['out_session_id'] = self.out_session_id.to_alipay_dict()
            else:
                params['out_session_id'] = self.out_session_id
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppJobagentSessionInitializeModel()
        if 'out_session_id' in d:
            o.out_session_id = d['out_session_id']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


