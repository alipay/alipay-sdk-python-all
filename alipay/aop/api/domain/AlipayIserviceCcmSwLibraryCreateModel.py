#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmSwLibraryCreateModel(object):

    def __init__(self):
        self._ccs_instance_id = None
        self._instance_code = None
        self._name = None
        self._tree_id = None

    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def instance_code(self):
        return self._instance_code

    @instance_code.setter
    def instance_code(self, value):
        self._instance_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def tree_id(self):
        return self._tree_id

    @tree_id.setter
    def tree_id(self, value):
        self._tree_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.instance_code:
            if hasattr(self.instance_code, 'to_alipay_dict'):
                params['instance_code'] = self.instance_code.to_alipay_dict()
            else:
                params['instance_code'] = self.instance_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.tree_id:
            if hasattr(self.tree_id, 'to_alipay_dict'):
                params['tree_id'] = self.tree_id.to_alipay_dict()
            else:
                params['tree_id'] = self.tree_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmSwLibraryCreateModel()
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'instance_code' in d:
            o.instance_code = d['instance_code']
        if 'name' in d:
            o.name = d['name']
        if 'tree_id' in d:
            o.tree_id = d['tree_id']
        return o


