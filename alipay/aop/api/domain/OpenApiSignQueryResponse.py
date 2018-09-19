#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiSignQueryResponse(object):

    def __init__(self):
        self._agreement_no = None
        self._invalid_time = None
        self._personal_product_code = None
        self._pricipal_type = None
        self._principal_id = None
        self._sign_scene = None
        self._sign_time = None
        self._status = None
        self._third_party_type = None
        self._valid_time = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def invalid_time(self):
        return self._invalid_time

    @invalid_time.setter
    def invalid_time(self, value):
        self._invalid_time = value
    @property
    def personal_product_code(self):
        return self._personal_product_code

    @personal_product_code.setter
    def personal_product_code(self, value):
        self._personal_product_code = value
    @property
    def pricipal_type(self):
        return self._pricipal_type

    @pricipal_type.setter
    def pricipal_type(self, value):
        self._pricipal_type = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def sign_scene(self):
        return self._sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self._sign_scene = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def third_party_type(self):
        return self._third_party_type

    @third_party_type.setter
    def third_party_type(self, value):
        self._third_party_type = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.invalid_time:
            if hasattr(self.invalid_time, 'to_alipay_dict'):
                params['invalid_time'] = self.invalid_time.to_alipay_dict()
            else:
                params['invalid_time'] = self.invalid_time
        if self.personal_product_code:
            if hasattr(self.personal_product_code, 'to_alipay_dict'):
                params['personal_product_code'] = self.personal_product_code.to_alipay_dict()
            else:
                params['personal_product_code'] = self.personal_product_code
        if self.pricipal_type:
            if hasattr(self.pricipal_type, 'to_alipay_dict'):
                params['pricipal_type'] = self.pricipal_type.to_alipay_dict()
            else:
                params['pricipal_type'] = self.pricipal_type
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.sign_scene:
            if hasattr(self.sign_scene, 'to_alipay_dict'):
                params['sign_scene'] = self.sign_scene.to_alipay_dict()
            else:
                params['sign_scene'] = self.sign_scene
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.third_party_type:
            if hasattr(self.third_party_type, 'to_alipay_dict'):
                params['third_party_type'] = self.third_party_type.to_alipay_dict()
            else:
                params['third_party_type'] = self.third_party_type
        if self.valid_time:
            if hasattr(self.valid_time, 'to_alipay_dict'):
                params['valid_time'] = self.valid_time.to_alipay_dict()
            else:
                params['valid_time'] = self.valid_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiSignQueryResponse()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'invalid_time' in d:
            o.invalid_time = d['invalid_time']
        if 'personal_product_code' in d:
            o.personal_product_code = d['personal_product_code']
        if 'pricipal_type' in d:
            o.pricipal_type = d['pricipal_type']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'status' in d:
            o.status = d['status']
        if 'third_party_type' in d:
            o.third_party_type = d['third_party_type']
        if 'valid_time' in d:
            o.valid_time = d['valid_time']
        return o


