#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleItemDTO import RecycleItemDTO


class AlipayCommerceRecycleItemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleItemQueryResponse, self).__init__()
        self._recycle_item_dto = None

    @property
    def recycle_item_dto(self):
        return self._recycle_item_dto

    @recycle_item_dto.setter
    def recycle_item_dto(self, value):
        if isinstance(value, RecycleItemDTO):
            self._recycle_item_dto = value
        else:
            self._recycle_item_dto = RecycleItemDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleItemQueryResponse, self).parse_response_content(response_content)
        if 'recycle_item_dto' in response:
            self.recycle_item_dto = response['recycle_item_dto']
