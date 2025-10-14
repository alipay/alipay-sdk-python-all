#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentDeductInfoDTO(object):

    def __init__(self):
        self._agreement_no = None
        self._service_name = None
        self._sign_scene = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def sign_scene(self):
        return self._sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self._sign_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.sign_scene:
            if hasattr(self.sign_scene, 'to_alipay_dict'):
                params['sign_scene'] = self.sign_scene.to_alipay_dict()
            else:
                params['sign_scene'] = self.sign_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentDeductInfoDTO()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        return o


