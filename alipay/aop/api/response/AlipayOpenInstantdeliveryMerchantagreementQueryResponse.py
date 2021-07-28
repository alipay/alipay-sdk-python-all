#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AgreementDetail import AgreementDetail


class AlipayOpenInstantdeliveryMerchantagreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenInstantdeliveryMerchantagreementQueryResponse, self).__init__()
        self._agreement_detail = None

    @property
    def agreement_detail(self):
        return self._agreement_detail

    @agreement_detail.setter
    def agreement_detail(self, value):
        if isinstance(value, AgreementDetail):
            self._agreement_detail = value
        else:
            self._agreement_detail = AgreementDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenInstantdeliveryMerchantagreementQueryResponse, self).parse_response_content(response_content)
        if 'agreement_detail' in response:
            self.agreement_detail = response['agreement_detail']
