#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateScenePhotoremoteApplyModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._image_content = None
        self._out_photo_id = None
        self._parent_phone_number = None
        self._school_std_code = None
        self._student_name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def image_content(self):
        return self._image_content

    @image_content.setter
    def image_content(self, value):
        self._image_content = value
    @property
    def out_photo_id(self):
        return self._out_photo_id

    @out_photo_id.setter
    def out_photo_id(self, value):
        self._out_photo_id = value
    @property
    def parent_phone_number(self):
        return self._parent_phone_number

    @parent_phone_number.setter
    def parent_phone_number(self, value):
        self._parent_phone_number = value
    @property
    def school_std_code(self):
        return self._school_std_code

    @school_std_code.setter
    def school_std_code(self, value):
        self._school_std_code = value
    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, value):
        self._student_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.image_content:
            if hasattr(self.image_content, 'to_alipay_dict'):
                params['image_content'] = self.image_content.to_alipay_dict()
            else:
                params['image_content'] = self.image_content
        if self.out_photo_id:
            if hasattr(self.out_photo_id, 'to_alipay_dict'):
                params['out_photo_id'] = self.out_photo_id.to_alipay_dict()
            else:
                params['out_photo_id'] = self.out_photo_id
        if self.parent_phone_number:
            if hasattr(self.parent_phone_number, 'to_alipay_dict'):
                params['parent_phone_number'] = self.parent_phone_number.to_alipay_dict()
            else:
                params['parent_phone_number'] = self.parent_phone_number
        if self.school_std_code:
            if hasattr(self.school_std_code, 'to_alipay_dict'):
                params['school_std_code'] = self.school_std_code.to_alipay_dict()
            else:
                params['school_std_code'] = self.school_std_code
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
        o = AlipayCommerceEducateScenePhotoremoteApplyModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'image_content' in d:
            o.image_content = d['image_content']
        if 'out_photo_id' in d:
            o.out_photo_id = d['out_photo_id']
        if 'parent_phone_number' in d:
            o.parent_phone_number = d['parent_phone_number']
        if 'school_std_code' in d:
            o.school_std_code = d['school_std_code']
        if 'student_name' in d:
            o.student_name = d['student_name']
        return o


