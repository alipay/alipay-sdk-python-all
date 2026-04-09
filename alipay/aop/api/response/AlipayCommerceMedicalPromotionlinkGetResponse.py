#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalPromotionlinkGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalPromotionlinkGetResponse, self).__init__()
        self._promotion_link = None

    @property
    def promotion_link(self):
        return self._promotion_link

    @promotion_link.setter
    def promotion_link(self, value):
        self._promotion_link = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalPromotionlinkGetResponse, self).parse_response_content(response_content)
        if 'promotion_link' in response:
            self.promotion_link = response['promotion_link']
