#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalUserDoctorSignModel(object):

    def __init__(self):
        self._doctor_id = None
        self._open_id = None
        self._sign_biz_id = None
        self._sign_biz_type = None
        self._source = None
        self._status = None
        self._user_id = None

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def sign_biz_id(self):
        return self._sign_biz_id

    @sign_biz_id.setter
    def sign_biz_id(self, value):
        self._sign_biz_id = value
    @property
    def sign_biz_type(self):
        return self._sign_biz_type

    @sign_biz_type.setter
    def sign_biz_type(self, value):
        self._sign_biz_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.sign_biz_id:
            if hasattr(self.sign_biz_id, 'to_alipay_dict'):
                params['sign_biz_id'] = self.sign_biz_id.to_alipay_dict()
            else:
                params['sign_biz_id'] = self.sign_biz_id
        if self.sign_biz_type:
            if hasattr(self.sign_biz_type, 'to_alipay_dict'):
                params['sign_biz_type'] = self.sign_biz_type.to_alipay_dict()
            else:
                params['sign_biz_type'] = self.sign_biz_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayCommerceMedicalUserDoctorSignModel()
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'sign_biz_id' in d:
            o.sign_biz_id = d['sign_biz_id']
        if 'sign_biz_type' in d:
            o.sign_biz_type = d['sign_biz_type']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


