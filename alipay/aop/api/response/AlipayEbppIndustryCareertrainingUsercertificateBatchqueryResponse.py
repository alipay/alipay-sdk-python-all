#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UsercertificateObject import UsercertificateObject


class AlipayEbppIndustryCareertrainingUsercertificateBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCareertrainingUsercertificateBatchqueryResponse, self).__init__()
        self._list = None
        self._total = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, UsercertificateObject):
            self._list = value
        else:
            self._list = UsercertificateObject.from_alipay_dict(value)
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCareertrainingUsercertificateBatchqueryResponse, self).parse_response_content(response_content)
        if 'list' in response:
            self.list = response['list']
        if 'total' in response:
            self.total = response['total']
