#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceFundBindQueryModel(object):

    def __init__(self):
        self._out_bind_no = None

    @property
    def out_bind_no(self):
        return self._out_bind_no

    @out_bind_no.setter
    def out_bind_no(self, value):
        self._out_bind_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_bind_no:
            if hasattr(self.out_bind_no, 'to_alipay_dict'):
                params['out_bind_no'] = self.out_bind_no.to_alipay_dict()
            else:
                params['out_bind_no'] = self.out_bind_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceFundBindQueryModel()
        if 'out_bind_no' in d:
            o.out_bind_no = d['out_bind_no']
        return o


