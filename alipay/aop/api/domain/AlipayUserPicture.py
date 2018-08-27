#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserPicture(object):

    def __init__(self):
        self._picture_type = None
        self._picture_url = None

    @property
    def picture_type(self):
        return self._picture_type

    @picture_type.setter
    def picture_type(self, value):
        self._picture_type = value
    @property
    def picture_url(self):
        return self._picture_url

    @picture_url.setter
    def picture_url(self, value):
        self._picture_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.picture_type:
            if hasattr(self.picture_type, 'to_alipay_dict'):
                params['picture_type'] = self.picture_type.to_alipay_dict()
            else:
                params['picture_type'] = self.picture_type
        if self.picture_url:
            if hasattr(self.picture_url, 'to_alipay_dict'):
                params['picture_url'] = self.picture_url.to_alipay_dict()
            else:
                params['picture_url'] = self.picture_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserPicture()
        if 'picture_type' in d:
            o.picture_type = d['picture_type']
        if 'picture_url' in d:
            o.picture_url = d['picture_url']
        return o


