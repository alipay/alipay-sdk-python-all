#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ObjTagRequest import ObjTagRequest


class AlipayFinanceQuotationQuotetradeopenTagQueryModel(object):

    def __init__(self):
        self._obj_tag_request = None

    @property
    def obj_tag_request(self):
        return self._obj_tag_request

    @obj_tag_request.setter
    def obj_tag_request(self, value):
        if isinstance(value, ObjTagRequest):
            self._obj_tag_request = value
        else:
            self._obj_tag_request = ObjTagRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.obj_tag_request:
            if hasattr(self.obj_tag_request, 'to_alipay_dict'):
                params['obj_tag_request'] = self.obj_tag_request.to_alipay_dict()
            else:
                params['obj_tag_request'] = self.obj_tag_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinanceQuotationQuotetradeopenTagQueryModel()
        if 'obj_tag_request' in d:
            o.obj_tag_request = d['obj_tag_request']
        return o


