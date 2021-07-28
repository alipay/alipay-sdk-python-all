#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CampusCardPicture(object):

    def __init__(self):
        self._picture_type = None
        self._url = None

    @property
    def picture_type(self):
        return self._picture_type

    @picture_type.setter
    def picture_type(self, value):
        self._picture_type = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.picture_type:
            if hasattr(self.picture_type, 'to_alipay_dict'):
                params['picture_type'] = self.picture_type.to_alipay_dict()
            else:
                params['picture_type'] = self.picture_type
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
        o = CampusCardPicture()
        if 'picture_type' in d:
            o.picture_type = d['picture_type']
        if 'url' in d:
            o.url = d['url']
        return o


