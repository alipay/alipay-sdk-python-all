#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoContentBizVO(object):

    def __init__(self):
        self._content = None
        self._meta_id = None
        self._type = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def meta_id(self):
        return self._meta_id

    @meta_id.setter
    def meta_id(self, value):
        self._meta_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.meta_id:
            if hasattr(self.meta_id, 'to_alipay_dict'):
                params['meta_id'] = self.meta_id.to_alipay_dict()
            else:
                params['meta_id'] = self.meta_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoContentBizVO()
        if 'content' in d:
            o.content = d['content']
        if 'meta_id' in d:
            o.meta_id = d['meta_id']
        if 'type' in d:
            o.type = d['type']
        return o


