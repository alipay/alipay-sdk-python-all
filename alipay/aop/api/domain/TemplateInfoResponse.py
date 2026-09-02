#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateInfoResponse(object):

    def __init__(self):
        self._scenario_description = None
        self._template_id = None
        self._template_name = None

    @property
    def scenario_description(self):
        return self._scenario_description

    @scenario_description.setter
    def scenario_description(self, value):
        self._scenario_description = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.scenario_description:
            if hasattr(self.scenario_description, 'to_alipay_dict'):
                params['scenario_description'] = self.scenario_description.to_alipay_dict()
            else:
                params['scenario_description'] = self.scenario_description
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateInfoResponse()
        if 'scenario_description' in d:
            o.scenario_description = d['scenario_description']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_name' in d:
            o.template_name = d['template_name']
        return o


