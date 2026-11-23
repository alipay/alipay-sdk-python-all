#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ValidateProductInfo(object):

    def __init__(self):
        self._face_score = None
        self._legal_person_cert_no = None
        self._legal_person_cert_type = None
        self._legal_person_name = None
        self._mobile_no = None
        self._product_name = None
        self._sms_code = None

    @property
    def face_score(self):
        return self._face_score

    @face_score.setter
    def face_score(self, value):
        self._face_score = value
    @property
    def legal_person_cert_no(self):
        return self._legal_person_cert_no

    @legal_person_cert_no.setter
    def legal_person_cert_no(self, value):
        self._legal_person_cert_no = value
    @property
    def legal_person_cert_type(self):
        return self._legal_person_cert_type

    @legal_person_cert_type.setter
    def legal_person_cert_type(self, value):
        self._legal_person_cert_type = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def sms_code(self):
        return self._sms_code

    @sms_code.setter
    def sms_code(self, value):
        self._sms_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.face_score:
            if hasattr(self.face_score, 'to_alipay_dict'):
                params['face_score'] = self.face_score.to_alipay_dict()
            else:
                params['face_score'] = self.face_score
        if self.legal_person_cert_no:
            if hasattr(self.legal_person_cert_no, 'to_alipay_dict'):
                params['legal_person_cert_no'] = self.legal_person_cert_no.to_alipay_dict()
            else:
                params['legal_person_cert_no'] = self.legal_person_cert_no
        if self.legal_person_cert_type:
            if hasattr(self.legal_person_cert_type, 'to_alipay_dict'):
                params['legal_person_cert_type'] = self.legal_person_cert_type.to_alipay_dict()
            else:
                params['legal_person_cert_type'] = self.legal_person_cert_type
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.sms_code:
            if hasattr(self.sms_code, 'to_alipay_dict'):
                params['sms_code'] = self.sms_code.to_alipay_dict()
            else:
                params['sms_code'] = self.sms_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ValidateProductInfo()
        if 'face_score' in d:
            o.face_score = d['face_score']
        if 'legal_person_cert_no' in d:
            o.legal_person_cert_no = d['legal_person_cert_no']
        if 'legal_person_cert_type' in d:
            o.legal_person_cert_type = d['legal_person_cert_type']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'sms_code' in d:
            o.sms_code = d['sms_code']
        return o


