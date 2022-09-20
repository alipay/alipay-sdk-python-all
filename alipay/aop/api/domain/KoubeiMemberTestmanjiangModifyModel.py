#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMemberTestmanjiangModifyModel(object):

    def __init__(self):
        self._json_test = None
        self._sss_uid = None
        self._sss_uid_openid = None

    @property
    def json_test(self):
        return self._json_test

    @json_test.setter
    def json_test(self, value):
        self._json_test = value
    @property
    def sss_uid(self):
        return self._sss_uid

    @sss_uid.setter
    def sss_uid(self, value):
        self._sss_uid = value
    @property
    def sss_uid_openid(self):
        return self._sss_uid_openid

    @sss_uid_openid.setter
    def sss_uid_openid(self, value):
        self._sss_uid_openid = value


    def to_alipay_dict(self):
        params = dict()
        if self.json_test:
            if hasattr(self.json_test, 'to_alipay_dict'):
                params['json_test'] = self.json_test.to_alipay_dict()
            else:
                params['json_test'] = self.json_test
        if self.sss_uid:
            if hasattr(self.sss_uid, 'to_alipay_dict'):
                params['sss_uid'] = self.sss_uid.to_alipay_dict()
            else:
                params['sss_uid'] = self.sss_uid
        if self.sss_uid_openid:
            if hasattr(self.sss_uid_openid, 'to_alipay_dict'):
                params['sss_uid_openid'] = self.sss_uid_openid.to_alipay_dict()
            else:
                params['sss_uid_openid'] = self.sss_uid_openid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMemberTestmanjiangModifyModel()
        if 'json_test' in d:
            o.json_test = d['json_test']
        if 'sss_uid' in d:
            o.sss_uid = d['sss_uid']
        if 'sss_uid_openid' in d:
            o.sss_uid_openid = d['sss_uid_openid']
        return o


