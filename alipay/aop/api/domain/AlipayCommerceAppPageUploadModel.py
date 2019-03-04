#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommerceAppUploadRequestContent import CommerceAppUploadRequestContent


class AlipayCommerceAppPageUploadModel(object):

    def __init__(self):
        self._content = None
        self._service_name = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, CommerceAppUploadRequestContent):
            self._content = value
        else:
            self._content = CommerceAppUploadRequestContent.from_alipay_dict(value)
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAppPageUploadModel()
        if 'content' in d:
            o.content = d['content']
        if 'service_name' in d:
            o.service_name = d['service_name']
        return o


