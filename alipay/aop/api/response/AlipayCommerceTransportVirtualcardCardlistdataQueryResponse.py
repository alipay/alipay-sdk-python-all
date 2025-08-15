#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubSceneCardModel import SubSceneCardModel


class AlipayCommerceTransportVirtualcardCardlistdataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVirtualcardCardlistdataQueryResponse, self).__init__()
        self._identification_card_list = None

    @property
    def identification_card_list(self):
        return self._identification_card_list

    @identification_card_list.setter
    def identification_card_list(self, value):
        if isinstance(value, list):
            self._identification_card_list = list()
            for i in value:
                if isinstance(i, SubSceneCardModel):
                    self._identification_card_list.append(i)
                else:
                    self._identification_card_list.append(SubSceneCardModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVirtualcardCardlistdataQueryResponse, self).parse_response_content(response_content)
        if 'identification_card_list' in response:
            self.identification_card_list = response['identification_card_list']
