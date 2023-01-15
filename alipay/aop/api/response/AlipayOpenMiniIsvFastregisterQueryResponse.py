#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniIsvFastregisterQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniIsvFastregisterQueryResponse, self).__init__()
        self._app_name = None
        self._isv_app_id = None
        self._mini_app_id = None
        self._order_no = None
        self._out_order_no = None
        self._status = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniIsvFastregisterQueryResponse, self).parse_response_content(response_content)
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'isv_app_id' in response:
            self.isv_app_id = response['isv_app_id']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'status' in response:
            self.status = response['status']
