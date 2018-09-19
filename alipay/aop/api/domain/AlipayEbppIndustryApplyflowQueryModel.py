#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryApplyflowQueryModel(object):

    def __init__(self):
        self._apply_flow_no = None
        self._extend_field = None
        self._out_apply_no = None

    @property
    def apply_flow_no(self):
        return self._apply_flow_no

    @apply_flow_no.setter
    def apply_flow_no(self, value):
        self._apply_flow_no = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_flow_no:
            if hasattr(self.apply_flow_no, 'to_alipay_dict'):
                params['apply_flow_no'] = self.apply_flow_no.to_alipay_dict()
            else:
                params['apply_flow_no'] = self.apply_flow_no
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryApplyflowQueryModel()
        if 'apply_flow_no' in d:
            o.apply_flow_no = d['apply_flow_no']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        return o


