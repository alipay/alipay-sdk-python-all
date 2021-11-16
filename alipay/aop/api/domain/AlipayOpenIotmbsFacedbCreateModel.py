#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsFacedbCreateModel(object):

    def __init__(self):
        self._face_id = None
        self._face_image = None
        self._phone_no = None
        self._project_id = None

    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value
    @property
    def face_image(self):
        return self._face_image

    @face_image.setter
    def face_image(self, value):
        self._face_image = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.face_id:
            if hasattr(self.face_id, 'to_alipay_dict'):
                params['face_id'] = self.face_id.to_alipay_dict()
            else:
                params['face_id'] = self.face_id
        if self.face_image:
            if hasattr(self.face_image, 'to_alipay_dict'):
                params['face_image'] = self.face_image.to_alipay_dict()
            else:
                params['face_image'] = self.face_image
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsFacedbCreateModel()
        if 'face_id' in d:
            o.face_id = d['face_id']
        if 'face_image' in d:
            o.face_image = d['face_image']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'project_id' in d:
            o.project_id = d['project_id']
        return o


