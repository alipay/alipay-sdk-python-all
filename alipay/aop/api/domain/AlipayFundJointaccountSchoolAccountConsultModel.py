#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundJointaccountSchoolAccountConsultModel(object):

    def __init__(self):
        self._biz_scene = None
        self._face_id = None
        self._master_open_id = None
        self._master_user_id = None
        self._product_code = None
        self._school_sign_type = None
        self._student_cert_no = None
        self._student_cert_type = None
        self._student_name = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value
    @property
    def master_open_id(self):
        return self._master_open_id

    @master_open_id.setter
    def master_open_id(self, value):
        self._master_open_id = value
    @property
    def master_user_id(self):
        return self._master_user_id

    @master_user_id.setter
    def master_user_id(self, value):
        self._master_user_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def school_sign_type(self):
        return self._school_sign_type

    @school_sign_type.setter
    def school_sign_type(self, value):
        self._school_sign_type = value
    @property
    def student_cert_no(self):
        return self._student_cert_no

    @student_cert_no.setter
    def student_cert_no(self, value):
        self._student_cert_no = value
    @property
    def student_cert_type(self):
        return self._student_cert_type

    @student_cert_type.setter
    def student_cert_type(self, value):
        self._student_cert_type = value
    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, value):
        self._student_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.face_id:
            if hasattr(self.face_id, 'to_alipay_dict'):
                params['face_id'] = self.face_id.to_alipay_dict()
            else:
                params['face_id'] = self.face_id
        if self.master_open_id:
            if hasattr(self.master_open_id, 'to_alipay_dict'):
                params['master_open_id'] = self.master_open_id.to_alipay_dict()
            else:
                params['master_open_id'] = self.master_open_id
        if self.master_user_id:
            if hasattr(self.master_user_id, 'to_alipay_dict'):
                params['master_user_id'] = self.master_user_id.to_alipay_dict()
            else:
                params['master_user_id'] = self.master_user_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.school_sign_type:
            if hasattr(self.school_sign_type, 'to_alipay_dict'):
                params['school_sign_type'] = self.school_sign_type.to_alipay_dict()
            else:
                params['school_sign_type'] = self.school_sign_type
        if self.student_cert_no:
            if hasattr(self.student_cert_no, 'to_alipay_dict'):
                params['student_cert_no'] = self.student_cert_no.to_alipay_dict()
            else:
                params['student_cert_no'] = self.student_cert_no
        if self.student_cert_type:
            if hasattr(self.student_cert_type, 'to_alipay_dict'):
                params['student_cert_type'] = self.student_cert_type.to_alipay_dict()
            else:
                params['student_cert_type'] = self.student_cert_type
        if self.student_name:
            if hasattr(self.student_name, 'to_alipay_dict'):
                params['student_name'] = self.student_name.to_alipay_dict()
            else:
                params['student_name'] = self.student_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundJointaccountSchoolAccountConsultModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'face_id' in d:
            o.face_id = d['face_id']
        if 'master_open_id' in d:
            o.master_open_id = d['master_open_id']
        if 'master_user_id' in d:
            o.master_user_id = d['master_user_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'school_sign_type' in d:
            o.school_sign_type = d['school_sign_type']
        if 'student_cert_no' in d:
            o.student_cert_no = d['student_cert_no']
        if 'student_cert_type' in d:
            o.student_cert_type = d['student_cert_type']
        if 'student_name' in d:
            o.student_name = d['student_name']
        return o


