#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePropertyVideocallRoomCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePropertyVideocallRoomCreateResponse, self).__init__()
        self._biz_name = None
        self._device_id = None
        self._owner_id = None
        self._r_token = None
        self._room_id = None
        self._room_sign = None
        self._server_url_arr = None
        self._sub_biz_name = None
        self._visit_biz_id = None
        self._visitor_customer_id = None

    @property
    def biz_name(self):
        return self._biz_name

    @biz_name.setter
    def biz_name(self, value):
        self._biz_name = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def r_token(self):
        return self._r_token

    @r_token.setter
    def r_token(self, value):
        self._r_token = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value
    @property
    def room_sign(self):
        return self._room_sign

    @room_sign.setter
    def room_sign(self, value):
        self._room_sign = value
    @property
    def server_url_arr(self):
        return self._server_url_arr

    @server_url_arr.setter
    def server_url_arr(self, value):
        self._server_url_arr = value
    @property
    def sub_biz_name(self):
        return self._sub_biz_name

    @sub_biz_name.setter
    def sub_biz_name(self, value):
        self._sub_biz_name = value
    @property
    def visit_biz_id(self):
        return self._visit_biz_id

    @visit_biz_id.setter
    def visit_biz_id(self, value):
        self._visit_biz_id = value
    @property
    def visitor_customer_id(self):
        return self._visitor_customer_id

    @visitor_customer_id.setter
    def visitor_customer_id(self, value):
        self._visitor_customer_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePropertyVideocallRoomCreateResponse, self).parse_response_content(response_content)
        if 'biz_name' in response:
            self.biz_name = response['biz_name']
        if 'device_id' in response:
            self.device_id = response['device_id']
        if 'owner_id' in response:
            self.owner_id = response['owner_id']
        if 'r_token' in response:
            self.r_token = response['r_token']
        if 'room_id' in response:
            self.room_id = response['room_id']
        if 'room_sign' in response:
            self.room_sign = response['room_sign']
        if 'server_url_arr' in response:
            self.server_url_arr = response['server_url_arr']
        if 'sub_biz_name' in response:
            self.sub_biz_name = response['sub_biz_name']
        if 'visit_biz_id' in response:
            self.visit_biz_id = response['visit_biz_id']
        if 'visitor_customer_id' in response:
            self.visitor_customer_id = response['visitor_customer_id']
