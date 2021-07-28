#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserInfoVO import UserInfoVO


class AlipayCommerceKidsRelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceKidsRelationQueryResponse, self).__init__()
        self._relation_list = None

    @property
    def relation_list(self):
        return self._relation_list

    @relation_list.setter
    def relation_list(self, value):
        if isinstance(value, list):
            self._relation_list = list()
            for i in value:
                if isinstance(i, UserInfoVO):
                    self._relation_list.append(i)
                else:
                    self._relation_list.append(UserInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceKidsRelationQueryResponse, self).parse_response_content(response_content)
        if 'relation_list' in response:
            self.relation_list = response['relation_list']
