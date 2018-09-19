#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetPointOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetPointOrderQueryResponse, self).__init__()
        self._alipay_order_no = None
        self._create_time = None
        self._dispatch_user_id = None
        self._memo = None
        self._merchant_order_no = None
        self._order_status = None
        self._point_count = None
        self._receive_user_id = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def dispatch_user_id(self):
        return self._dispatch_user_id

    @dispatch_user_id.setter
    def dispatch_user_id(self, value):
        self._dispatch_user_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def point_count(self):
        return self._point_count

    @point_count.setter
    def point_count(self, value):
        self._point_count = value
    @property
    def receive_user_id(self):
        return self._receive_user_id

    @receive_user_id.setter
    def receive_user_id(self, value):
        self._receive_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetPointOrderQueryResponse, self).parse_response_content(response_content)
        if 'alipay_order_no' in response:
            self.alipay_order_no = response['alipay_order_no']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'dispatch_user_id' in response:
            self.dispatch_user_id = response['dispatch_user_id']
        if 'memo' in response:
            self.memo = response['memo']
        if 'merchant_order_no' in response:
            self.merchant_order_no = response['merchant_order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'point_count' in response:
            self.point_count = response['point_count']
        if 'receive_user_id' in response:
            self.receive_user_id = response['receive_user_id']
