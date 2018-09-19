#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringTablecodeQueryModel(object):

    def __init__(self):
        self._url_context = None

    @property
    def url_context(self):
        return self._url_context

    @url_context.setter
    def url_context(self, value):
        self._url_context = value


    def to_alipay_dict(self):
        params = dict()
        if self.url_context:
            if hasattr(self.url_context, 'to_alipay_dict'):
                params['url_context'] = self.url_context.to_alipay_dict()
            else:
                params['url_context'] = self.url_context
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringTablecodeQueryModel()
        if 'url_context' in d:
            o.url_context = d['url_context']
        return o


