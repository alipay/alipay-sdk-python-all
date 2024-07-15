#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoItemExtInfo(object):

    def __init__(self):
        self._out_single_subsidy = None

    @property
    def out_single_subsidy(self):
        return self._out_single_subsidy

    @out_single_subsidy.setter
    def out_single_subsidy(self, value):
        self._out_single_subsidy = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_single_subsidy:
            if hasattr(self.out_single_subsidy, 'to_alipay_dict'):
                params['out_single_subsidy'] = self.out_single_subsidy.to_alipay_dict()
            else:
                params['out_single_subsidy'] = self.out_single_subsidy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoItemExtInfo()
        if 'out_single_subsidy' in d:
            o.out_single_subsidy = d['out_single_subsidy']
        return o


