#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiPcreditbenefitFuncardassertReturnResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiPcreditbenefitFuncardassertReturnResponse, self).__init__()
        self._actual_point = None
        self._biz_no = None
        self._decrease_status = None
        self._order_id = None

    @property
    def actual_point(self):
        return self._actual_point

    @actual_point.setter
    def actual_point(self, value):
        self._actual_point = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def decrease_status(self):
        return self._decrease_status

    @decrease_status.setter
    def decrease_status(self, value):
        self._decrease_status = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiPcreditbenefitFuncardassertReturnResponse, self).parse_response_content(response_content)
        if 'actual_point' in response:
            self.actual_point = response['actual_point']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'decrease_status' in response:
            self.decrease_status = response['decrease_status']
        if 'order_id' in response:
            self.order_id = response['order_id']
