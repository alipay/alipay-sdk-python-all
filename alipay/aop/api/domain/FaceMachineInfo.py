#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FaceMachineInfo(object):

    def __init__(self):
        self._camera_drive_ver = None
        self._camera_model = None
        self._camera_name = None
        self._camera_ver = None
        self._ext = None
        self._machine_code = None
        self._machine_model = None
        self._machine_ver = None

    @property
    def camera_drive_ver(self):
        return self._camera_drive_ver

    @camera_drive_ver.setter
    def camera_drive_ver(self, value):
        self._camera_drive_ver = value
    @property
    def camera_model(self):
        return self._camera_model

    @camera_model.setter
    def camera_model(self, value):
        self._camera_model = value
    @property
    def camera_name(self):
        return self._camera_name

    @camera_name.setter
    def camera_name(self, value):
        self._camera_name = value
    @property
    def camera_ver(self):
        return self._camera_ver

    @camera_ver.setter
    def camera_ver(self, value):
        self._camera_ver = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def machine_code(self):
        return self._machine_code

    @machine_code.setter
    def machine_code(self, value):
        self._machine_code = value
    @property
    def machine_model(self):
        return self._machine_model

    @machine_model.setter
    def machine_model(self, value):
        self._machine_model = value
    @property
    def machine_ver(self):
        return self._machine_ver

    @machine_ver.setter
    def machine_ver(self, value):
        self._machine_ver = value


    def to_alipay_dict(self):
        params = dict()
        if self.camera_drive_ver:
            if hasattr(self.camera_drive_ver, 'to_alipay_dict'):
                params['camera_drive_ver'] = self.camera_drive_ver.to_alipay_dict()
            else:
                params['camera_drive_ver'] = self.camera_drive_ver
        if self.camera_model:
            if hasattr(self.camera_model, 'to_alipay_dict'):
                params['camera_model'] = self.camera_model.to_alipay_dict()
            else:
                params['camera_model'] = self.camera_model
        if self.camera_name:
            if hasattr(self.camera_name, 'to_alipay_dict'):
                params['camera_name'] = self.camera_name.to_alipay_dict()
            else:
                params['camera_name'] = self.camera_name
        if self.camera_ver:
            if hasattr(self.camera_ver, 'to_alipay_dict'):
                params['camera_ver'] = self.camera_ver.to_alipay_dict()
            else:
                params['camera_ver'] = self.camera_ver
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.machine_code:
            if hasattr(self.machine_code, 'to_alipay_dict'):
                params['machine_code'] = self.machine_code.to_alipay_dict()
            else:
                params['machine_code'] = self.machine_code
        if self.machine_model:
            if hasattr(self.machine_model, 'to_alipay_dict'):
                params['machine_model'] = self.machine_model.to_alipay_dict()
            else:
                params['machine_model'] = self.machine_model
        if self.machine_ver:
            if hasattr(self.machine_ver, 'to_alipay_dict'):
                params['machine_ver'] = self.machine_ver.to_alipay_dict()
            else:
                params['machine_ver'] = self.machine_ver
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FaceMachineInfo()
        if 'camera_drive_ver' in d:
            o.camera_drive_ver = d['camera_drive_ver']
        if 'camera_model' in d:
            o.camera_model = d['camera_model']
        if 'camera_name' in d:
            o.camera_name = d['camera_name']
        if 'camera_ver' in d:
            o.camera_ver = d['camera_ver']
        if 'ext' in d:
            o.ext = d['ext']
        if 'machine_code' in d:
            o.machine_code = d['machine_code']
        if 'machine_model' in d:
            o.machine_model = d['machine_model']
        if 'machine_ver' in d:
            o.machine_ver = d['machine_ver']
        return o


