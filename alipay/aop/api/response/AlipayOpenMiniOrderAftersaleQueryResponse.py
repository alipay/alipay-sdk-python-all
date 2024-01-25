#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniOrderAftersaleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderAftersaleQueryResponse, self).__init__()
        self._action_type = None
        self._aftersale_reason = None
        self._order_id = None
        self._out_aftersale_id = None
        self._status = None
        self._type = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def aftersale_reason(self):
        return self._aftersale_reason

    @aftersale_reason.setter
    def aftersale_reason(self, value):
        self._aftersale_reason = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_aftersale_id(self):
        return self._out_aftersale_id

    @out_aftersale_id.setter
    def out_aftersale_id(self, value):
        self._out_aftersale_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderAftersaleQueryResponse, self).parse_response_content(response_content)
        if 'action_type' in response:
            self.action_type = response['action_type']
        if 'aftersale_reason' in response:
            self.aftersale_reason = response['aftersale_reason']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_aftersale_id' in response:
            self.out_aftersale_id = response['out_aftersale_id']
        if 'status' in response:
            self.status = response['status']
        if 'type' in response:
            self.type = response['type']
