#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NOrderTagQueryByCoilNoResp(object):

    def __init__(self):
        self._bind_status = None
        self._position_id = None
        self._qr_code_url = None

    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, value):
        self._position_id = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_status:
            if hasattr(self.bind_status, 'to_alipay_dict'):
                params['bind_status'] = self.bind_status.to_alipay_dict()
            else:
                params['bind_status'] = self.bind_status
        if self.position_id:
            if hasattr(self.position_id, 'to_alipay_dict'):
                params['position_id'] = self.position_id.to_alipay_dict()
            else:
                params['position_id'] = self.position_id
        if self.qr_code_url:
            if hasattr(self.qr_code_url, 'to_alipay_dict'):
                params['qr_code_url'] = self.qr_code_url.to_alipay_dict()
            else:
                params['qr_code_url'] = self.qr_code_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NOrderTagQueryByCoilNoResp()
        if 'bind_status' in d:
            o.bind_status = d['bind_status']
        if 'position_id' in d:
            o.position_id = d['position_id']
        if 'qr_code_url' in d:
            o.qr_code_url = d['qr_code_url']
        return o


