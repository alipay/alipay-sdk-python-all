#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppServicePromoDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppServicePromoDeleteResponse, self).__init__()
        self._promo_record_id = None

    @property
    def promo_record_id(self):
        return self._promo_record_id

    @promo_record_id.setter
    def promo_record_id(self, value):
        self._promo_record_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppServicePromoDeleteResponse, self).parse_response_content(response_content)
        if 'promo_record_id' in response:
            self.promo_record_id = response['promo_record_id']
