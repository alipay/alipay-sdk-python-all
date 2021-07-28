#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateSecondaryOperationDTO(object):

    def __init__(self):
        self._need_write_off = None
        self._title = None
        self._url = None

    @property
    def need_write_off(self):
        return self._need_write_off

    @need_write_off.setter
    def need_write_off(self, value):
        self._need_write_off = value
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
        if self.need_write_off:
            if hasattr(self.need_write_off, 'to_alipay_dict'):
                params['need_write_off'] = self.need_write_off.to_alipay_dict()
            else:
                params['need_write_off'] = self.need_write_off
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
        o = TemplateSecondaryOperationDTO()
        if 'need_write_off' in d:
            o.need_write_off = d['need_write_off']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


