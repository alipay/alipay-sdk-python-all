#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PoiInfoVo import PoiInfoVo


class AlipayCloudCloudpromoPartnerAllpoiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoPartnerAllpoiQueryResponse, self).__init__()
        self._agent_id = None
        self._item_id = None
        self._next_nearest_poi_list = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def next_nearest_poi_list(self):
        return self._next_nearest_poi_list

    @next_nearest_poi_list.setter
    def next_nearest_poi_list(self, value):
        if isinstance(value, PoiInfoVo):
            self._next_nearest_poi_list = value
        else:
            self._next_nearest_poi_list = PoiInfoVo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoPartnerAllpoiQueryResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'next_nearest_poi_list' in response:
            self.next_nearest_poi_list = response['next_nearest_poi_list']
