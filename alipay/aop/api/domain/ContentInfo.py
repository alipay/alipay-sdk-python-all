#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentDetail import ContentDetail


class ContentInfo(object):

    def __init__(self):
        self._content_details = None

    @property
    def content_details(self):
        return self._content_details

    @content_details.setter
    def content_details(self, value):
        if isinstance(value, list):
            self._content_details = list()
            for i in value:
                if isinstance(i, ContentDetail):
                    self._content_details.append(i)
                else:
                    self._content_details.append(ContentDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.content_details:
            if isinstance(self.content_details, list):
                for i in range(0, len(self.content_details)):
                    element = self.content_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_details[i] = element.to_alipay_dict()
            if hasattr(self.content_details, 'to_alipay_dict'):
                params['content_details'] = self.content_details.to_alipay_dict()
            else:
                params['content_details'] = self.content_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentInfo()
        if 'content_details' in d:
            o.content_details = d['content_details']
        return o


