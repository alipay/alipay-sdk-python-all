#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAntlbsCrowdMatchModel(object):

    def __init__(self):
        self._crowd_code = None
        self._scene_code = None
        self._uid = None
        self._uid_type = None

    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        if isinstance(value, list):
            self._crowd_code = list()
            for i in value:
                self._crowd_code.append(i)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def uid_type(self):
        return self._uid_type

    @uid_type.setter
    def uid_type(self, value):
        self._uid_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_code:
            if isinstance(self.crowd_code, list):
                for i in range(0, len(self.crowd_code)):
                    element = self.crowd_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.crowd_code[i] = element.to_alipay_dict()
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.uid_type:
            if hasattr(self.uid_type, 'to_alipay_dict'):
                params['uid_type'] = self.uid_type.to_alipay_dict()
            else:
                params['uid_type'] = self.uid_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAntlbsCrowdMatchModel()
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'uid' in d:
            o.uid = d['uid']
        if 'uid_type' in d:
            o.uid_type = d['uid_type']
        return o


