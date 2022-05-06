#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSceneConfigQueryModel(object):

    def __init__(self):
        self._school_id = None
        self._school_std_code = None

    @property
    def school_id(self):
        return self._school_id

    @school_id.setter
    def school_id(self, value):
        self._school_id = value
    @property
    def school_std_code(self):
        return self._school_std_code

    @school_std_code.setter
    def school_std_code(self, value):
        self._school_std_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.school_id:
            if hasattr(self.school_id, 'to_alipay_dict'):
                params['school_id'] = self.school_id.to_alipay_dict()
            else:
                params['school_id'] = self.school_id
        if self.school_std_code:
            if hasattr(self.school_std_code, 'to_alipay_dict'):
                params['school_std_code'] = self.school_std_code.to_alipay_dict()
            else:
                params['school_std_code'] = self.school_std_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSceneConfigQueryModel()
        if 'school_id' in d:
            o.school_id = d['school_id']
        if 'school_std_code' in d:
            o.school_std_code = d['school_std_code']
        return o


