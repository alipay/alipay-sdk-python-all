#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozIdentificationCustomerEnrollcertifyInitializeModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_scene_name = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._face_type = None
        self._has_welcome_page = None
        self._metainfo = None
        self._mobile = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_scene_name(self):
        return self._biz_scene_name

    @biz_scene_name.setter
    def biz_scene_name(self, value):
        self._biz_scene_name = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
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
    def face_type(self):
        return self._face_type

    @face_type.setter
    def face_type(self, value):
        self._face_type = value
    @property
    def has_welcome_page(self):
        return self._has_welcome_page

    @has_welcome_page.setter
    def has_welcome_page(self, value):
        self._has_welcome_page = value
    @property
    def metainfo(self):
        return self._metainfo

    @metainfo.setter
    def metainfo(self, value):
        self._metainfo = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_scene_name:
            if hasattr(self.biz_scene_name, 'to_alipay_dict'):
                params['biz_scene_name'] = self.biz_scene_name.to_alipay_dict()
            else:
                params['biz_scene_name'] = self.biz_scene_name
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
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
        if self.face_type:
            if hasattr(self.face_type, 'to_alipay_dict'):
                params['face_type'] = self.face_type.to_alipay_dict()
            else:
                params['face_type'] = self.face_type
        if self.has_welcome_page:
            if hasattr(self.has_welcome_page, 'to_alipay_dict'):
                params['has_welcome_page'] = self.has_welcome_page.to_alipay_dict()
            else:
                params['has_welcome_page'] = self.has_welcome_page
        if self.metainfo:
            if hasattr(self.metainfo, 'to_alipay_dict'):
                params['metainfo'] = self.metainfo.to_alipay_dict()
            else:
                params['metainfo'] = self.metainfo
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozIdentificationCustomerEnrollcertifyInitializeModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_scene_name' in d:
            o.biz_scene_name = d['biz_scene_name']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'face_type' in d:
            o.face_type = d['face_type']
        if 'has_welcome_page' in d:
            o.has_welcome_page = d['has_welcome_page']
        if 'metainfo' in d:
            o.metainfo = d['metainfo']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


