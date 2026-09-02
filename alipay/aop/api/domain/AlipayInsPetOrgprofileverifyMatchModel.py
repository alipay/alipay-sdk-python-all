#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsPetOrgprofileverifyMatchModel(object):

    def __init__(self):
        self._org_code = None
        self._pet_face_url = None
        self._pet_type = None

    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def pet_face_url(self):
        return self._pet_face_url

    @pet_face_url.setter
    def pet_face_url(self, value):
        self._pet_face_url = value
    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        self._pet_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.pet_face_url:
            if hasattr(self.pet_face_url, 'to_alipay_dict'):
                params['pet_face_url'] = self.pet_face_url.to_alipay_dict()
            else:
                params['pet_face_url'] = self.pet_face_url
        if self.pet_type:
            if hasattr(self.pet_type, 'to_alipay_dict'):
                params['pet_type'] = self.pet_type.to_alipay_dict()
            else:
                params['pet_type'] = self.pet_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsPetOrgprofileverifyMatchModel()
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'pet_face_url' in d:
            o.pet_face_url = d['pet_face_url']
        if 'pet_type' in d:
            o.pet_type = d['pet_type']
        return o


