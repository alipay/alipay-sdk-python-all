#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalPatientsigninPatientdataSendModel(object):

    def __init__(self):
        self._alipay_user = None
        self._aq_user = None
        self._hdf_user = None
        self._scene = None

    @property
    def alipay_user(self):
        return self._alipay_user

    @alipay_user.setter
    def alipay_user(self, value):
        self._alipay_user = value
    @property
    def aq_user(self):
        return self._aq_user

    @aq_user.setter
    def aq_user(self, value):
        self._aq_user = value
    @property
    def hdf_user(self):
        return self._hdf_user

    @hdf_user.setter
    def hdf_user(self, value):
        self._hdf_user = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user:
            if hasattr(self.alipay_user, 'to_alipay_dict'):
                params['alipay_user'] = self.alipay_user.to_alipay_dict()
            else:
                params['alipay_user'] = self.alipay_user
        if self.aq_user:
            if hasattr(self.aq_user, 'to_alipay_dict'):
                params['aq_user'] = self.aq_user.to_alipay_dict()
            else:
                params['aq_user'] = self.aq_user
        if self.hdf_user:
            if hasattr(self.hdf_user, 'to_alipay_dict'):
                params['hdf_user'] = self.hdf_user.to_alipay_dict()
            else:
                params['hdf_user'] = self.hdf_user
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalPatientsigninPatientdataSendModel()
        if 'alipay_user' in d:
            o.alipay_user = d['alipay_user']
        if 'aq_user' in d:
            o.aq_user = d['aq_user']
        if 'hdf_user' in d:
            o.hdf_user = d['hdf_user']
        if 'scene' in d:
            o.scene = d['scene']
        return o


