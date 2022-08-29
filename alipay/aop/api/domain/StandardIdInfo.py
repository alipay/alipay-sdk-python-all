#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StandardIdInfo(object):

    def __init__(self):
        self._outer_source_id = None
        self._standard_id = None

    @property
    def outer_source_id(self):
        return self._outer_source_id

    @outer_source_id.setter
    def outer_source_id(self, value):
        self._outer_source_id = value
    @property
    def standard_id(self):
        return self._standard_id

    @standard_id.setter
    def standard_id(self, value):
        self._standard_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.outer_source_id:
            if hasattr(self.outer_source_id, 'to_alipay_dict'):
                params['outer_source_id'] = self.outer_source_id.to_alipay_dict()
            else:
                params['outer_source_id'] = self.outer_source_id
        if self.standard_id:
            if hasattr(self.standard_id, 'to_alipay_dict'):
                params['standard_id'] = self.standard_id.to_alipay_dict()
            else:
                params['standard_id'] = self.standard_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StandardIdInfo()
        if 'outer_source_id' in d:
            o.outer_source_id = d['outer_source_id']
        if 'standard_id' in d:
            o.standard_id = d['standard_id']
        return o


