#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTerminalEdgecloudSimcardNetflowmonitorSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTerminalEdgecloudSimcardNetflowmonitorSyncResponse, self).__init__()
        self._biz_date = None
        self._biz_date_file_seq_id = None
        self._record_detail_id = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_date_file_seq_id(self):
        return self._biz_date_file_seq_id

    @biz_date_file_seq_id.setter
    def biz_date_file_seq_id(self, value):
        self._biz_date_file_seq_id = value
    @property
    def record_detail_id(self):
        return self._record_detail_id

    @record_detail_id.setter
    def record_detail_id(self, value):
        self._record_detail_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTerminalEdgecloudSimcardNetflowmonitorSyncResponse, self).parse_response_content(response_content)
        if 'biz_date' in response:
            self.biz_date = response['biz_date']
        if 'biz_date_file_seq_id' in response:
            self.biz_date_file_seq_id = response['biz_date_file_seq_id']
        if 'record_detail_id' in response:
            self.record_detail_id = response['record_detail_id']
