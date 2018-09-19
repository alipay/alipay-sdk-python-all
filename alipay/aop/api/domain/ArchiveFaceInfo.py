#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ArchiveFaceInfo(object):

    def __init__(self):
        self._face_image = None
        self._type = None
        self._usable = None

    @property
    def face_image(self):
        return self._face_image

    @face_image.setter
    def face_image(self, value):
        self._face_image = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def usable(self):
        return self._usable

    @usable.setter
    def usable(self, value):
        self._usable = value


    def to_alipay_dict(self):
        params = dict()
        if self.face_image:
            if hasattr(self.face_image, 'to_alipay_dict'):
                params['face_image'] = self.face_image.to_alipay_dict()
            else:
                params['face_image'] = self.face_image
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.usable:
            if hasattr(self.usable, 'to_alipay_dict'):
                params['usable'] = self.usable.to_alipay_dict()
            else:
                params['usable'] = self.usable
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArchiveFaceInfo()
        if 'face_image' in d:
            o.face_image = d['face_image']
        if 'type' in d:
            o.type = d['type']
        if 'usable' in d:
            o.usable = d['usable']
        return o


