#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePropertyVideocallCheckModel(object):

    def __init__(self):
        self._visit_biz_id = None

    @property
    def visit_biz_id(self):
        return self._visit_biz_id

    @visit_biz_id.setter
    def visit_biz_id(self, value):
        self._visit_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.visit_biz_id:
            if hasattr(self.visit_biz_id, 'to_alipay_dict'):
                params['visit_biz_id'] = self.visit_biz_id.to_alipay_dict()
            else:
                params['visit_biz_id'] = self.visit_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePropertyVideocallCheckModel()
        if 'visit_biz_id' in d:
            o.visit_biz_id = d['visit_biz_id']
        return o


