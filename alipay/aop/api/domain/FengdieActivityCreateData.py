#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdieActivityCreatePageData import FengdieActivityCreatePageData


class FengdieActivityCreateData(object):

    def __init__(self):
        self._name = None
        self._offline_time = None
        self._page = None
        self._title = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def offline_time(self):
        return self._offline_time

    @offline_time.setter
    def offline_time(self, value):
        self._offline_time = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        if isinstance(value, list):
            self._page = list()
            for i in value:
                if isinstance(i, FengdieActivityCreatePageData):
                    self._page.append(i)
                else:
                    self._page.append(FengdieActivityCreatePageData.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.offline_time:
            if hasattr(self.offline_time, 'to_alipay_dict'):
                params['offline_time'] = self.offline_time.to_alipay_dict()
            else:
                params['offline_time'] = self.offline_time
        if self.page:
            if isinstance(self.page, list):
                for i in range(0, len(self.page)):
                    element = self.page[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.page[i] = element.to_alipay_dict()
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
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
        o = FengdieActivityCreateData()
        if 'name' in d:
            o.name = d['name']
        if 'offline_time' in d:
            o.offline_time = d['offline_time']
        if 'page' in d:
            o.page = d['page']
        if 'title' in d:
            o.title = d['title']
        return o


