#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateRightsContentDTO(object):

    def __init__(self):
        self._detail = None
        self._logo_id = None
        self._title = None

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def logo_id(self):
        return self._logo_id

    @logo_id.setter
    def logo_id(self, value):
        self._logo_id = value
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
        if self.logo_id:
            if hasattr(self.logo_id, 'to_alipay_dict'):
                params['logo_id'] = self.logo_id.to_alipay_dict()
            else:
                params['logo_id'] = self.logo_id
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
        if 'logo_id' in d:
            o.logo_id = d['logo_id']
        if 'title' in d:
            o.title = d['title']
        return o


