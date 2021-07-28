#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneYebAssetOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneYebAssetOrderQueryResponse, self).__init__()
        self._close_by = None
        self._close_reason = None
        self._gmt_close = None
        self._gmt_create = None
        self._order_no = None
        self._order_status = None
        self._order_timeout = None
        self._out_biz_no = None
        self._user_id = None

    @property
    def close_by(self):
        return self._close_by

    @close_by.setter
    def close_by(self, value):
        self._close_by = value
    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def gmt_close(self):
        return self._gmt_close

    @gmt_close.setter
    def gmt_close(self, value):
        self._gmt_close = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_timeout(self):
        return self._order_timeout

    @order_timeout.setter
    def order_timeout(self, value):
        self._order_timeout = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneYebAssetOrderQueryResponse, self).parse_response_content(response_content)
        if 'close_by' in response:
            self.close_by = response['close_by']
        if 'close_reason' in response:
            self.close_reason = response['close_reason']
        if 'gmt_close' in response:
            self.gmt_close = response['gmt_close']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'order_timeout' in response:
            self.order_timeout = response['order_timeout']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
