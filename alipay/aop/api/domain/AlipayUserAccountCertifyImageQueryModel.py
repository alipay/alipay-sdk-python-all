#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountCertifyImageQueryModel(object):

    def __init__(self):
        self._picture_url = None

    @property
    def picture_url(self):
        return self._picture_url

    @picture_url.setter
    def picture_url(self, value):
        if isinstance(value, list):
            self._picture_url = list()
            for i in value:
                self._picture_url.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.picture_url:
            if isinstance(self.picture_url, list):
                for i in range(0, len(self.picture_url)):
                    element = self.picture_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.picture_url[i] = element.to_alipay_dict()
            if hasattr(self.picture_url, 'to_alipay_dict'):
                params['picture_url'] = self.picture_url.to_alipay_dict()
            else:
                params['picture_url'] = self.picture_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAccountCertifyImageQueryModel()
        if 'picture_url' in d:
            o.picture_url = d['picture_url']
        return o


