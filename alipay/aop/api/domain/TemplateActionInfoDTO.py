#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateActionMiniAppUrlDTO import TemplateActionMiniAppUrlDTO


class TemplateActionInfoDTO(object):

    def __init__(self):
        self._code = None
        self._mini_app_url = None
        self._text = None
        self._url = None
        self._url_type = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def mini_app_url(self):
        return self._mini_app_url

    @mini_app_url.setter
    def mini_app_url(self, value):
        if isinstance(value, TemplateActionMiniAppUrlDTO):
            self._mini_app_url = value
        else:
            self._mini_app_url = TemplateActionMiniAppUrlDTO.from_alipay_dict(value)
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def url_type(self):
        return self._url_type

    @url_type.setter
    def url_type(self, value):
        self._url_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.mini_app_url:
            if hasattr(self.mini_app_url, 'to_alipay_dict'):
                params['mini_app_url'] = self.mini_app_url.to_alipay_dict()
            else:
                params['mini_app_url'] = self.mini_app_url
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
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
        o = TemplateActionInfoDTO()
        if 'code' in d:
            o.code = d['code']
        if 'mini_app_url' in d:
            o.mini_app_url = d['mini_app_url']
        if 'text' in d:
            o.text = d['text']
        if 'url' in d:
            o.url = d['url']
        if 'url_type' in d:
            o.url_type = d['url_type']
        return o


