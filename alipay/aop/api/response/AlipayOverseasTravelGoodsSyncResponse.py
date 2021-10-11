#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTravelGoodsSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelGoodsSyncResponse, self).__init__()
        self._goods_biz_status = None
        self._sync_order_id = None
        self._sync_status = None

    @property
    def goods_biz_status(self):
        return self._goods_biz_status

    @goods_biz_status.setter
    def goods_biz_status(self, value):
        self._goods_biz_status = value
    @property
    def sync_order_id(self):
        return self._sync_order_id

    @sync_order_id.setter
    def sync_order_id(self, value):
        self._sync_order_id = value
    @property
    def sync_status(self):
        return self._sync_status

    @sync_status.setter
    def sync_status(self, value):
        self._sync_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelGoodsSyncResponse, self).parse_response_content(response_content)
        if 'goods_biz_status' in response:
            self.goods_biz_status = response['goods_biz_status']
        if 'sync_order_id' in response:
            self.sync_order_id = response['sync_order_id']
        if 'sync_status' in response:
            self.sync_status = response['sync_status']
