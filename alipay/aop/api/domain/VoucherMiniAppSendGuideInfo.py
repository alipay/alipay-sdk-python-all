#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherMiniAppSendGuideInfo(object):

    def __init__(self):
        self._mini_app_url = None

    @property
    def mini_app_url(self):
        return self._mini_app_url

    @mini_app_url.setter
    def mini_app_url(self, value):
        self._mini_app_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.mini_app_url:
            if hasattr(self.mini_app_url, 'to_alipay_dict'):
                params['mini_app_url'] = self.mini_app_url.to_alipay_dict()
            else:
                params['mini_app_url'] = self.mini_app_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherMiniAppSendGuideInfo()
        if 'mini_app_url' in d:
            o.mini_app_url = d['mini_app_url']
        return o


