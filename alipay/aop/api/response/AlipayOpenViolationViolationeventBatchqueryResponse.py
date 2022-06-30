#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ViolationEvent import ViolationEvent


class AlipayOpenViolationViolationeventBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenViolationViolationeventBatchqueryResponse, self).__init__()
        self._violation_record_infos = None

    @property
    def violation_record_infos(self):
        return self._violation_record_infos

    @violation_record_infos.setter
    def violation_record_infos(self, value):
        if isinstance(value, ViolationEvent):
            self._violation_record_infos = value
        else:
            self._violation_record_infos = ViolationEvent.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenViolationViolationeventBatchqueryResponse, self).parse_response_content(response_content)
        if 'violation_record_infos' in response:
            self.violation_record_infos = response['violation_record_infos']
