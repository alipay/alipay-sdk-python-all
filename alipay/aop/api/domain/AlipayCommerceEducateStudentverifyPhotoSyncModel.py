#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateStudentverifyPhotoSyncModel(object):

    def __init__(self):
        self._isv_app_id = None
        self._out_student_id = None
        self._photo_url = None

    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value
    @property
    def out_student_id(self):
        return self._out_student_id

    @out_student_id.setter
    def out_student_id(self, value):
        self._out_student_id = value
    @property
    def photo_url(self):
        return self._photo_url

    @photo_url.setter
    def photo_url(self, value):
        self._photo_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_app_id:
            if hasattr(self.isv_app_id, 'to_alipay_dict'):
                params['isv_app_id'] = self.isv_app_id.to_alipay_dict()
            else:
                params['isv_app_id'] = self.isv_app_id
        if self.out_student_id:
            if hasattr(self.out_student_id, 'to_alipay_dict'):
                params['out_student_id'] = self.out_student_id.to_alipay_dict()
            else:
                params['out_student_id'] = self.out_student_id
        if self.photo_url:
            if hasattr(self.photo_url, 'to_alipay_dict'):
                params['photo_url'] = self.photo_url.to_alipay_dict()
            else:
                params['photo_url'] = self.photo_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateStudentverifyPhotoSyncModel()
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        if 'out_student_id' in d:
            o.out_student_id = d['out_student_id']
        if 'photo_url' in d:
            o.photo_url = d['photo_url']
        return o


