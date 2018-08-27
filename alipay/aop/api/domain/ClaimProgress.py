#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClaimProgress(object):

    def __init__(self):
        self._update_content = None
        self._update_time = None

    @property
    def update_content(self):
        return self._update_content

    @update_content.setter
    def update_content(self, value):
        self._update_content = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.update_content:
            if hasattr(self.update_content, 'to_alipay_dict'):
                params['update_content'] = self.update_content.to_alipay_dict()
            else:
                params['update_content'] = self.update_content
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClaimProgress()
        if 'update_content' in d:
            o.update_content = d['update_content']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


