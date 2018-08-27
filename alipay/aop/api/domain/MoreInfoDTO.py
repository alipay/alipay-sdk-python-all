#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MoreInfoDTO(object):

    def __init__(self):
        self._descs = None
        self._params = None
        self._title = None
        self._url = None

    @property
    def descs(self):
        return self._descs

    @descs.setter
    def descs(self, value):
        if isinstance(value, list):
            self._descs = list()
            for i in value:
                self._descs.append(i)
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.descs:
            if isinstance(self.descs, list):
                for i in range(0, len(self.descs)):
                    element = self.descs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.descs[i] = element.to_alipay_dict()
            if hasattr(self.descs, 'to_alipay_dict'):
                params['descs'] = self.descs.to_alipay_dict()
            else:
                params['descs'] = self.descs
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MoreInfoDTO()
        if 'descs' in d:
            o.descs = d['descs']
        if 'params' in d:
            o.params = d['params']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


