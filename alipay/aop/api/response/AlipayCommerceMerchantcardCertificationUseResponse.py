#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertificateSubmitResonse import CertificateSubmitResonse


class AlipayCommerceMerchantcardCertificationUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardCertificationUseResponse, self).__init__()
        self._context = None
        self._res = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        if isinstance(value, list):
            self._context = list()
            for i in value:
                if isinstance(i, CertificateSubmitResonse):
                    self._context.append(i)
                else:
                    self._context.append(CertificateSubmitResonse.from_alipay_dict(i))
    @property
    def res(self):
        return self._res

    @res.setter
    def res(self, value):
        self._res = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardCertificationUseResponse, self).parse_response_content(response_content)
        if 'context' in response:
            self.context = response['context']
        if 'res' in response:
            self.res = response['res']
