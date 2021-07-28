#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishSpecGroupDetail(object):

    def __init__(self):
        self._spec_id = None
        self._spec_name = None

    @property
    def spec_id(self):
        return self._spec_id

    @spec_id.setter
    def spec_id(self, value):
        self._spec_id = value
    @property
    def spec_name(self):
        return self._spec_name

    @spec_name.setter
    def spec_name(self, value):
        self._spec_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.spec_id:
            if hasattr(self.spec_id, 'to_alipay_dict'):
                params['spec_id'] = self.spec_id.to_alipay_dict()
            else:
                params['spec_id'] = self.spec_id
        if self.spec_name:
            if hasattr(self.spec_name, 'to_alipay_dict'):
                params['spec_name'] = self.spec_name.to_alipay_dict()
            else:
                params['spec_name'] = self.spec_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishSpecGroupDetail()
        if 'spec_id' in d:
            o.spec_id = d['spec_id']
        if 'spec_name' in d:
            o.spec_name = d['spec_name']
        return o


