#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistCarfinExpressverificationQueryModel(object):

    def __init__(self):
        self._express_no = None
        self._out_express_no = None

    @property
    def express_no(self):
        return self._express_no

    @express_no.setter
    def express_no(self, value):
        self._express_no = value
    @property
    def out_express_no(self):
        return self._out_express_no

    @out_express_no.setter
    def out_express_no(self, value):
        self._out_express_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.express_no:
            if hasattr(self.express_no, 'to_alipay_dict'):
                params['express_no'] = self.express_no.to_alipay_dict()
            else:
                params['express_no'] = self.express_no
        if self.out_express_no:
            if hasattr(self.out_express_no, 'to_alipay_dict'):
                params['out_express_no'] = self.out_express_no.to_alipay_dict()
            else:
                params['out_express_no'] = self.out_express_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinExpressverificationQueryModel()
        if 'express_no' in d:
            o.express_no = d['express_no']
        if 'out_express_no' in d:
            o.out_express_no = d['out_express_no']
        return o


