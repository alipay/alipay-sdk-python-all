#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromoterDeleteInfo import PromoterDeleteInfo


class AlipayCommerceOperationPromoterRelationDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPromoterRelationDeleteResponse, self).__init__()
        self._promoter_delete_result = None

    @property
    def promoter_delete_result(self):
        return self._promoter_delete_result

    @promoter_delete_result.setter
    def promoter_delete_result(self, value):
        if isinstance(value, PromoterDeleteInfo):
            self._promoter_delete_result = value
        else:
            self._promoter_delete_result = PromoterDeleteInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPromoterRelationDeleteResponse, self).parse_response_content(response_content)
        if 'promoter_delete_result' in response:
            self.promoter_delete_result = response['promoter_delete_result']
