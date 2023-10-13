#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ErrorPageSetting(object):

    def __init__(self):
        self._error_page_404 = None

    @property
    def error_page_404(self):
        return self._error_page_404

    @error_page_404.setter
    def error_page_404(self, value):
        self._error_page_404 = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_page_404:
            if hasattr(self.error_page_404, 'to_alipay_dict'):
                params['error_page_404'] = self.error_page_404.to_alipay_dict()
            else:
                params['error_page_404'] = self.error_page_404
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ErrorPageSetting()
        if 'error_page_404' in d:
            o.error_page_404 = d['error_page_404']
        return o


