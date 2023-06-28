#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WithholdSignInfo(object):

    def __init__(self):
        self._agreement_no = None
        self._agreement_status = None
        self._sign_scene = None
        self._sign_time = None
        self._unsign_time = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_status(self):
        return self._agreement_status

    @agreement_status.setter
    def agreement_status(self, value):
        self._agreement_status = value
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
    def unsign_time(self):
        return self._unsign_time

    @unsign_time.setter
    def unsign_time(self, value):
        self._unsign_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.agreement_status:
            if hasattr(self.agreement_status, 'to_alipay_dict'):
                params['agreement_status'] = self.agreement_status.to_alipay_dict()
            else:
                params['agreement_status'] = self.agreement_status
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
        if self.unsign_time:
            if hasattr(self.unsign_time, 'to_alipay_dict'):
                params['unsign_time'] = self.unsign_time.to_alipay_dict()
            else:
                params['unsign_time'] = self.unsign_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WithholdSignInfo()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'agreement_status' in d:
            o.agreement_status = d['agreement_status']
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'unsign_time' in d:
            o.unsign_time = d['unsign_time']
        return o


