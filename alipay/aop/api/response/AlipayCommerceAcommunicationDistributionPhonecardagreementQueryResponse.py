#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PhoneCardAgreementModel import PhoneCardAgreementModel


class AlipayCommerceAcommunicationDistributionPhonecardagreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationDistributionPhonecardagreementQueryResponse, self).__init__()
        self._agreement_list = None
        self._agreement_request_id = None

    @property
    def agreement_list(self):
        return self._agreement_list

    @agreement_list.setter
    def agreement_list(self, value):
        if isinstance(value, list):
            self._agreement_list = list()
            for i in value:
                if isinstance(i, PhoneCardAgreementModel):
                    self._agreement_list.append(i)
                else:
                    self._agreement_list.append(PhoneCardAgreementModel.from_alipay_dict(i))
    @property
    def agreement_request_id(self):
        return self._agreement_request_id

    @agreement_request_id.setter
    def agreement_request_id(self, value):
        self._agreement_request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationDistributionPhonecardagreementQueryResponse, self).parse_response_content(response_content)
        if 'agreement_list' in response:
            self.agreement_list = response['agreement_list']
        if 'agreement_request_id' in response:
            self.agreement_request_id = response['agreement_request_id']
