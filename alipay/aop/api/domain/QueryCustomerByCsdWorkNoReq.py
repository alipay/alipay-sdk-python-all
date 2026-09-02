#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryCustomerByCsdWorkNoReq(object):

    def __init__(self):
        self._csd_work_no = None

    @property
    def csd_work_no(self):
        return self._csd_work_no

    @csd_work_no.setter
    def csd_work_no(self, value):
        self._csd_work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.csd_work_no:
            if hasattr(self.csd_work_no, 'to_alipay_dict'):
                params['csd_work_no'] = self.csd_work_no.to_alipay_dict()
            else:
                params['csd_work_no'] = self.csd_work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryCustomerByCsdWorkNoReq()
        if 'csd_work_no' in d:
            o.csd_work_no = d['csd_work_no']
        return o


