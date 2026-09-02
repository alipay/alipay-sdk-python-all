#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YpzOfflineQrCodeCardOne(object):

    def __init__(self):
        self._image_url = None
        self._redirect_url = None

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YpzOfflineQrCodeCardOne()
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        return o


