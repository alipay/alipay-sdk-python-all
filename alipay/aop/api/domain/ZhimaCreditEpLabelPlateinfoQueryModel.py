#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpLabelPlateinfoQueryModel(object):

    def __init__(self):
        self._plate_biz_no = None

    @property
    def plate_biz_no(self):
        return self._plate_biz_no

    @plate_biz_no.setter
    def plate_biz_no(self, value):
        self._plate_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.plate_biz_no:
            if hasattr(self.plate_biz_no, 'to_alipay_dict'):
                params['plate_biz_no'] = self.plate_biz_no.to_alipay_dict()
            else:
                params['plate_biz_no'] = self.plate_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpLabelPlateinfoQueryModel()
        if 'plate_biz_no' in d:
            o.plate_biz_no = d['plate_biz_no']
        return o


