#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertdocUrlQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._cert_doc_type = None
        self._city = None
        self._url_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def cert_doc_type(self):
        return self._cert_doc_type

    @cert_doc_type.setter
    def cert_doc_type(self, value):
        self._cert_doc_type = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def url_type(self):
        return self._url_type

    @url_type.setter
    def url_type(self, value):
        self._url_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cert_doc_type:
            if hasattr(self.cert_doc_type, 'to_alipay_dict'):
                params['cert_doc_type'] = self.cert_doc_type.to_alipay_dict()
            else:
                params['cert_doc_type'] = self.cert_doc_type
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.url_type:
            if hasattr(self.url_type, 'to_alipay_dict'):
                params['url_type'] = self.url_type.to_alipay_dict()
            else:
                params['url_type'] = self.url_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertdocUrlQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cert_doc_type' in d:
            o.cert_doc_type = d['cert_doc_type']
        if 'city' in d:
            o.city = d['city']
        if 'url_type' in d:
            o.url_type = d['url_type']
        return o


