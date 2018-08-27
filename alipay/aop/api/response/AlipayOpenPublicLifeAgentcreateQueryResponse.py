#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicLifeAgentcreateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicLifeAgentcreateQueryResponse, self).__init__()
        self._life_app_id = None
        self._merchant_pid = None
        self._order_status_biz_desc = None
        self._out_biz_no = None
        self._refused_reason = None

    @property
    def life_app_id(self):
        return self._life_app_id

    @life_app_id.setter
    def life_app_id(self, value):
        self._life_app_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def order_status_biz_desc(self):
        return self._order_status_biz_desc

    @order_status_biz_desc.setter
    def order_status_biz_desc(self, value):
        self._order_status_biz_desc = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def refused_reason(self):
        return self._refused_reason

    @refused_reason.setter
    def refused_reason(self, value):
        self._refused_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicLifeAgentcreateQueryResponse, self).parse_response_content(response_content)
        if 'life_app_id' in response:
            self.life_app_id = response['life_app_id']
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
        if 'order_status_biz_desc' in response:
            self.order_status_biz_desc = response['order_status_biz_desc']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'refused_reason' in response:
            self.refused_reason = response['refused_reason']
