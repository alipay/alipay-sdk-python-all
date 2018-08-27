#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdFacepayUploadModel(object):

    def __init__(self):
        self._check_code = None
        self._face_image = None
        self._store_id = None

    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def face_image(self):
        return self._face_image

    @face_image.setter
    def face_image(self, value):
        self._face_image = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
        if self.face_image:
            if hasattr(self.face_image, 'to_alipay_dict'):
                params['face_image'] = self.face_image.to_alipay_dict()
            else:
                params['face_image'] = self.face_image
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdFacepayUploadModel()
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'face_image' in d:
            o.face_image = d['face_image']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


