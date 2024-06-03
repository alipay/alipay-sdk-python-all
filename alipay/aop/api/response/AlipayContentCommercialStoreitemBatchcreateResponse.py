#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LiveStoreItemInfoDTO import LiveStoreItemInfoDTO


class AlipayContentCommercialStoreitemBatchcreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayContentCommercialStoreitemBatchcreateResponse, self).__init__()
        self._item_info_list = None

    @property
    def item_info_list(self):
        return self._item_info_list

    @item_info_list.setter
    def item_info_list(self, value):
        if isinstance(value, list):
            self._item_info_list = list()
            for i in value:
                if isinstance(i, LiveStoreItemInfoDTO):
                    self._item_info_list.append(i)
                else:
                    self._item_info_list.append(LiveStoreItemInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayContentCommercialStoreitemBatchcreateResponse, self).parse_response_content(response_content)
        if 'item_info_list' in response:
            self.item_info_list = response['item_info_list']
