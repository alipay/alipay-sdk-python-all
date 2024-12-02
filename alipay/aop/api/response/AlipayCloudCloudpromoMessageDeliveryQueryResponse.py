#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CallRecordDetail import CallRecordDetail


class AlipayCloudCloudpromoMessageDeliveryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMessageDeliveryQueryResponse, self).__init__()
        self._call_record_details = None
        self._record_id = None
        self._status = None

    @property
    def call_record_details(self):
        return self._call_record_details

    @call_record_details.setter
    def call_record_details(self, value):
        if isinstance(value, list):
            self._call_record_details = list()
            for i in value:
                if isinstance(i, CallRecordDetail):
                    self._call_record_details.append(i)
                else:
                    self._call_record_details.append(CallRecordDetail.from_alipay_dict(i))
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMessageDeliveryQueryResponse, self).parse_response_content(response_content)
        if 'call_record_details' in response:
            self.call_record_details = response['call_record_details']
        if 'record_id' in response:
            self.record_id = response['record_id']
        if 'status' in response:
            self.status = response['status']
