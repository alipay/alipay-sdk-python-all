#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WelfareAuthExtReq import WelfareAuthExtReq


class AlipayDigitalmgmtWelfareSupplierauthQueryModel(object):

    def __init__(self):
        self._api_key = None
        self._emp_sid = None
        self._ext_info = None
        self._login_id = None
        self._scene = None

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value
    @property
    def emp_sid(self):
        return self._emp_sid

    @emp_sid.setter
    def emp_sid(self, value):
        self._emp_sid = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, WelfareAuthExtReq):
            self._ext_info = value
        else:
            self._ext_info = WelfareAuthExtReq.from_alipay_dict(value)
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_key:
            if hasattr(self.api_key, 'to_alipay_dict'):
                params['api_key'] = self.api_key.to_alipay_dict()
            else:
                params['api_key'] = self.api_key
        if self.emp_sid:
            if hasattr(self.emp_sid, 'to_alipay_dict'):
                params['emp_sid'] = self.emp_sid.to_alipay_dict()
            else:
                params['emp_sid'] = self.emp_sid
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
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
        o = AlipayDigitalmgmtWelfareSupplierauthQueryModel()
        if 'api_key' in d:
            o.api_key = d['api_key']
        if 'emp_sid' in d:
            o.emp_sid = d['emp_sid']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'scene' in d:
            o.scene = d['scene']
        return o


