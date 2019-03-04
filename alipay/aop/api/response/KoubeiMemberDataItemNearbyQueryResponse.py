#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NearbyGoods import NearbyGoods


class KoubeiMemberDataItemNearbyQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMemberDataItemNearbyQueryResponse, self).__init__()
        self._goods_list = None
        self._has_more = None
        self._next_start = None

    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        if isinstance(value, list):
            self._goods_list = list()
            for i in value:
                if isinstance(i, NearbyGoods):
                    self._goods_list.append(i)
                else:
                    self._goods_list.append(NearbyGoods.from_alipay_dict(i))
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def next_start(self):
        return self._next_start

    @next_start.setter
    def next_start(self, value):
        self._next_start = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMemberDataItemNearbyQueryResponse, self).parse_response_content(response_content)
        if 'goods_list' in response:
            self.goods_list = response['goods_list']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'next_start' in response:
            self.next_start = response['next_start']
