#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderIndirectSmidQueryModel(object):

    def __init__(self):
        self._origin_qrvalue = None

    @property
    def origin_qrvalue(self):
        return self._origin_qrvalue

    @origin_qrvalue.setter
    def origin_qrvalue(self, value):
        self._origin_qrvalue = value


    def to_alipay_dict(self):
        params = dict()
        if self.origin_qrvalue:
            if hasattr(self.origin_qrvalue, 'to_alipay_dict'):
                params['origin_qrvalue'] = self.origin_qrvalue.to_alipay_dict()
            else:
                params['origin_qrvalue'] = self.origin_qrvalue
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderIndirectSmidQueryModel()
        if 'origin_qrvalue' in d:
            o.origin_qrvalue = d['origin_qrvalue']
        return o


