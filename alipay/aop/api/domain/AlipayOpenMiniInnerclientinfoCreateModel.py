#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerclientinfoCreateModel(object):

    def __init__(self):
        self._bundle_id = None
        self._bundle_name = None
        self._bundle_prefix = None
        self._inst_code = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def bundle_name(self):
        return self._bundle_name

    @bundle_name.setter
    def bundle_name(self, value):
        self._bundle_name = value
    @property
    def bundle_prefix(self):
        return self._bundle_prefix

    @bundle_prefix.setter
    def bundle_prefix(self, value):
        self._bundle_prefix = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.bundle_name:
            if hasattr(self.bundle_name, 'to_alipay_dict'):
                params['bundle_name'] = self.bundle_name.to_alipay_dict()
            else:
                params['bundle_name'] = self.bundle_name
        if self.bundle_prefix:
            if hasattr(self.bundle_prefix, 'to_alipay_dict'):
                params['bundle_prefix'] = self.bundle_prefix.to_alipay_dict()
            else:
                params['bundle_prefix'] = self.bundle_prefix
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerclientinfoCreateModel()
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'bundle_name' in d:
            o.bundle_name = d['bundle_name']
        if 'bundle_prefix' in d:
            o.bundle_prefix = d['bundle_prefix']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        return o


