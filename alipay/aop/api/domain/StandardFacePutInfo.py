#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StandardFacePutInfo(object):

    def __init__(self):
        self._error_code = None
        self._face_id = None
        self._result = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.face_id:
            if hasattr(self.face_id, 'to_alipay_dict'):
                params['face_id'] = self.face_id.to_alipay_dict()
            else:
                params['face_id'] = self.face_id
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StandardFacePutInfo()
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'face_id' in d:
            o.face_id = d['face_id']
        if 'result' in d:
            o.result = d['result']
        return o


