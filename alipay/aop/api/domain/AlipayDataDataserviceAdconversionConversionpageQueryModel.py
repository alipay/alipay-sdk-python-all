#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdconversionConversionpageQueryModel(object):

    def __init__(self):
        self._current = None
        self._page_size = None
        self._principal_tag = None

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.current:
            if hasattr(self.current, 'to_alipay_dict'):
                params['current'] = self.current.to_alipay_dict()
            else:
                params['current'] = self.current
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdconversionConversionpageQueryModel()
        if 'current' in d:
            o.current = d['current']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        return o


