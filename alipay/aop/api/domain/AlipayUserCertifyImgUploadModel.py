#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertifyImgUploadModel(object):

    def __init__(self):
        self._biz_from = None
        self._content = None
        self._storage_type = None

    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def storage_type(self):
        return self._storage_type

    @storage_type.setter
    def storage_type(self, value):
        self._storage_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.storage_type:
            if hasattr(self.storage_type, 'to_alipay_dict'):
                params['storage_type'] = self.storage_type.to_alipay_dict()
            else:
                params['storage_type'] = self.storage_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertifyImgUploadModel()
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'content' in d:
            o.content = d['content']
        if 'storage_type' in d:
            o.storage_type = d['storage_type']
        return o


