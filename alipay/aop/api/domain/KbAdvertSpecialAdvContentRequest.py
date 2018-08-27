#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertContentPasswordModify import KbAdvertContentPasswordModify


class KbAdvertSpecialAdvContentRequest(object):

    def __init__(self):
        self._content_password_modify = None
        self._content_type = None

    @property
    def content_password_modify(self):
        return self._content_password_modify

    @content_password_modify.setter
    def content_password_modify(self, value):
        if isinstance(value, KbAdvertContentPasswordModify):
            self._content_password_modify = value
        else:
            self._content_password_modify = KbAdvertContentPasswordModify.from_alipay_dict(value)
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_password_modify:
            if hasattr(self.content_password_modify, 'to_alipay_dict'):
                params['content_password_modify'] = self.content_password_modify.to_alipay_dict()
            else:
                params['content_password_modify'] = self.content_password_modify
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertSpecialAdvContentRequest()
        if 'content_password_modify' in d:
            o.content_password_modify = d['content_password_modify']
        if 'content_type' in d:
            o.content_type = d['content_type']
        return o


