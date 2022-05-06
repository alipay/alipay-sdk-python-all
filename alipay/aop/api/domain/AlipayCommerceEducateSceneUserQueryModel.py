#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSceneUserQueryModel(object):

    def __init__(self):
        self._alipay_school_id = None
        self._alipay_user_id = None
        self._cert_no = None
        self._cert_type = None
        self._face_user_id = None
        self._name = None

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
    def face_user_id(self):
        return self._face_user_id

    @face_user_id.setter
    def face_user_id(self, value):
        self._face_user_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


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
        if self.face_user_id:
            if hasattr(self.face_user_id, 'to_alipay_dict'):
                params['face_user_id'] = self.face_user_id.to_alipay_dict()
            else:
                params['face_user_id'] = self.face_user_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSceneUserQueryModel()
        if 'alipay_school_id' in d:
            o.alipay_school_id = d['alipay_school_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'face_user_id' in d:
            o.face_user_id = d['face_user_id']
        if 'name' in d:
            o.name = d['name']
        return o


