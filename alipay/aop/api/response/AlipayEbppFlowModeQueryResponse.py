#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppFlowModeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppFlowModeQueryResponse, self).__init__()
        self._activity_id = None
        self._ext_msg = None
        self._mobile = None
        self._product_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def ext_msg(self):
        return self._ext_msg

    @ext_msg.setter
    def ext_msg(self, value):
        self._ext_msg = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppFlowModeQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'ext_msg' in response:
            self.ext_msg = response['ext_msg']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'product_id' in response:
            self.product_id = response['product_id']
