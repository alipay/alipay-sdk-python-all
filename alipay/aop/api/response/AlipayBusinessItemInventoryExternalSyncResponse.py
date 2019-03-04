#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBusinessItemInventoryExternalSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessItemInventoryExternalSyncResponse, self).__init__()
        self._item_ids = None
        self._request_id = None

    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, value):
        if isinstance(value, list):
            self._item_ids = list()
            for i in value:
                self._item_ids.append(i)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessItemInventoryExternalSyncResponse, self).parse_response_content(response_content)
        if 'item_ids' in response:
            self.item_ids = response['item_ids']
        if 'request_id' in response:
            self.request_id = response['request_id']
