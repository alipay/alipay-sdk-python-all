#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotMarketingTemplateQueryModel(object):

    def __init__(self):
        self._template_ids = None

    @property
    def template_ids(self):
        return self._template_ids

    @template_ids.setter
    def template_ids(self, value):
        if isinstance(value, list):
            self._template_ids = list()
            for i in value:
                self._template_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.template_ids:
            if isinstance(self.template_ids, list):
                for i in range(0, len(self.template_ids)):
                    element = self.template_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_ids[i] = element.to_alipay_dict()
            if hasattr(self.template_ids, 'to_alipay_dict'):
                params['template_ids'] = self.template_ids.to_alipay_dict()
            else:
                params['template_ids'] = self.template_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotMarketingTemplateQueryModel()
        if 'template_ids' in d:
            o.template_ids = d['template_ids']
        return o


