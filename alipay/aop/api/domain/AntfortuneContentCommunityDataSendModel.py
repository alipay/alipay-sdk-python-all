#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneContentCommunityDataSendModel(object):

    def __init__(self):
        self._content = None
        self._source_id = None
        self._soure_type = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def soure_type(self):
        return self._soure_type

    @soure_type.setter
    def soure_type(self, value):
        self._soure_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.soure_type:
            if hasattr(self.soure_type, 'to_alipay_dict'):
                params['soure_type'] = self.soure_type.to_alipay_dict()
            else:
                params['soure_type'] = self.soure_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneContentCommunityDataSendModel()
        if 'content' in d:
            o.content = d['content']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'soure_type' in d:
            o.soure_type = d['soure_type']
        return o


