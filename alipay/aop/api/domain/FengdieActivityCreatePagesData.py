#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdieActivityComponentModel import FengdieActivityComponentModel
from alipay.aop.api.domain.FengdieActivitySchemaModel import FengdieActivitySchemaModel


class FengdieActivityCreatePagesData(object):

    def __init__(self):
        self._components = None
        self._page_data = None
        self._page_path = None
        self._title = None

    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        if isinstance(value, list):
            self._components = list()
            for i in value:
                if isinstance(i, FengdieActivityComponentModel):
                    self._components.append(i)
                else:
                    self._components.append(FengdieActivityComponentModel.from_alipay_dict(i))
    @property
    def page_data(self):
        return self._page_data

    @page_data.setter
    def page_data(self, value):
        if isinstance(value, list):
            self._page_data = list()
            for i in value:
                if isinstance(i, FengdieActivitySchemaModel):
                    self._page_data.append(i)
                else:
                    self._page_data.append(FengdieActivitySchemaModel.from_alipay_dict(i))
    @property
    def page_path(self):
        return self._page_path

    @page_path.setter
    def page_path(self, value):
        self._page_path = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.components:
            if isinstance(self.components, list):
                for i in range(0, len(self.components)):
                    element = self.components[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.components[i] = element.to_alipay_dict()
            if hasattr(self.components, 'to_alipay_dict'):
                params['components'] = self.components.to_alipay_dict()
            else:
                params['components'] = self.components
        if self.page_data:
            if isinstance(self.page_data, list):
                for i in range(0, len(self.page_data)):
                    element = self.page_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.page_data[i] = element.to_alipay_dict()
            if hasattr(self.page_data, 'to_alipay_dict'):
                params['page_data'] = self.page_data.to_alipay_dict()
            else:
                params['page_data'] = self.page_data
        if self.page_path:
            if hasattr(self.page_path, 'to_alipay_dict'):
                params['page_path'] = self.page_path.to_alipay_dict()
            else:
                params['page_path'] = self.page_path
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
        o = FengdieActivityCreatePagesData()
        if 'components' in d:
            o.components = d['components']
        if 'page_data' in d:
            o.page_data = d['page_data']
        if 'page_path' in d:
            o.page_path = d['page_path']
        if 'title' in d:
            o.title = d['title']
        return o


