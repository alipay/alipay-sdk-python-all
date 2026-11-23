#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RedirectUrls import RedirectUrls
from alipay.aop.api.domain.VerifyOrderInfo import VerifyOrderInfo


class AlipayCommerceEducateVerifyConsultModel(object):

    def __init__(self):
        self._redirect_urls = None
        self._verify_info = None
        self._verify_request_id = None

    @property
    def redirect_urls(self):
        return self._redirect_urls

    @redirect_urls.setter
    def redirect_urls(self, value):
        if isinstance(value, list):
            self._redirect_urls = list()
            for i in value:
                if isinstance(i, RedirectUrls):
                    self._redirect_urls.append(i)
                else:
                    self._redirect_urls.append(RedirectUrls.from_alipay_dict(i))
    @property
    def verify_info(self):
        return self._verify_info

    @verify_info.setter
    def verify_info(self, value):
        if isinstance(value, VerifyOrderInfo):
            self._verify_info = value
        else:
            self._verify_info = VerifyOrderInfo.from_alipay_dict(value)
    @property
    def verify_request_id(self):
        return self._verify_request_id

    @verify_request_id.setter
    def verify_request_id(self, value):
        self._verify_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.redirect_urls:
            if isinstance(self.redirect_urls, list):
                for i in range(0, len(self.redirect_urls)):
                    element = self.redirect_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.redirect_urls[i] = element.to_alipay_dict()
            if hasattr(self.redirect_urls, 'to_alipay_dict'):
                params['redirect_urls'] = self.redirect_urls.to_alipay_dict()
            else:
                params['redirect_urls'] = self.redirect_urls
        if self.verify_info:
            if hasattr(self.verify_info, 'to_alipay_dict'):
                params['verify_info'] = self.verify_info.to_alipay_dict()
            else:
                params['verify_info'] = self.verify_info
        if self.verify_request_id:
            if hasattr(self.verify_request_id, 'to_alipay_dict'):
                params['verify_request_id'] = self.verify_request_id.to_alipay_dict()
            else:
                params['verify_request_id'] = self.verify_request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateVerifyConsultModel()
        if 'redirect_urls' in d:
            o.redirect_urls = d['redirect_urls']
        if 'verify_info' in d:
            o.verify_info = d['verify_info']
        if 'verify_request_id' in d:
            o.verify_request_id = d['verify_request_id']
        return o


