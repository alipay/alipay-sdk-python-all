#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeliveryActivityInfo import DeliveryActivityInfo


class AlipayUserDtbankcustActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankcustActivityQueryResponse, self).__init__()
        self._delivery_activity_infos = None
        self._has_next = None
        self._item_count = None
        self._last_activity_id = None
        self._recommend_display = None

    @property
    def delivery_activity_infos(self):
        return self._delivery_activity_infos

    @delivery_activity_infos.setter
    def delivery_activity_infos(self, value):
        if isinstance(value, list):
            self._delivery_activity_infos = list()
            for i in value:
                if isinstance(i, DeliveryActivityInfo):
                    self._delivery_activity_infos.append(i)
                else:
                    self._delivery_activity_infos.append(DeliveryActivityInfo.from_alipay_dict(i))
    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
    @property
    def item_count(self):
        return self._item_count

    @item_count.setter
    def item_count(self, value):
        self._item_count = value
    @property
    def last_activity_id(self):
        return self._last_activity_id

    @last_activity_id.setter
    def last_activity_id(self, value):
        self._last_activity_id = value
    @property
    def recommend_display(self):
        return self._recommend_display

    @recommend_display.setter
    def recommend_display(self, value):
        self._recommend_display = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankcustActivityQueryResponse, self).parse_response_content(response_content)
        if 'delivery_activity_infos' in response:
            self.delivery_activity_infos = response['delivery_activity_infos']
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'item_count' in response:
            self.item_count = response['item_count']
        if 'last_activity_id' in response:
            self.last_activity_id = response['last_activity_id']
        if 'recommend_display' in response:
            self.recommend_display = response['recommend_display']
