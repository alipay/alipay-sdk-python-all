#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryJobContractQueryModel(object):

    def __init__(self):
        self._outer_biz_no = None

    @property
    def outer_biz_no(self):
        return self._outer_biz_no

    @outer_biz_no.setter
    def outer_biz_no(self, value):
        self._outer_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.outer_biz_no:
            if hasattr(self.outer_biz_no, 'to_alipay_dict'):
                params['outer_biz_no'] = self.outer_biz_no.to_alipay_dict()
            else:
                params['outer_biz_no'] = self.outer_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryJobContractQueryModel()
        if 'outer_biz_no' in d:
            o.outer_biz_no = d['outer_biz_no']
        return o


