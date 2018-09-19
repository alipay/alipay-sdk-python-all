#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateMdcodeNotifyConfDTO(object):

    def __init__(self):
        self._ext_params = None
        self._url = None

    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
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
        o = TemplateMdcodeNotifyConfDTO()
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'url' in d:
            o.url = d['url']
        return o


