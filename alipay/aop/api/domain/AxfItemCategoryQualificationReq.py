#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AxfItemCategoryQualificationReq(object):

    def __init__(self):
        self._qualification_content = None
        self._qualification_type = None

    @property
    def qualification_content(self):
        return self._qualification_content

    @qualification_content.setter
    def qualification_content(self, value):
        self._qualification_content = value
    @property
    def qualification_type(self):
        return self._qualification_type

    @qualification_type.setter
    def qualification_type(self, value):
        self._qualification_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.qualification_content:
            if hasattr(self.qualification_content, 'to_alipay_dict'):
                params['qualification_content'] = self.qualification_content.to_alipay_dict()
            else:
                params['qualification_content'] = self.qualification_content
        if self.qualification_type:
            if hasattr(self.qualification_type, 'to_alipay_dict'):
                params['qualification_type'] = self.qualification_type.to_alipay_dict()
            else:
                params['qualification_type'] = self.qualification_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AxfItemCategoryQualificationReq()
        if 'qualification_content' in d:
            o.qualification_content = d['qualification_content']
        if 'qualification_type' in d:
            o.qualification_type = d['qualification_type']
        return o


