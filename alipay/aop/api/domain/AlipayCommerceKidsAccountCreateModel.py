#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceKidsAccountCreateModel(object):

    def __init__(self):
        self._child_cert_no = None
        self._child_cert_type = None
        self._child_name = None
        self._class_name = None
        self._contact_mobile = None
        self._out_biz_id = None
        self._out_biz_type = None
        self._parent_uid = None
        self._scene_code = None
        self._school_id = None
        self._student_no = None

    @property
    def child_cert_no(self):
        return self._child_cert_no

    @child_cert_no.setter
    def child_cert_no(self, value):
        self._child_cert_no = value
    @property
    def child_cert_type(self):
        return self._child_cert_type

    @child_cert_type.setter
    def child_cert_type(self, value):
        self._child_cert_type = value
    @property
    def child_name(self):
        return self._child_name

    @child_name.setter
    def child_name(self, value):
        self._child_name = value
    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def parent_uid(self):
        return self._parent_uid

    @parent_uid.setter
    def parent_uid(self, value):
        self._parent_uid = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def school_id(self):
        return self._school_id

    @school_id.setter
    def school_id(self, value):
        self._school_id = value
    @property
    def student_no(self):
        return self._student_no

    @student_no.setter
    def student_no(self, value):
        self._student_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.child_cert_no:
            if hasattr(self.child_cert_no, 'to_alipay_dict'):
                params['child_cert_no'] = self.child_cert_no.to_alipay_dict()
            else:
                params['child_cert_no'] = self.child_cert_no
        if self.child_cert_type:
            if hasattr(self.child_cert_type, 'to_alipay_dict'):
                params['child_cert_type'] = self.child_cert_type.to_alipay_dict()
            else:
                params['child_cert_type'] = self.child_cert_type
        if self.child_name:
            if hasattr(self.child_name, 'to_alipay_dict'):
                params['child_name'] = self.child_name.to_alipay_dict()
            else:
                params['child_name'] = self.child_name
        if self.class_name:
            if hasattr(self.class_name, 'to_alipay_dict'):
                params['class_name'] = self.class_name.to_alipay_dict()
            else:
                params['class_name'] = self.class_name
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.parent_uid:
            if hasattr(self.parent_uid, 'to_alipay_dict'):
                params['parent_uid'] = self.parent_uid.to_alipay_dict()
            else:
                params['parent_uid'] = self.parent_uid
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.school_id:
            if hasattr(self.school_id, 'to_alipay_dict'):
                params['school_id'] = self.school_id.to_alipay_dict()
            else:
                params['school_id'] = self.school_id
        if self.student_no:
            if hasattr(self.student_no, 'to_alipay_dict'):
                params['student_no'] = self.student_no.to_alipay_dict()
            else:
                params['student_no'] = self.student_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceKidsAccountCreateModel()
        if 'child_cert_no' in d:
            o.child_cert_no = d['child_cert_no']
        if 'child_cert_type' in d:
            o.child_cert_type = d['child_cert_type']
        if 'child_name' in d:
            o.child_name = d['child_name']
        if 'class_name' in d:
            o.class_name = d['class_name']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'parent_uid' in d:
            o.parent_uid = d['parent_uid']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'school_id' in d:
            o.school_id = d['school_id']
        if 'student_no' in d:
            o.student_no = d['student_no']
        return o


