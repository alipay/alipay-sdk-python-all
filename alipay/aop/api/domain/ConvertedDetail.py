#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConvertedDetail(object):

    def __init__(self):
        self._converted_id = None
        self._converted_name = None

    @property
    def converted_id(self):
        return self._converted_id

    @converted_id.setter
    def converted_id(self, value):
        self._converted_id = value
    @property
    def converted_name(self):
        return self._converted_name

    @converted_name.setter
    def converted_name(self, value):
        self._converted_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.converted_id:
            if hasattr(self.converted_id, 'to_alipay_dict'):
                params['converted_id'] = self.converted_id.to_alipay_dict()
            else:
                params['converted_id'] = self.converted_id
        if self.converted_name:
            if hasattr(self.converted_name, 'to_alipay_dict'):
                params['converted_name'] = self.converted_name.to_alipay_dict()
            else:
                params['converted_name'] = self.converted_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConvertedDetail()
        if 'converted_id' in d:
            o.converted_id = d['converted_id']
        if 'converted_name' in d:
            o.converted_name = d['converted_name']
        return o


