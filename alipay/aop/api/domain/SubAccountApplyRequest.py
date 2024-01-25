#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubAccountApplyRequest(object):

    def __init__(self):
        self._ou_code = None
        self._source_uid = None

    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def source_uid(self):
        return self._source_uid

    @source_uid.setter
    def source_uid(self, value):
        self._source_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        if self.source_uid:
            if hasattr(self.source_uid, 'to_alipay_dict'):
                params['source_uid'] = self.source_uid.to_alipay_dict()
            else:
                params['source_uid'] = self.source_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubAccountApplyRequest()
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'source_uid' in d:
            o.source_uid = d['source_uid']
        return o


