#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCreditAutofinanceVidGetModel(object):

    def __init__(self):
        self._orgcode = None
        self._uid = None
        self._version = None

    @property
    def orgcode(self):
        return self._orgcode

    @orgcode.setter
    def orgcode(self, value):
        self._orgcode = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value


    def to_alipay_dict(self):
        params = dict()
        if self.orgcode:
            if hasattr(self.orgcode, 'to_alipay_dict'):
                params['orgcode'] = self.orgcode.to_alipay_dict()
            else:
                params['orgcode'] = self.orgcode
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.version:
            if hasattr(self.version, 'to_alipay_dict'):
                params['version'] = self.version.to_alipay_dict()
            else:
                params['version'] = self.version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCreditAutofinanceVidGetModel()
        if 'orgcode' in d:
            o.orgcode = d['orgcode']
        if 'uid' in d:
            o.uid = d['uid']
        if 'version' in d:
            o.version = d['version']
        return o


