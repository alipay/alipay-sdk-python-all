#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne


class AlipayOpenMiniReleaststBatchqueryModel(object):

    def __init__(self):
        self._canshu = None
        self._fuza = None

    @property
    def canshu(self):
        return self._canshu

    @canshu.setter
    def canshu(self, value):
        self._canshu = value
    @property
    def fuza(self):
        return self._fuza

    @fuza.setter
    def fuza(self, value):
        if isinstance(value, GavintestNewLeveaOne):
            self._fuza = value
        else:
            self._fuza = GavintestNewLeveaOne.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.canshu:
            if hasattr(self.canshu, 'to_alipay_dict'):
                params['canshu'] = self.canshu.to_alipay_dict()
            else:
                params['canshu'] = self.canshu
        if self.fuza:
            if hasattr(self.fuza, 'to_alipay_dict'):
                params['fuza'] = self.fuza.to_alipay_dict()
            else:
                params['fuza'] = self.fuza
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniReleaststBatchqueryModel()
        if 'canshu' in d:
            o.canshu = d['canshu']
        if 'fuza' in d:
            o.fuza = d['fuza']
        return o


