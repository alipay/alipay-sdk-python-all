#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdTianwutestModifyModel(object):

    def __init__(self):
        self._tianwutest = None

    @property
    def tianwutest(self):
        return self._tianwutest

    @tianwutest.setter
    def tianwutest(self, value):
        self._tianwutest = value


    def to_alipay_dict(self):
        params = dict()
        if self.tianwutest:
            if hasattr(self.tianwutest, 'to_alipay_dict'):
                params['tianwutest'] = self.tianwutest.to_alipay_dict()
            else:
                params['tianwutest'] = self.tianwutest
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdTianwutestModifyModel()
        if 'tianwutest' in d:
            o.tianwutest = d['tianwutest']
        return o


