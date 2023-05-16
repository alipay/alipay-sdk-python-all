#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CedsipeihuanCcomplex import CedsipeihuanCcomplex


class AlipaySecurityProdOpenapiVBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdOpenapiVBatchqueryResponse, self).__init__()
        self._area_code = None
        self._cde = None
        self._ds = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def cde(self):
        return self._cde

    @cde.setter
    def cde(self, value):
        self._cde = value
    @property
    def ds(self):
        return self._ds

    @ds.setter
    def ds(self, value):
        if isinstance(value, CedsipeihuanCcomplex):
            self._ds = value
        else:
            self._ds = CedsipeihuanCcomplex.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdOpenapiVBatchqueryResponse, self).parse_response_content(response_content)
        if 'area_code' in response:
            self.area_code = response['area_code']
        if 'cde' in response:
            self.cde = response['cde']
        if 'ds' in response:
            self.ds = response['ds']
