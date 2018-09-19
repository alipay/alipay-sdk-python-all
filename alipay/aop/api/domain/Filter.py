#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LabelContext import LabelContext


class Filter(object):

    def __init__(self):
        self._context = None
        self._template = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        if isinstance(value, LabelContext):
            self._context = value
        else:
            self._context = LabelContext.from_alipay_dict(value)
    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        self._template = value


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.template:
            if hasattr(self.template, 'to_alipay_dict'):
                params['template'] = self.template.to_alipay_dict()
            else:
                params['template'] = self.template
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Filter()
        if 'context' in d:
            o.context = d['context']
        if 'template' in d:
            o.template = d['template']
        return o


