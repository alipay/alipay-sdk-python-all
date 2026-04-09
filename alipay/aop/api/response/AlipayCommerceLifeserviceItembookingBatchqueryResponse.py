#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LifeserviceItemBookingRelation import LifeserviceItemBookingRelation


class AlipayCommerceLifeserviceItembookingBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceItembookingBatchqueryResponse, self).__init__()
        self._content = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, list):
            self._content = list()
            for i in value:
                if isinstance(i, LifeserviceItemBookingRelation):
                    self._content.append(i)
                else:
                    self._content.append(LifeserviceItemBookingRelation.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceItembookingBatchqueryResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
