#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditBankTraining import CreditBankTraining


class AlipayCommerceEducateCreditbankTrainingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCreditbankTrainingQueryResponse, self).__init__()
        self._training = None

    @property
    def training(self):
        return self._training

    @training.setter
    def training(self, value):
        if isinstance(value, list):
            self._training = list()
            for i in value:
                if isinstance(i, CreditBankTraining):
                    self._training.append(i)
                else:
                    self._training.append(CreditBankTraining.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCreditbankTrainingQueryResponse, self).parse_response_content(response_content)
        if 'training' in response:
            self.training = response['training']
