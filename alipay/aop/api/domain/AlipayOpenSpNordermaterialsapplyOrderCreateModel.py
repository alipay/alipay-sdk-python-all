#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNordermaterialsapplyOrderCreateModel(object):

    def __init__(self):
        self._materials_template_code = None
        self._test_flag = None

    @property
    def materials_template_code(self):
        return self._materials_template_code

    @materials_template_code.setter
    def materials_template_code(self, value):
        self._materials_template_code = value
    @property
    def test_flag(self):
        return self._test_flag

    @test_flag.setter
    def test_flag(self, value):
        self._test_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.materials_template_code:
            if hasattr(self.materials_template_code, 'to_alipay_dict'):
                params['materials_template_code'] = self.materials_template_code.to_alipay_dict()
            else:
                params['materials_template_code'] = self.materials_template_code
        if self.test_flag:
            if hasattr(self.test_flag, 'to_alipay_dict'):
                params['test_flag'] = self.test_flag.to_alipay_dict()
            else:
                params['test_flag'] = self.test_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordermaterialsapplyOrderCreateModel()
        if 'materials_template_code' in d:
            o.materials_template_code = d['materials_template_code']
        if 'test_flag' in d:
            o.test_flag = d['test_flag']
        return o


