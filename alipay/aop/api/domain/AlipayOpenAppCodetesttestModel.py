#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppCodetesttestModel(object):

    def __init__(self):
        self._testparam = None
        self._testtestparam = None

    @property
    def testparam(self):
        return self._testparam

    @testparam.setter
    def testparam(self, value):
        self._testparam = value
    @property
    def testtestparam(self):
        return self._testtestparam

    @testtestparam.setter
    def testtestparam(self, value):
        self._testtestparam = value


    def to_alipay_dict(self):
        params = dict()
        if self.testparam:
            if hasattr(self.testparam, 'to_alipay_dict'):
                params['testparam'] = self.testparam.to_alipay_dict()
            else:
                params['testparam'] = self.testparam
        if self.testtestparam:
            if hasattr(self.testtestparam, 'to_alipay_dict'):
                params['testtestparam'] = self.testtestparam.to_alipay_dict()
            else:
                params['testtestparam'] = self.testtestparam
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppCodetesttestModel()
        if 'testparam' in d:
            o.testparam = d['testparam']
        if 'testtestparam' in d:
            o.testtestparam = d['testtestparam']
        return o


