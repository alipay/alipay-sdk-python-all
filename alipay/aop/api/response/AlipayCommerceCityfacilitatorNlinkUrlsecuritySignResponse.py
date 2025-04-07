#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCityfacilitatorNlinkUrlsecuritySignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorNlinkUrlsecuritySignResponse, self).__init__()
        self._cost_time = None
        self._msg_info = None
        self._server_sign = None
        self._trace_id_info = None
        self._url = None

    @property
    def cost_time(self):
        return self._cost_time

    @cost_time.setter
    def cost_time(self, value):
        self._cost_time = value
    @property
    def msg_info(self):
        return self._msg_info

    @msg_info.setter
    def msg_info(self, value):
        self._msg_info = value
    @property
    def server_sign(self):
        return self._server_sign

    @server_sign.setter
    def server_sign(self, value):
        self._server_sign = value
    @property
    def trace_id_info(self):
        return self._trace_id_info

    @trace_id_info.setter
    def trace_id_info(self, value):
        self._trace_id_info = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorNlinkUrlsecuritySignResponse, self).parse_response_content(response_content)
        if 'cost_time' in response:
            self.cost_time = response['cost_time']
        if 'msg_info' in response:
            self.msg_info = response['msg_info']
        if 'server_sign' in response:
            self.server_sign = response['server_sign']
        if 'trace_id_info' in response:
            self.trace_id_info = response['trace_id_info']
        if 'url' in response:
            self.url = response['url']
