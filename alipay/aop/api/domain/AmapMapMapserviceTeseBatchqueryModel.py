#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AmapMapMapserviceTeseBatchqueryModel(object):

    def __init__(self):
        self._sed = None

    @property
    def sed(self):
        return self._sed

    @sed.setter
    def sed(self, value):
        self._sed = value


    def to_alipay_dict(self):
        params = dict()
        if self.sed:
            if hasattr(self.sed, 'to_alipay_dict'):
                params['sed'] = self.sed.to_alipay_dict()
            else:
                params['sed'] = self.sed
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmapMapMapserviceTeseBatchqueryModel()
        if 'sed' in d:
            o.sed = d['sed']
        return o


