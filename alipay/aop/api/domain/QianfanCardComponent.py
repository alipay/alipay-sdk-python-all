#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QianfanCardComponent(object):

    def __init__(self):
        self._param_mapping = None
        self._post_guide = None
        self._pre_guide = None
        self._template_content = None

    @property
    def param_mapping(self):
        return self._param_mapping

    @param_mapping.setter
    def param_mapping(self, value):
        self._param_mapping = value
    @property
    def post_guide(self):
        return self._post_guide

    @post_guide.setter
    def post_guide(self, value):
        self._post_guide = value
    @property
    def pre_guide(self):
        return self._pre_guide

    @pre_guide.setter
    def pre_guide(self, value):
        self._pre_guide = value
    @property
    def template_content(self):
        return self._template_content

    @template_content.setter
    def template_content(self, value):
        self._template_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.param_mapping:
            if hasattr(self.param_mapping, 'to_alipay_dict'):
                params['param_mapping'] = self.param_mapping.to_alipay_dict()
            else:
                params['param_mapping'] = self.param_mapping
        if self.post_guide:
            if hasattr(self.post_guide, 'to_alipay_dict'):
                params['post_guide'] = self.post_guide.to_alipay_dict()
            else:
                params['post_guide'] = self.post_guide
        if self.pre_guide:
            if hasattr(self.pre_guide, 'to_alipay_dict'):
                params['pre_guide'] = self.pre_guide.to_alipay_dict()
            else:
                params['pre_guide'] = self.pre_guide
        if self.template_content:
            if hasattr(self.template_content, 'to_alipay_dict'):
                params['template_content'] = self.template_content.to_alipay_dict()
            else:
                params['template_content'] = self.template_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QianfanCardComponent()
        if 'param_mapping' in d:
            o.param_mapping = d['param_mapping']
        if 'post_guide' in d:
            o.post_guide = d['post_guide']
        if 'pre_guide' in d:
            o.pre_guide = d['pre_guide']
        if 'template_content' in d:
            o.template_content = d['template_content']
        return o


