#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceBizinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceBizinfoSyncResponse, self).__init__()
        self._biz_info_id = None
        self._biz_unit_id = None
        self._info_id = None
        self._sec_status = None

    @property
    def biz_info_id(self):
        return self._biz_info_id

    @biz_info_id.setter
    def biz_info_id(self, value):
        self._biz_info_id = value
    @property
    def biz_unit_id(self):
        return self._biz_unit_id

    @biz_unit_id.setter
    def biz_unit_id(self, value):
        self._biz_unit_id = value
    @property
    def info_id(self):
        return self._info_id

    @info_id.setter
    def info_id(self, value):
        self._info_id = value
    @property
    def sec_status(self):
        return self._sec_status

    @sec_status.setter
    def sec_status(self, value):
        self._sec_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceBizinfoSyncResponse, self).parse_response_content(response_content)
        if 'biz_info_id' in response:
            self.biz_info_id = response['biz_info_id']
        if 'biz_unit_id' in response:
            self.biz_unit_id = response['biz_unit_id']
        if 'info_id' in response:
            self.info_id = response['info_id']
        if 'sec_status' in response:
            self.sec_status = response['sec_status']
