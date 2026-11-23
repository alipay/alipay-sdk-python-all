#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalAicsDtcontrolVisitorqueueQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAicsDtcontrolVisitorqueueQueryResponse, self).__init__()
        self._order_position = None
        self._queue_status = None
        self._seat_id = None
        self._seat_type = None
        self._service_uniq_code = None
        self._skill_group_id = None
        self._skill_group_type = None

    @property
    def order_position(self):
        return self._order_position

    @order_position.setter
    def order_position(self, value):
        self._order_position = value
    @property
    def queue_status(self):
        return self._queue_status

    @queue_status.setter
    def queue_status(self, value):
        self._queue_status = value
    @property
    def seat_id(self):
        return self._seat_id

    @seat_id.setter
    def seat_id(self, value):
        self._seat_id = value
    @property
    def seat_type(self):
        return self._seat_type

    @seat_type.setter
    def seat_type(self, value):
        self._seat_type = value
    @property
    def service_uniq_code(self):
        return self._service_uniq_code

    @service_uniq_code.setter
    def service_uniq_code(self, value):
        self._service_uniq_code = value
    @property
    def skill_group_id(self):
        return self._skill_group_id

    @skill_group_id.setter
    def skill_group_id(self, value):
        self._skill_group_id = value
    @property
    def skill_group_type(self):
        return self._skill_group_type

    @skill_group_type.setter
    def skill_group_type(self, value):
        self._skill_group_type = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAicsDtcontrolVisitorqueueQueryResponse, self).parse_response_content(response_content)
        if 'order_position' in response:
            self.order_position = response['order_position']
        if 'queue_status' in response:
            self.queue_status = response['queue_status']
        if 'seat_id' in response:
            self.seat_id = response['seat_id']
        if 'seat_type' in response:
            self.seat_type = response['seat_type']
        if 'service_uniq_code' in response:
            self.service_uniq_code = response['service_uniq_code']
        if 'skill_group_id' in response:
            self.skill_group_id = response['skill_group_id']
        if 'skill_group_type' in response:
            self.skill_group_type = response['skill_group_type']
