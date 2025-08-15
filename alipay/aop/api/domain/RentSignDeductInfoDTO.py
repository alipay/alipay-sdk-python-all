#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentSignDeductInfoDTO(object):

    def __init__(self):
        self._sign_scene = None

    @property
    def sign_scene(self):
        return self._sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self._sign_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.sign_scene:
            if hasattr(self.sign_scene, 'to_alipay_dict'):
                params['sign_scene'] = self.sign_scene.to_alipay_dict()
            else:
                params['sign_scene'] = self.sign_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentSignDeductInfoDTO()
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        return o


