#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMerchantcardAgreementtemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardAgreementtemplateQueryResponse, self).__init__()
        self._order_agreement_template_content = None

    @property
    def order_agreement_template_content(self):
        return self._order_agreement_template_content

    @order_agreement_template_content.setter
    def order_agreement_template_content(self, value):
        self._order_agreement_template_content = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardAgreementtemplateQueryResponse, self).parse_response_content(response_content)
        if 'order_agreement_template_content' in response:
            self.order_agreement_template_content = response['order_agreement_template_content']
