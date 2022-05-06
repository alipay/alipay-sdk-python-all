#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberCardOperator(object):

    def __init__(self):
        self._ext_op_id = None
        self._op_id = None
        self._op_type = None

    @property
    def ext_op_id(self):
        return self._ext_op_id

    @ext_op_id.setter
    def ext_op_id(self, value):
        self._ext_op_id = value
    @property
    def op_id(self):
        return self._op_id

    @op_id.setter
    def op_id(self, value):
        self._op_id = value
    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, value):
        self._op_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_op_id:
            if hasattr(self.ext_op_id, 'to_alipay_dict'):
                params['ext_op_id'] = self.ext_op_id.to_alipay_dict()
            else:
                params['ext_op_id'] = self.ext_op_id
        if self.op_id:
            if hasattr(self.op_id, 'to_alipay_dict'):
                params['op_id'] = self.op_id.to_alipay_dict()
            else:
                params['op_id'] = self.op_id
        if self.op_type:
            if hasattr(self.op_type, 'to_alipay_dict'):
                params['op_type'] = self.op_type.to_alipay_dict()
            else:
                params['op_type'] = self.op_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberCardOperator()
        if 'ext_op_id' in d:
            o.ext_op_id = d['ext_op_id']
        if 'op_id' in d:
            o.op_id = d['op_id']
        if 'op_type' in d:
            o.op_type = d['op_type']
        return o


