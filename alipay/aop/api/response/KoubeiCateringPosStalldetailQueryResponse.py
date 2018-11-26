#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StallEntity import StallEntity


class KoubeiCateringPosStalldetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosStalldetailQueryResponse, self).__init__()
        self._stall_entity = None

    @property
    def stall_entity(self):
        return self._stall_entity

    @stall_entity.setter
    def stall_entity(self, value):
        if isinstance(value, StallEntity):
            self._stall_entity = value
        else:
            self._stall_entity = StallEntity.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosStalldetailQueryResponse, self).parse_response_content(response_content)
        if 'stall_entity' in response:
            self.stall_entity = response['stall_entity']
