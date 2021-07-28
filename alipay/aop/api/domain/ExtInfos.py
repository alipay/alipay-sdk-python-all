#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtInfos(object):

    def __init__(self):
        self._req_from_page = None

    @property
    def req_from_page(self):
        return self._req_from_page

    @req_from_page.setter
    def req_from_page(self, value):
        self._req_from_page = value


    def to_alipay_dict(self):
        params = dict()
        if self.req_from_page:
            if hasattr(self.req_from_page, 'to_alipay_dict'):
                params['req_from_page'] = self.req_from_page.to_alipay_dict()
            else:
                params['req_from_page'] = self.req_from_page
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtInfos()
        if 'req_from_page' in d:
            o.req_from_page = d['req_from_page']
        return o


