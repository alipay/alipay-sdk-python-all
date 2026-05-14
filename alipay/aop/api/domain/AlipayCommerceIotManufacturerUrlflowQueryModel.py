#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotManufacturerUrlflowQueryModel(object):

    def __init__(self):
        self._flow_no = None

    @property
    def flow_no(self):
        return self._flow_no

    @flow_no.setter
    def flow_no(self, value):
        self._flow_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.flow_no:
            if hasattr(self.flow_no, 'to_alipay_dict'):
                params['flow_no'] = self.flow_no.to_alipay_dict()
            else:
                params['flow_no'] = self.flow_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotManufacturerUrlflowQueryModel()
        if 'flow_no' in d:
            o.flow_no = d['flow_no']
        return o


