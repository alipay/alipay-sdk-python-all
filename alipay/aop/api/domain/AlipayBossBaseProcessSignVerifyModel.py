#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossBaseProcessSignVerifyModel(object):

    def __init__(self):
        self._puid = None
        self._sign_content = None

    @property
    def puid(self):
        return self._puid

    @puid.setter
    def puid(self, value):
        self._puid = value
    @property
    def sign_content(self):
        return self._sign_content

    @sign_content.setter
    def sign_content(self, value):
        self._sign_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.puid:
            if hasattr(self.puid, 'to_alipay_dict'):
                params['puid'] = self.puid.to_alipay_dict()
            else:
                params['puid'] = self.puid
        if self.sign_content:
            if hasattr(self.sign_content, 'to_alipay_dict'):
                params['sign_content'] = self.sign_content.to_alipay_dict()
            else:
                params['sign_content'] = self.sign_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossBaseProcessSignVerifyModel()
        if 'puid' in d:
            o.puid = d['puid']
        if 'sign_content' in d:
            o.sign_content = d['sign_content']
        return o


