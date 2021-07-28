#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotSdarttoolMessageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotSdarttoolMessageQueryResponse, self).__init__()
        self._consume_err_code = None
        self._consume_err_msg = None
        self._consume_state = None
        self._deliver_cnt = None
        self._deliver_status = None
        self._last_deliver_at = None
        self._msg_ack_time = None
        self._msg_bida = None
        self._msg_expire_time = None
        self._msg_gmt_create = None
        self._msg_priority = None

    @property
    def consume_err_code(self):
        return self._consume_err_code

    @consume_err_code.setter
    def consume_err_code(self, value):
        self._consume_err_code = value
    @property
    def consume_err_msg(self):
        return self._consume_err_msg

    @consume_err_msg.setter
    def consume_err_msg(self, value):
        self._consume_err_msg = value
    @property
    def consume_state(self):
        return self._consume_state

    @consume_state.setter
    def consume_state(self, value):
        self._consume_state = value
    @property
    def deliver_cnt(self):
        return self._deliver_cnt

    @deliver_cnt.setter
    def deliver_cnt(self, value):
        self._deliver_cnt = value
    @property
    def deliver_status(self):
        return self._deliver_status

    @deliver_status.setter
    def deliver_status(self, value):
        self._deliver_status = value
    @property
    def last_deliver_at(self):
        return self._last_deliver_at

    @last_deliver_at.setter
    def last_deliver_at(self, value):
        self._last_deliver_at = value
    @property
    def msg_ack_time(self):
        return self._msg_ack_time

    @msg_ack_time.setter
    def msg_ack_time(self, value):
        self._msg_ack_time = value
    @property
    def msg_bida(self):
        return self._msg_bida

    @msg_bida.setter
    def msg_bida(self, value):
        self._msg_bida = value
    @property
    def msg_expire_time(self):
        return self._msg_expire_time

    @msg_expire_time.setter
    def msg_expire_time(self, value):
        self._msg_expire_time = value
    @property
    def msg_gmt_create(self):
        return self._msg_gmt_create

    @msg_gmt_create.setter
    def msg_gmt_create(self, value):
        self._msg_gmt_create = value
    @property
    def msg_priority(self):
        return self._msg_priority

    @msg_priority.setter
    def msg_priority(self, value):
        self._msg_priority = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotSdarttoolMessageQueryResponse, self).parse_response_content(response_content)
        if 'consume_err_code' in response:
            self.consume_err_code = response['consume_err_code']
        if 'consume_err_msg' in response:
            self.consume_err_msg = response['consume_err_msg']
        if 'consume_state' in response:
            self.consume_state = response['consume_state']
        if 'deliver_cnt' in response:
            self.deliver_cnt = response['deliver_cnt']
        if 'deliver_status' in response:
            self.deliver_status = response['deliver_status']
        if 'last_deliver_at' in response:
            self.last_deliver_at = response['last_deliver_at']
        if 'msg_ack_time' in response:
            self.msg_ack_time = response['msg_ack_time']
        if 'msg_bida' in response:
            self.msg_bida = response['msg_bida']
        if 'msg_expire_time' in response:
            self.msg_expire_time = response['msg_expire_time']
        if 'msg_gmt_create' in response:
            self.msg_gmt_create = response['msg_gmt_create']
        if 'msg_priority' in response:
            self.msg_priority = response['msg_priority']
