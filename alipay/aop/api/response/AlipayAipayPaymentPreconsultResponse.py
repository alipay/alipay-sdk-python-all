#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AiPayConsultTemplate import AiPayConsultTemplate


class AlipayAipayPaymentPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayPaymentPreconsultResponse, self).__init__()
        self._business_data = None
        self._template = None

    @property
    def business_data(self):
        return self._business_data

    @business_data.setter
    def business_data(self, value):
        self._business_data = value
    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        if isinstance(value, AiPayConsultTemplate):
            self._template = value
        else:
            self._template = AiPayConsultTemplate.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayAipayPaymentPreconsultResponse, self).parse_response_content(response_content)
        if 'business_data' in response:
            self.business_data = response['business_data']
        if 'template' in response:
            self.template = response['template']
