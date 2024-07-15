#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaDataCreditscoreExemplifiedCoderainyQueryModel(object):

    def __init__(self):
        self._boolean_a = None
        self._openid = None
        self._string_a = None
        self._testcase_openid = None
        self._uid = None

    @property
    def boolean_a(self):
        return self._boolean_a

    @boolean_a.setter
    def boolean_a(self, value):
        self._boolean_a = value
    @property
    def openid(self):
        return self._openid

    @openid.setter
    def openid(self, value):
        self._openid = value
    @property
    def string_a(self):
        return self._string_a

    @string_a.setter
    def string_a(self, value):
        self._string_a = value
    @property
    def testcase_openid(self):
        return self._testcase_openid

    @testcase_openid.setter
    def testcase_openid(self, value):
        self._testcase_openid = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.boolean_a:
            if hasattr(self.boolean_a, 'to_alipay_dict'):
                params['boolean_a'] = self.boolean_a.to_alipay_dict()
            else:
                params['boolean_a'] = self.boolean_a
        if self.openid:
            if hasattr(self.openid, 'to_alipay_dict'):
                params['openid'] = self.openid.to_alipay_dict()
            else:
                params['openid'] = self.openid
        if self.string_a:
            if hasattr(self.string_a, 'to_alipay_dict'):
                params['string_a'] = self.string_a.to_alipay_dict()
            else:
                params['string_a'] = self.string_a
        if self.testcase_openid:
            if hasattr(self.testcase_openid, 'to_alipay_dict'):
                params['testcase_openid'] = self.testcase_openid.to_alipay_dict()
            else:
                params['testcase_openid'] = self.testcase_openid
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
        o = ZhimaDataCreditscoreExemplifiedCoderainyQueryModel()
        if 'boolean_a' in d:
            o.boolean_a = d['boolean_a']
        if 'openid' in d:
            o.openid = d['openid']
        if 'string_a' in d:
            o.string_a = d['string_a']
        if 'testcase_openid' in d:
            o.testcase_openid = d['testcase_openid']
        if 'uid' in d:
            o.uid = d['uid']
        return o


