#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne


class AlipaySecurityProdDfesfDefBatchqueryModel(object):

    def __init__(self):
        self._dd = None
        self._latitude = None

    @property
    def dd(self):
        return self._dd

    @dd.setter
    def dd(self, value):
        if isinstance(value, GavintestNewLeveaOne):
            self._dd = value
        else:
            self._dd = GavintestNewLeveaOne.from_alipay_dict(value)
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value


    def to_alipay_dict(self):
        params = dict()
        if self.dd:
            if hasattr(self.dd, 'to_alipay_dict'):
                params['dd'] = self.dd.to_alipay_dict()
            else:
                params['dd'] = self.dd
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdDfesfDefBatchqueryModel()
        if 'dd' in d:
            o.dd = d['dd']
        if 'latitude' in d:
            o.latitude = d['latitude']
        return o


