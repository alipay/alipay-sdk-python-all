#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PageTemplateParamInfoDTO import PageTemplateParamInfoDTO


class AlipaySecurityYyuDvsdvdsBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityYyuDvsdvdsBatchqueryResponse, self).__init__()
        self._asd = None
        self._asdasda = None
        self._asdf = None
        self._sadf = None

    @property
    def asd(self):
        return self._asd

    @asd.setter
    def asd(self, value):
        if isinstance(value, PageTemplateParamInfoDTO):
            self._asd = value
        else:
            self._asd = PageTemplateParamInfoDTO.from_alipay_dict(value)
    @property
    def asdasda(self):
        return self._asdasda

    @asdasda.setter
    def asdasda(self, value):
        self._asdasda = value
    @property
    def asdf(self):
        return self._asdf

    @asdf.setter
    def asdf(self, value):
        self._asdf = value
    @property
    def sadf(self):
        return self._sadf

    @sadf.setter
    def sadf(self, value):
        self._sadf = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityYyuDvsdvdsBatchqueryResponse, self).parse_response_content(response_content)
        if 'asd' in response:
            self.asd = response['asd']
        if 'asdasda' in response:
            self.asdasda = response['asdasda']
        if 'asdf' in response:
            self.asdf = response['asdf']
        if 'sadf' in response:
            self.sadf = response['sadf']
