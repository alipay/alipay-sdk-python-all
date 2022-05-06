#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSceneUserUnsignModel(object):

    def __init__(self):
        self._alipay_school_id = None
        self._alipay_user_id = None
        self._face_user_id = None

    @property
    def alipay_school_id(self):
        return self._alipay_school_id

    @alipay_school_id.setter
    def alipay_school_id(self, value):
        self._alipay_school_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def face_user_id(self):
        return self._face_user_id

    @face_user_id.setter
    def face_user_id(self, value):
        self._face_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_school_id:
            if hasattr(self.alipay_school_id, 'to_alipay_dict'):
                params['alipay_school_id'] = self.alipay_school_id.to_alipay_dict()
            else:
                params['alipay_school_id'] = self.alipay_school_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.face_user_id:
            if hasattr(self.face_user_id, 'to_alipay_dict'):
                params['face_user_id'] = self.face_user_id.to_alipay_dict()
            else:
                params['face_user_id'] = self.face_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSceneUserUnsignModel()
        if 'alipay_school_id' in d:
            o.alipay_school_id = d['alipay_school_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'face_user_id' in d:
            o.face_user_id = d['face_user_id']
        return o


