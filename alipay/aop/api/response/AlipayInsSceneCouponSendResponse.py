#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsCertificate import InsCertificate
from alipay.aop.api.domain.InsProduct import InsProduct


class AlipayInsSceneCouponSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneCouponSendResponse, self).__init__()
        self._certificate = None
        self._compaign_id = None
        self._flow_id = None
        self._product = None

    @property
    def certificate(self):
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        if isinstance(value, InsCertificate):
            self._certificate = value
        else:
            self._certificate = InsCertificate.from_alipay_dict(value)
    @property
    def compaign_id(self):
        return self._compaign_id

    @compaign_id.setter
    def compaign_id(self, value):
        self._compaign_id = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        if isinstance(value, InsProduct):
            self._product = value
        else:
            self._product = InsProduct.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneCouponSendResponse, self).parse_response_content(response_content)
        if 'certificate' in response:
            self.certificate = response['certificate']
        if 'compaign_id' in response:
            self.compaign_id = response['compaign_id']
        if 'flow_id' in response:
            self.flow_id = response['flow_id']
        if 'product' in response:
            self.product = response['product']
