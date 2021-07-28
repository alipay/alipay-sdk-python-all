#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdUserCreateModel(object):

    def __init__(self):
        self._alipay_pid = None
        self._biz_token = None
        self._status = None

    @property
    def alipay_pid(self):
        return self._alipay_pid

    @alipay_pid.setter
    def alipay_pid(self, value):
        self._alipay_pid = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_pid:
            if hasattr(self.alipay_pid, 'to_alipay_dict'):
                params['alipay_pid'] = self.alipay_pid.to_alipay_dict()
            else:
                params['alipay_pid'] = self.alipay_pid
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdUserCreateModel()
        if 'alipay_pid' in d:
            o.alipay_pid = d['alipay_pid']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'status' in d:
            o.status = d['status']
        return o


