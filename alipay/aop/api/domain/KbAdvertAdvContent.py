#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertAdvContent(object):

    def __init__(self):
        self._codec = None
        self._link_url = None

    @property
    def codec(self):
        return self._codec

    @codec.setter
    def codec(self, value):
        self._codec = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.codec:
            if hasattr(self.codec, 'to_alipay_dict'):
                params['codec'] = self.codec.to_alipay_dict()
            else:
                params['codec'] = self.codec
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertAdvContent()
        if 'codec' in d:
            o.codec = d['codec']
        if 'link_url' in d:
            o.link_url = d['link_url']
        return o


