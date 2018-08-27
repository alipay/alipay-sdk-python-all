#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAuthIndustryPlatformCreateTokenModel(object):

    def __init__(self):
        self._isv_appid = None
        self._scope = None

    @property
    def isv_appid(self):
        return self._isv_appid

    @isv_appid.setter
    def isv_appid(self, value):
        self._isv_appid = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_appid:
            if hasattr(self.isv_appid, 'to_alipay_dict'):
                params['isv_appid'] = self.isv_appid.to_alipay_dict()
            else:
                params['isv_appid'] = self.isv_appid
        if self.scope:
            if hasattr(self.scope, 'to_alipay_dict'):
                params['scope'] = self.scope.to_alipay_dict()
            else:
                params['scope'] = self.scope
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthIndustryPlatformCreateTokenModel()
        if 'isv_appid' in d:
            o.isv_appid = d['isv_appid']
        if 'scope' in d:
            o.scope = d['scope']
        return o


