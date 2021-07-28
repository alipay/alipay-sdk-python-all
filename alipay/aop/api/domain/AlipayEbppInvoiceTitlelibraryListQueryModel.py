#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceTitlelibraryListQueryModel(object):

    def __init__(self):
        self._title_simple_name = None

    @property
    def title_simple_name(self):
        return self._title_simple_name

    @title_simple_name.setter
    def title_simple_name(self, value):
        self._title_simple_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.title_simple_name:
            if hasattr(self.title_simple_name, 'to_alipay_dict'):
                params['title_simple_name'] = self.title_simple_name.to_alipay_dict()
            else:
                params['title_simple_name'] = self.title_simple_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceTitlelibraryListQueryModel()
        if 'title_simple_name' in d:
            o.title_simple_name = d['title_simple_name']
        return o


