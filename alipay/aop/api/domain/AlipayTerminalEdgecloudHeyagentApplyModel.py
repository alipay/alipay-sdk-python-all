#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTerminalEdgecloudHeyagentApplyModel(object):

    def __init__(self):
        self._application_id = None
        self._biz_code = None
        self._boot_type = None
        self._open_id = None
        self._uid = None

    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        self._application_id = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def boot_type(self):
        return self._boot_type

    @boot_type.setter
    def boot_type(self, value):
        self._boot_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_id:
            if hasattr(self.application_id, 'to_alipay_dict'):
                params['application_id'] = self.application_id.to_alipay_dict()
            else:
                params['application_id'] = self.application_id
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.boot_type:
            if hasattr(self.boot_type, 'to_alipay_dict'):
                params['boot_type'] = self.boot_type.to_alipay_dict()
            else:
                params['boot_type'] = self.boot_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTerminalEdgecloudHeyagentApplyModel()
        if 'application_id' in d:
            o.application_id = d['application_id']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'boot_type' in d:
            o.boot_type = d['boot_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'uid' in d:
            o.uid = d['uid']
        return o


