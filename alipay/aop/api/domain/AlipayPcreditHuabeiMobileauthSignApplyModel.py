#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiMobileauthSignApplyModel(object):

    def __init__(self):
        self._request = None

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, value):
        self._request = value


    def to_alipay_dict(self):
        params = dict()
        if self.request:
            if hasattr(self.request, 'to_alipay_dict'):
                params['request'] = self.request.to_alipay_dict()
            else:
                params['request'] = self.request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiMobileauthSignApplyModel()
        if 'request' in d:
            o.request = d['request']
        return o


