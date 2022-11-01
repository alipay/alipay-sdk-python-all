#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JsonOpenidTest import JsonOpenidTest


class OpenidTestAll(object):

    def __init__(self):
        self._json = None
        self._jsonuid = None
        self._openid = None
        self._uid = None

    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, value):
        if isinstance(value, JsonOpenidTest):
            self._json = value
        else:
            self._json = JsonOpenidTest.from_alipay_dict(value)
    @property
    def jsonuid(self):
        return self._jsonuid

    @jsonuid.setter
    def jsonuid(self, value):
        self._jsonuid = value
    @property
    def openid(self):
        return self._openid

    @openid.setter
    def openid(self, value):
        self._openid = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.json:
            if hasattr(self.json, 'to_alipay_dict'):
                params['json'] = self.json.to_alipay_dict()
            else:
                params['json'] = self.json
        if self.jsonuid:
            if hasattr(self.jsonuid, 'to_alipay_dict'):
                params['jsonuid'] = self.jsonuid.to_alipay_dict()
            else:
                params['jsonuid'] = self.jsonuid
        if self.openid:
            if hasattr(self.openid, 'to_alipay_dict'):
                params['openid'] = self.openid.to_alipay_dict()
            else:
                params['openid'] = self.openid
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
        o = OpenidTestAll()
        if 'json' in d:
            o.json = d['json']
        if 'jsonuid' in d:
            o.jsonuid = d['jsonuid']
        if 'openid' in d:
            o.openid = d['openid']
        if 'uid' in d:
            o.uid = d['uid']
        return o


