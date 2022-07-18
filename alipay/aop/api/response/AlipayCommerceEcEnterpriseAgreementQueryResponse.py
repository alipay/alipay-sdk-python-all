#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnterpriseAgreementDTO import EnterpriseAgreementDTO


class AlipayCommerceEcEnterpriseAgreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEnterpriseAgreementQueryResponse, self).__init__()
        self._enterprise_agreement_dto = None

    @property
    def enterprise_agreement_dto(self):
        return self._enterprise_agreement_dto

    @enterprise_agreement_dto.setter
    def enterprise_agreement_dto(self, value):
        if isinstance(value, EnterpriseAgreementDTO):
            self._enterprise_agreement_dto = value
        else:
            self._enterprise_agreement_dto = EnterpriseAgreementDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEnterpriseAgreementQueryResponse, self).parse_response_content(response_content)
        if 'enterprise_agreement_dto' in response:
            self.enterprise_agreement_dto = response['enterprise_agreement_dto']
