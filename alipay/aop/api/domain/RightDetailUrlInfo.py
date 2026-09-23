#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RightDetailUrlInfo(object):

    def __init__(self):
        self._has_right = None
        self._right_detail_url = None

    @property
    def has_right(self):
        return self._has_right

    @has_right.setter
    def has_right(self, value):
        self._has_right = value
    @property
    def right_detail_url(self):
        return self._right_detail_url

    @right_detail_url.setter
    def right_detail_url(self, value):
        self._right_detail_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_right:
            if hasattr(self.has_right, 'to_alipay_dict'):
                params['has_right'] = self.has_right.to_alipay_dict()
            else:
                params['has_right'] = self.has_right
        if self.right_detail_url:
            if hasattr(self.right_detail_url, 'to_alipay_dict'):
                params['right_detail_url'] = self.right_detail_url.to_alipay_dict()
            else:
                params['right_detail_url'] = self.right_detail_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RightDetailUrlInfo()
        if 'has_right' in d:
            o.has_right = d['has_right']
        if 'right_detail_url' in d:
            o.right_detail_url = d['right_detail_url']
        return o


