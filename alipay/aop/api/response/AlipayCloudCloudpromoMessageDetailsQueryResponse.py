#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SmsSendDetail import SmsSendDetail


class AlipayCloudCloudpromoMessageDetailsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMessageDetailsQueryResponse, self).__init__()
        self._sms_send_detail = None
        self._success_count = None
        self._total_count = None

    @property
    def sms_send_detail(self):
        return self._sms_send_detail

    @sms_send_detail.setter
    def sms_send_detail(self, value):
        if isinstance(value, list):
            self._sms_send_detail = list()
            for i in value:
                if isinstance(i, SmsSendDetail):
                    self._sms_send_detail.append(i)
                else:
                    self._sms_send_detail.append(SmsSendDetail.from_alipay_dict(i))
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMessageDetailsQueryResponse, self).parse_response_content(response_content)
        if 'sms_send_detail' in response:
            self.sms_send_detail = response['sms_send_detail']
        if 'success_count' in response:
            self.success_count = response['success_count']
        if 'total_count' in response:
            self.total_count = response['total_count']
