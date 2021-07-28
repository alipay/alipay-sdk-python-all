#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FillContent import FillContent
from alipay.aop.api.domain.SignFieldBean import SignFieldBean


class TemplateInfoBean(object):

    def __init__(self):
        self._fill_contents = None
        self._name = None
        self._signfields = None
        self._template_id = None

    @property
    def fill_contents(self):
        return self._fill_contents

    @fill_contents.setter
    def fill_contents(self, value):
        if isinstance(value, list):
            self._fill_contents = list()
            for i in value:
                if isinstance(i, FillContent):
                    self._fill_contents.append(i)
                else:
                    self._fill_contents.append(FillContent.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def signfields(self):
        return self._signfields

    @signfields.setter
    def signfields(self, value):
        if isinstance(value, list):
            self._signfields = list()
            for i in value:
                if isinstance(i, SignFieldBean):
                    self._signfields.append(i)
                else:
                    self._signfields.append(SignFieldBean.from_alipay_dict(i))
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fill_contents:
            if isinstance(self.fill_contents, list):
                for i in range(0, len(self.fill_contents)):
                    element = self.fill_contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fill_contents[i] = element.to_alipay_dict()
            if hasattr(self.fill_contents, 'to_alipay_dict'):
                params['fill_contents'] = self.fill_contents.to_alipay_dict()
            else:
                params['fill_contents'] = self.fill_contents
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.signfields:
            if isinstance(self.signfields, list):
                for i in range(0, len(self.signfields)):
                    element = self.signfields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.signfields[i] = element.to_alipay_dict()
            if hasattr(self.signfields, 'to_alipay_dict'):
                params['signfields'] = self.signfields.to_alipay_dict()
            else:
                params['signfields'] = self.signfields
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateInfoBean()
        if 'fill_contents' in d:
            o.fill_contents = d['fill_contents']
        if 'name' in d:
            o.name = d['name']
        if 'signfields' in d:
            o.signfields = d['signfields']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


