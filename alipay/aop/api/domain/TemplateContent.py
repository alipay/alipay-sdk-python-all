#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateContent(object):

    def __init__(self):
        self._annotation = None
        self._tpl_code = None
        self._tpl_data = None

    @property
    def annotation(self):
        return self._annotation

    @annotation.setter
    def annotation(self, value):
        self._annotation = value
    @property
    def tpl_code(self):
        return self._tpl_code

    @tpl_code.setter
    def tpl_code(self, value):
        self._tpl_code = value
    @property
    def tpl_data(self):
        return self._tpl_data

    @tpl_data.setter
    def tpl_data(self, value):
        self._tpl_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.annotation:
            if hasattr(self.annotation, 'to_alipay_dict'):
                params['annotation'] = self.annotation.to_alipay_dict()
            else:
                params['annotation'] = self.annotation
        if self.tpl_code:
            if hasattr(self.tpl_code, 'to_alipay_dict'):
                params['tpl_code'] = self.tpl_code.to_alipay_dict()
            else:
                params['tpl_code'] = self.tpl_code
        if self.tpl_data:
            if hasattr(self.tpl_data, 'to_alipay_dict'):
                params['tpl_data'] = self.tpl_data.to_alipay_dict()
            else:
                params['tpl_data'] = self.tpl_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateContent()
        if 'annotation' in d:
            o.annotation = d['annotation']
        if 'tpl_code' in d:
            o.tpl_code = d['tpl_code']
        if 'tpl_data' in d:
            o.tpl_data = d['tpl_data']
        return o


