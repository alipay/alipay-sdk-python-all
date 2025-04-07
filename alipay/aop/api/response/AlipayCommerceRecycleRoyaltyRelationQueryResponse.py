#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleRoyaltyQueryVO import RecycleRoyaltyQueryVO


class AlipayCommerceRecycleRoyaltyRelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleRoyaltyRelationQueryResponse, self).__init__()
        self._royalty_list = None

    @property
    def royalty_list(self):
        return self._royalty_list

    @royalty_list.setter
    def royalty_list(self, value):
        if isinstance(value, list):
            self._royalty_list = list()
            for i in value:
                if isinstance(i, RecycleRoyaltyQueryVO):
                    self._royalty_list.append(i)
                else:
                    self._royalty_list.append(RecycleRoyaltyQueryVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleRoyaltyRelationQueryResponse, self).parse_response_content(response_content)
        if 'royalty_list' in response:
            self.royalty_list = response['royalty_list']
