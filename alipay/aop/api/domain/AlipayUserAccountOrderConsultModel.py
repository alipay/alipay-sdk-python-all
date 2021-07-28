#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsultParams import ConsultParams


class AlipayUserAccountOrderConsultModel(object):

    def __init__(self):
        self._ext_info = None
        self._hid = None
        self._logon_id = None
        self._scene_code = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, ConsultParams):
            self._ext_info = value
        else:
            self._ext_info = ConsultParams.from_alipay_dict(value)
    @property
    def hid(self):
        return self._hid

    @hid.setter
    def hid(self, value):
        self._hid = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.hid:
            if hasattr(self.hid, 'to_alipay_dict'):
                params['hid'] = self.hid.to_alipay_dict()
            else:
                params['hid'] = self.hid
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAccountOrderConsultModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'hid' in d:
            o.hid = d['hid']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


