#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryObArtifactListRequest(object):

    def __init__(self):
        self._use_type_str = None
        self._version_tag_str = None

    @property
    def use_type_str(self):
        return self._use_type_str

    @use_type_str.setter
    def use_type_str(self, value):
        self._use_type_str = value
    @property
    def version_tag_str(self):
        return self._version_tag_str

    @version_tag_str.setter
    def version_tag_str(self, value):
        self._version_tag_str = value


    def to_alipay_dict(self):
        params = dict()
        if self.use_type_str:
            if hasattr(self.use_type_str, 'to_alipay_dict'):
                params['use_type_str'] = self.use_type_str.to_alipay_dict()
            else:
                params['use_type_str'] = self.use_type_str
        if self.version_tag_str:
            if hasattr(self.version_tag_str, 'to_alipay_dict'):
                params['version_tag_str'] = self.version_tag_str.to_alipay_dict()
            else:
                params['version_tag_str'] = self.version_tag_str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryObArtifactListRequest()
        if 'use_type_str' in d:
            o.use_type_str = d['use_type_str']
        if 'version_tag_str' in d:
            o.version_tag_str = d['version_tag_str']
        return o


