#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneApplicationQueryModel(object):

    def __init__(self):
        self._application_no = None
        self._out_biz_no = None
        self._prod_code = None

    @property
    def application_no(self):
        return self._application_no

    @application_no.setter
    def application_no(self, value):
        self._application_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_no:
            if hasattr(self.application_no, 'to_alipay_dict'):
                params['application_no'] = self.application_no.to_alipay_dict()
            else:
                params['application_no'] = self.application_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneApplicationQueryModel()
        if 'application_no' in d:
            o.application_no = d['application_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        return o


