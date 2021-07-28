#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateFacepayCloseModel(object):

    def __init__(self):
        self._face_uid = None
        self._scene = None
        self._school_stdcode = None

    @property
    def face_uid(self):
        return self._face_uid

    @face_uid.setter
    def face_uid(self, value):
        self._face_uid = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def school_stdcode(self):
        return self._school_stdcode

    @school_stdcode.setter
    def school_stdcode(self, value):
        self._school_stdcode = value


    def to_alipay_dict(self):
        params = dict()
        if self.face_uid:
            if hasattr(self.face_uid, 'to_alipay_dict'):
                params['face_uid'] = self.face_uid.to_alipay_dict()
            else:
                params['face_uid'] = self.face_uid
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.school_stdcode:
            if hasattr(self.school_stdcode, 'to_alipay_dict'):
                params['school_stdcode'] = self.school_stdcode.to_alipay_dict()
            else:
                params['school_stdcode'] = self.school_stdcode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateFacepayCloseModel()
        if 'face_uid' in d:
            o.face_uid = d['face_uid']
        if 'scene' in d:
            o.scene = d['scene']
        if 'school_stdcode' in d:
            o.school_stdcode = d['school_stdcode']
        return o


