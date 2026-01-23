#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OcrAttachmentRes(object):

    def __init__(self):
        self._aq_id = None
        self._aq_type = None
        self._aq_url = None
        self._id = None
        self._ocr_res = None
        self._type = None
        self._url = None

    @property
    def aq_id(self):
        return self._aq_id

    @aq_id.setter
    def aq_id(self, value):
        self._aq_id = value
    @property
    def aq_type(self):
        return self._aq_type

    @aq_type.setter
    def aq_type(self, value):
        self._aq_type = value
    @property
    def aq_url(self):
        return self._aq_url

    @aq_url.setter
    def aq_url(self, value):
        self._aq_url = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def ocr_res(self):
        return self._ocr_res

    @ocr_res.setter
    def ocr_res(self, value):
        self._ocr_res = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.aq_id:
            if hasattr(self.aq_id, 'to_alipay_dict'):
                params['aq_id'] = self.aq_id.to_alipay_dict()
            else:
                params['aq_id'] = self.aq_id
        if self.aq_type:
            if hasattr(self.aq_type, 'to_alipay_dict'):
                params['aq_type'] = self.aq_type.to_alipay_dict()
            else:
                params['aq_type'] = self.aq_type
        if self.aq_url:
            if hasattr(self.aq_url, 'to_alipay_dict'):
                params['aq_url'] = self.aq_url.to_alipay_dict()
            else:
                params['aq_url'] = self.aq_url
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.ocr_res:
            if hasattr(self.ocr_res, 'to_alipay_dict'):
                params['ocr_res'] = self.ocr_res.to_alipay_dict()
            else:
                params['ocr_res'] = self.ocr_res
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OcrAttachmentRes()
        if 'aq_id' in d:
            o.aq_id = d['aq_id']
        if 'aq_type' in d:
            o.aq_type = d['aq_type']
        if 'aq_url' in d:
            o.aq_url = d['aq_url']
        if 'id' in d:
            o.id = d['id']
        if 'ocr_res' in d:
            o.ocr_res = d['ocr_res']
        if 'type' in d:
            o.type = d['type']
        if 'url' in d:
            o.url = d['url']
        return o


