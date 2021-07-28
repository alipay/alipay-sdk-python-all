#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTravelGoodsSyncresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelGoodsSyncresultQueryResponse, self).__init__()
        self._goods_biz_status = None
        self._sync_failed_code = None
        self._sync_failed_msg = None
        self._sync_status = None

    @property
    def goods_biz_status(self):
        return self._goods_biz_status

    @goods_biz_status.setter
    def goods_biz_status(self, value):
        self._goods_biz_status = value
    @property
    def sync_failed_code(self):
        return self._sync_failed_code

    @sync_failed_code.setter
    def sync_failed_code(self, value):
        self._sync_failed_code = value
    @property
    def sync_failed_msg(self):
        return self._sync_failed_msg

    @sync_failed_msg.setter
    def sync_failed_msg(self, value):
        self._sync_failed_msg = value
    @property
    def sync_status(self):
        return self._sync_status

    @sync_status.setter
    def sync_status(self, value):
        self._sync_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelGoodsSyncresultQueryResponse, self).parse_response_content(response_content)
        if 'goods_biz_status' in response:
            self.goods_biz_status = response['goods_biz_status']
        if 'sync_failed_code' in response:
            self.sync_failed_code = response['sync_failed_code']
        if 'sync_failed_msg' in response:
            self.sync_failed_msg = response['sync_failed_msg']
        if 'sync_status' in response:
            self.sync_status = response['sync_status']
