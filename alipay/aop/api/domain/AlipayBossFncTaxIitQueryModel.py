#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IitBizDetailBillQueryPageOpenApiDTO import IitBizDetailBillQueryPageOpenApiDTO


class AlipayBossFncTaxIitQueryModel(object):

    def __init__(self):
        self._iit_request = None

    @property
    def iit_request(self):
        return self._iit_request

    @iit_request.setter
    def iit_request(self, value):
        if isinstance(value, IitBizDetailBillQueryPageOpenApiDTO):
            self._iit_request = value
        else:
            self._iit_request = IitBizDetailBillQueryPageOpenApiDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.iit_request:
            if hasattr(self.iit_request, 'to_alipay_dict'):
                params['iit_request'] = self.iit_request.to_alipay_dict()
            else:
                params['iit_request'] = self.iit_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncTaxIitQueryModel()
        if 'iit_request' in d:
            o.iit_request = d['iit_request']
        return o


