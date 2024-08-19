#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitQueryContent import BenefitQueryContent


class BenefitQueryResponseComponent(object):

    def __init__(self):
        self._content = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, BenefitQueryContent):
            self._content = value
        else:
            self._content = BenefitQueryContent.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitQueryResponseComponent()
        if 'content' in d:
            o.content = d['content']
        return o


