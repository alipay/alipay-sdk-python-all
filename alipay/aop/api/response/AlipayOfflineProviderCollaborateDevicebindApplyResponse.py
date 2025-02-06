#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderCollaborateDevicebindApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCollaborateDevicebindApplyResponse, self).__init__()
        self._activity_info_url = None
        self._device_bind_status = None
        self._device_remark = None
        self._device_sn = None
        self._in_white_list = None
        self._out_biz_no = None
        self._sales_entry_order_id = None
        self._solution_id = None

    @property
    def activity_info_url(self):
        return self._activity_info_url

    @activity_info_url.setter
    def activity_info_url(self, value):
        self._activity_info_url = value
    @property
    def device_bind_status(self):
        return self._device_bind_status

    @device_bind_status.setter
    def device_bind_status(self, value):
        self._device_bind_status = value
    @property
    def device_remark(self):
        return self._device_remark

    @device_remark.setter
    def device_remark(self, value):
        self._device_remark = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def in_white_list(self):
        return self._in_white_list

    @in_white_list.setter
    def in_white_list(self, value):
        self._in_white_list = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sales_entry_order_id(self):
        return self._sales_entry_order_id

    @sales_entry_order_id.setter
    def sales_entry_order_id(self, value):
        self._sales_entry_order_id = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCollaborateDevicebindApplyResponse, self).parse_response_content(response_content)
        if 'activity_info_url' in response:
            self.activity_info_url = response['activity_info_url']
        if 'device_bind_status' in response:
            self.device_bind_status = response['device_bind_status']
        if 'device_remark' in response:
            self.device_remark = response['device_remark']
        if 'device_sn' in response:
            self.device_sn = response['device_sn']
        if 'in_white_list' in response:
            self.in_white_list = response['in_white_list']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'sales_entry_order_id' in response:
            self.sales_entry_order_id = response['sales_entry_order_id']
        if 'solution_id' in response:
            self.solution_id = response['solution_id']
