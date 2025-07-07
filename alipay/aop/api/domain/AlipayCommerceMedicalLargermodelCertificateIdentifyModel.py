#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalLargermodelCertificateIdentifyModel(object):

    def __init__(self):
        self._cert_type = None
        self._image_content = None
        self._image_url = None

    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def image_content(self):
        return self._image_content

    @image_content.setter
    def image_content(self, value):
        self._image_content = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.image_content:
            if hasattr(self.image_content, 'to_alipay_dict'):
                params['image_content'] = self.image_content.to_alipay_dict()
            else:
                params['image_content'] = self.image_content
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalLargermodelCertificateIdentifyModel()
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'image_content' in d:
            o.image_content = d['image_content']
        if 'image_url' in d:
            o.image_url = d['image_url']
        return o


