#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ComponentDTO import ComponentDTO


class TemplateComponentListResponse(object):

    def __init__(self):
        self._component = None
        self._template_code = None

    @property
    def component(self):
        return self._component

    @component.setter
    def component(self, value):
        if isinstance(value, list):
            self._component = list()
            for i in value:
                if isinstance(i, ComponentDTO):
                    self._component.append(i)
                else:
                    self._component.append(ComponentDTO.from_alipay_dict(i))
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.component:
            if isinstance(self.component, list):
                for i in range(0, len(self.component)):
                    element = self.component[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.component[i] = element.to_alipay_dict()
            if hasattr(self.component, 'to_alipay_dict'):
                params['component'] = self.component.to_alipay_dict()
            else:
                params['component'] = self.component
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateComponentListResponse()
        if 'component' in d:
            o.component = d['component']
        if 'template_code' in d:
            o.template_code = d['template_code']
        return o


