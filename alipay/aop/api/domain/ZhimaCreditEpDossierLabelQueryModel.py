#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpDossierLabelQueryModel(object):

    def __init__(self):
        self._ep_cert_no = None
        self._scene_code = None
        self._show_flag = None

    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def show_flag(self):
        return self._show_flag

    @show_flag.setter
    def show_flag(self, value):
        self._show_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.show_flag:
            if hasattr(self.show_flag, 'to_alipay_dict'):
                params['show_flag'] = self.show_flag.to_alipay_dict()
            else:
                params['show_flag'] = self.show_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpDossierLabelQueryModel()
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'show_flag' in d:
            o.show_flag = d['show_flag']
        return o


