#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgreementSignInfoDTO(object):

    def __init__(self):
        self._sign_notify_url = None
        self._sign_return_url = None

    @property
    def sign_notify_url(self):
        return self._sign_notify_url

    @sign_notify_url.setter
    def sign_notify_url(self, value):
        self._sign_notify_url = value
    @property
    def sign_return_url(self):
        return self._sign_return_url

    @sign_return_url.setter
    def sign_return_url(self, value):
        self._sign_return_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.sign_notify_url:
            if hasattr(self.sign_notify_url, 'to_alipay_dict'):
                params['sign_notify_url'] = self.sign_notify_url.to_alipay_dict()
            else:
                params['sign_notify_url'] = self.sign_notify_url
        if self.sign_return_url:
            if hasattr(self.sign_return_url, 'to_alipay_dict'):
                params['sign_return_url'] = self.sign_return_url.to_alipay_dict()
            else:
                params['sign_return_url'] = self.sign_return_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgreementSignInfoDTO()
        if 'sign_notify_url' in d:
            o.sign_notify_url = d['sign_notify_url']
        if 'sign_return_url' in d:
            o.sign_return_url = d['sign_return_url']
        return o


