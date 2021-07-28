#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OuterAttachment import OuterAttachment


class AlipayDataDataserviceAdPrincipalQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdPrincipalQueryResponse, self).__init__()
        self._alipay_pid = None
        self._attachment_list = None
        self._principal_id = None
        self._refuse_reason = None
        self._status = None
        self._trade_id = None

    @property
    def alipay_pid(self):
        return self._alipay_pid

    @alipay_pid.setter
    def alipay_pid(self, value):
        self._alipay_pid = value
    @property
    def attachment_list(self):
        return self._attachment_list

    @attachment_list.setter
    def attachment_list(self, value):
        if isinstance(value, list):
            self._attachment_list = list()
            for i in value:
                if isinstance(i, OuterAttachment):
                    self._attachment_list.append(i)
                else:
                    self._attachment_list.append(OuterAttachment.from_alipay_dict(i))
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdPrincipalQueryResponse, self).parse_response_content(response_content)
        if 'alipay_pid' in response:
            self.alipay_pid = response['alipay_pid']
        if 'attachment_list' in response:
            self.attachment_list = response['attachment_list']
        if 'principal_id' in response:
            self.principal_id = response['principal_id']
        if 'refuse_reason' in response:
            self.refuse_reason = response['refuse_reason']
        if 'status' in response:
            self.status = response['status']
        if 'trade_id' in response:
            self.trade_id = response['trade_id']
