#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationOpenbizmockRzoneQueryModel(object):

    def __init__(self):
        self._test_json = None
        self._uid = None
        self._uid_openid = None

    @property
    def test_json(self):
        return self._test_json

    @test_json.setter
    def test_json(self, value):
        self._test_json = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def uid_openid(self):
        return self._uid_openid

    @uid_openid.setter
    def uid_openid(self, value):
        self._uid_openid = value


    def to_alipay_dict(self):
        params = dict()
        if self.test_json:
            if hasattr(self.test_json, 'to_alipay_dict'):
                params['test_json'] = self.test_json.to_alipay_dict()
            else:
                params['test_json'] = self.test_json
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.uid_openid:
            if hasattr(self.uid_openid, 'to_alipay_dict'):
                params['uid_openid'] = self.uid_openid.to_alipay_dict()
            else:
                params['uid_openid'] = self.uid_openid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockRzoneQueryModel()
        if 'test_json' in d:
            o.test_json = d['test_json']
        if 'uid' in d:
            o.uid = d['uid']
        if 'uid_openid' in d:
            o.uid_openid = d['uid_openid']
        return o


