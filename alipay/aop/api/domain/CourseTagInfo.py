#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CourseTagInfo(object):

    def __init__(self):
        self._tag_code = None

    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CourseTagInfo()
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        return o


