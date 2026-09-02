#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeAcpShortenurlQueryModel(object):

    def __init__(self):
        self._schema_url = None

    @property
    def schema_url(self):
        return self._schema_url

    @schema_url.setter
    def schema_url(self, value):
        self._schema_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.schema_url:
            if hasattr(self.schema_url, 'to_alipay_dict'):
                params['schema_url'] = self.schema_url.to_alipay_dict()
            else:
                params['schema_url'] = self.schema_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeAcpShortenurlQueryModel()
        if 'schema_url' in d:
            o.schema_url = d['schema_url']
        return o


