#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryTrafficFacecertifyresultQueryModel(object):

    def __init__(self):
        self._check_id = None

    @property
    def check_id(self):
        return self._check_id

    @check_id.setter
    def check_id(self, value):
        self._check_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_id:
            if hasattr(self.check_id, 'to_alipay_dict'):
                params['check_id'] = self.check_id.to_alipay_dict()
            else:
                params['check_id'] = self.check_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryTrafficFacecertifyresultQueryModel()
        if 'check_id' in d:
            o.check_id = d['check_id']
        return o


