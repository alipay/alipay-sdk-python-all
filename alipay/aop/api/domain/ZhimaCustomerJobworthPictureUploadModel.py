#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerJobworthPictureUploadModel(object):

    def __init__(self):
        self._content = None
        self._pic_type = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def pic_type(self):
        return self._pic_type

    @pic_type.setter
    def pic_type(self, value):
        self._pic_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.pic_type:
            if hasattr(self.pic_type, 'to_alipay_dict'):
                params['pic_type'] = self.pic_type.to_alipay_dict()
            else:
                params['pic_type'] = self.pic_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerJobworthPictureUploadModel()
        if 'content' in d:
            o.content = d['content']
        if 'pic_type' in d:
            o.pic_type = d['pic_type']
        return o


