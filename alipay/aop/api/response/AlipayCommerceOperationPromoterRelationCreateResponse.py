#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromoterCreateInfo import PromoterCreateInfo


class AlipayCommerceOperationPromoterRelationCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPromoterRelationCreateResponse, self).__init__()
        self._promoter_create_result = None

    @property
    def promoter_create_result(self):
        return self._promoter_create_result

    @promoter_create_result.setter
    def promoter_create_result(self, value):
        if isinstance(value, PromoterCreateInfo):
            self._promoter_create_result = value
        else:
            self._promoter_create_result = PromoterCreateInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPromoterRelationCreateResponse, self).parse_response_content(response_content)
        if 'promoter_create_result' in response:
            self.promoter_create_result = response['promoter_create_result']
