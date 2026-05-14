#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNordermaterialsapplyMaterialsrecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsapplyMaterialsrecordQueryResponse, self).__init__()
        self._record_id = None
        self._reject_reason = None
        self._remain_retry_count = None
        self._status = None

    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def remain_retry_count(self):
        return self._remain_retry_count

    @remain_retry_count.setter
    def remain_retry_count(self, value):
        self._remain_retry_count = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsapplyMaterialsrecordQueryResponse, self).parse_response_content(response_content)
        if 'record_id' in response:
            self.record_id = response['record_id']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'remain_retry_count' in response:
            self.remain_retry_count = response['remain_retry_count']
        if 'status' in response:
            self.status = response['status']
