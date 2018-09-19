#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateRightsContentDTO(object):

    def __init__(self):
        self._detail = None
        self._title = None

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail:
            if hasattr(self.detail, 'to_alipay_dict'):
                params['detail'] = self.detail.to_alipay_dict()
            else:
                params['detail'] = self.detail
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateRightsContentDTO()
        if 'detail' in d:
            o.detail = d['detail']
        if 'title' in d:
            o.title = d['title']
        return o


