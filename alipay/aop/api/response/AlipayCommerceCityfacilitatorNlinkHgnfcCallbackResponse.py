#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCityfacilitatorNlinkHgnfcCallbackResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorNlinkHgnfcCallbackResponse, self).__init__()
        self._biz_scene = None
        self._can_retry = None
        self._cost_time = None
        self._data = None
        self._req_id = None
        self._ret_code = None
        self._ret_message = None
        self._service_id = None
        self._sub_ret_code = None
        self._sub_ret_message = None
        self._trace_id_info = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def can_retry(self):
        return self._can_retry

    @can_retry.setter
    def can_retry(self, value):
        self._can_retry = value
    @property
    def cost_time(self):
        return self._cost_time

    @cost_time.setter
    def cost_time(self, value):
        self._cost_time = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def req_id(self):
        return self._req_id

    @req_id.setter
    def req_id(self, value):
        self._req_id = value
    @property
    def ret_code(self):
        return self._ret_code

    @ret_code.setter
    def ret_code(self, value):
        self._ret_code = value
    @property
    def ret_message(self):
        return self._ret_message

    @ret_message.setter
    def ret_message(self, value):
        self._ret_message = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def sub_ret_code(self):
        return self._sub_ret_code

    @sub_ret_code.setter
    def sub_ret_code(self, value):
        self._sub_ret_code = value
    @property
    def sub_ret_message(self):
        return self._sub_ret_message

    @sub_ret_message.setter
    def sub_ret_message(self, value):
        self._sub_ret_message = value
    @property
    def trace_id_info(self):
        return self._trace_id_info

    @trace_id_info.setter
    def trace_id_info(self, value):
        self._trace_id_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorNlinkHgnfcCallbackResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'can_retry' in response:
            self.can_retry = response['can_retry']
        if 'cost_time' in response:
            self.cost_time = response['cost_time']
        if 'data' in response:
            self.data = response['data']
        if 'req_id' in response:
            self.req_id = response['req_id']
        if 'ret_code' in response:
            self.ret_code = response['ret_code']
        if 'ret_message' in response:
            self.ret_message = response['ret_message']
        if 'service_id' in response:
            self.service_id = response['service_id']
        if 'sub_ret_code' in response:
            self.sub_ret_code = response['sub_ret_code']
        if 'sub_ret_message' in response:
            self.sub_ret_message = response['sub_ret_message']
        if 'trace_id_info' in response:
            self.trace_id_info = response['trace_id_info']
