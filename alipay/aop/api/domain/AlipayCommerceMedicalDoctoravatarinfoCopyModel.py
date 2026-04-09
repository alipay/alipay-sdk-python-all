#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalDoctoravatarinfoCopyModel(object):

    def __init__(self):
        self._avatar_id = None
        self._url = None

    @property
    def avatar_id(self):
        return self._avatar_id

    @avatar_id.setter
    def avatar_id(self, value):
        self._avatar_id = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar_id:
            if hasattr(self.avatar_id, 'to_alipay_dict'):
                params['avatar_id'] = self.avatar_id.to_alipay_dict()
            else:
                params['avatar_id'] = self.avatar_id
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
        o = AlipayCommerceMedicalDoctoravatarinfoCopyModel()
        if 'avatar_id' in d:
            o.avatar_id = d['avatar_id']
        if 'url' in d:
            o.url = d['url']
        return o


