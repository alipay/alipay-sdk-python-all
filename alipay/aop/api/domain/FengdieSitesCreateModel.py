#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdieActivityCreatePageData import FengdieActivityCreatePageData
from alipay.aop.api.domain.FengdieActivityCreatePagesData import FengdieActivityCreatePagesData


class FengdieSitesCreateModel(object):

    def __init__(self):
        self._domain = None
        self._name = None
        self._offline_time = None
        self._page = None
        self._pages = None
        self._title = None

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value
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
        if isinstance(value, FengdieActivityCreatePageData):
            self._page = value
        else:
            self._page = FengdieActivityCreatePageData.from_alipay_dict(value)
    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, list):
            self._pages = list()
            for i in value:
                if isinstance(i, FengdieActivityCreatePagesData):
                    self._pages.append(i)
                else:
                    self._pages.append(FengdieActivityCreatePagesData.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.domain:
            if hasattr(self.domain, 'to_alipay_dict'):
                params['domain'] = self.domain.to_alipay_dict()
            else:
                params['domain'] = self.domain
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
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.pages:
            if isinstance(self.pages, list):
                for i in range(0, len(self.pages)):
                    element = self.pages[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pages[i] = element.to_alipay_dict()
            if hasattr(self.pages, 'to_alipay_dict'):
                params['pages'] = self.pages.to_alipay_dict()
            else:
                params['pages'] = self.pages
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
        o = FengdieSitesCreateModel()
        if 'domain' in d:
            o.domain = d['domain']
        if 'name' in d:
            o.name = d['name']
        if 'offline_time' in d:
            o.offline_time = d['offline_time']
        if 'page' in d:
            o.page = d['page']
        if 'pages' in d:
            o.pages = d['pages']
        if 'title' in d:
            o.title = d['title']
        return o


