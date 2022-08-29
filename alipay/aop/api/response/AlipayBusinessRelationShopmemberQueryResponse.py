#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopMemberInfo import ShopMemberInfo


class AlipayBusinessRelationShopmemberQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessRelationShopmemberQueryResponse, self).__init__()
        self._shop_member_infos = None

    @property
    def shop_member_infos(self):
        return self._shop_member_infos

    @shop_member_infos.setter
    def shop_member_infos(self, value):
        if isinstance(value, list):
            self._shop_member_infos = list()
            for i in value:
                if isinstance(i, ShopMemberInfo):
                    self._shop_member_infos.append(i)
                else:
                    self._shop_member_infos.append(ShopMemberInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessRelationShopmemberQueryResponse, self).parse_response_content(response_content)
        if 'shop_member_infos' in response:
            self.shop_member_infos = response['shop_member_infos']
