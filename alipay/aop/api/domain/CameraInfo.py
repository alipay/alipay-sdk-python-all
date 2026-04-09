#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CameraInfo(object):

    def __init__(self):
        self._auth_code = None
        self._camera_id = None
        self._rtsp = None
        self._vendor = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def camera_id(self):
        return self._camera_id

    @camera_id.setter
    def camera_id(self, value):
        self._camera_id = value
    @property
    def rtsp(self):
        return self._rtsp

    @rtsp.setter
    def rtsp(self, value):
        self._rtsp = value
    @property
    def vendor(self):
        return self._vendor

    @vendor.setter
    def vendor(self, value):
        self._vendor = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.camera_id:
            if hasattr(self.camera_id, 'to_alipay_dict'):
                params['camera_id'] = self.camera_id.to_alipay_dict()
            else:
                params['camera_id'] = self.camera_id
        if self.rtsp:
            if hasattr(self.rtsp, 'to_alipay_dict'):
                params['rtsp'] = self.rtsp.to_alipay_dict()
            else:
                params['rtsp'] = self.rtsp
        if self.vendor:
            if hasattr(self.vendor, 'to_alipay_dict'):
                params['vendor'] = self.vendor.to_alipay_dict()
            else:
                params['vendor'] = self.vendor
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CameraInfo()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'camera_id' in d:
            o.camera_id = d['camera_id']
        if 'rtsp' in d:
            o.rtsp = d['rtsp']
        if 'vendor' in d:
            o.vendor = d['vendor']
        return o


