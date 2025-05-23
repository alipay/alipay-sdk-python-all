#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserPersonPictureDetail(object):

    def __init__(self):
        self._picture_data = None
        self._picture_url = None

    @property
    def picture_data(self):
        return self._picture_data

    @picture_data.setter
    def picture_data(self, value):
        self._picture_data = value
    @property
    def picture_url(self):
        return self._picture_url

    @picture_url.setter
    def picture_url(self, value):
        self._picture_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.picture_data:
            if hasattr(self.picture_data, 'to_alipay_dict'):
                params['picture_data'] = self.picture_data.to_alipay_dict()
            else:
                params['picture_data'] = self.picture_data
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
        o = UserPersonPictureDetail()
        if 'picture_data' in d:
            o.picture_data = d['picture_data']
        if 'picture_url' in d:
            o.picture_url = d['picture_url']
        return o


