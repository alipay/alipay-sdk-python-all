#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertifyImgUploadModel(object):

    def __init__(self):
        self._biz_from = None
        self._biz_id = None
        self._cert_type = None
        self._content = None
        self._image_type = None
        self._storage_type = None

    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def image_type(self):
        return self._image_type

    @image_type.setter
    def image_type(self, value):
        self._image_type = value
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
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.image_type:
            if hasattr(self.image_type, 'to_alipay_dict'):
                params['image_type'] = self.image_type.to_alipay_dict()
            else:
                params['image_type'] = self.image_type
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
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'content' in d:
            o.content = d['content']
        if 'image_type' in d:
            o.image_type = d['image_type']
        if 'storage_type' in d:
            o.storage_type = d['storage_type']
        return o


