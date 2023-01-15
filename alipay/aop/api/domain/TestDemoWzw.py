#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TestDemoWzw(object):

    def __init__(self):
        self._oid_open_id = None
        self._uid = None

    @property
    def oid_open_id(self):
        return self._oid_open_id

    @oid_open_id.setter
    def oid_open_id(self, value):
        self._oid_open_id = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.oid_open_id:
            if hasattr(self.oid_open_id, 'to_alipay_dict'):
                params['oid_open_id'] = self.oid_open_id.to_alipay_dict()
            else:
                params['oid_open_id'] = self.oid_open_id
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
        o = TestDemoWzw()
        if 'oid_open_id' in d:
            o.oid_open_id = d['oid_open_id']
        if 'uid' in d:
            o.uid = d['uid']
        return o


