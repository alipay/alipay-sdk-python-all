#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccessSceneUrl(object):

    def __init__(self):
        self._access_url = None
        self._scheme_url = None
        self._text = None

    @property
    def access_url(self):
        return self._access_url

    @access_url.setter
    def access_url(self, value):
        self._access_url = value
    @property
    def scheme_url(self):
        return self._scheme_url

    @scheme_url.setter
    def scheme_url(self, value):
        self._scheme_url = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_url:
            if hasattr(self.access_url, 'to_alipay_dict'):
                params['access_url'] = self.access_url.to_alipay_dict()
            else:
                params['access_url'] = self.access_url
        if self.scheme_url:
            if hasattr(self.scheme_url, 'to_alipay_dict'):
                params['scheme_url'] = self.scheme_url.to_alipay_dict()
            else:
                params['scheme_url'] = self.scheme_url
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessSceneUrl()
        if 'access_url' in d:
            o.access_url = d['access_url']
        if 'scheme_url' in d:
            o.scheme_url = d['scheme_url']
        if 'text' in d:
            o.text = d['text']
        return o


