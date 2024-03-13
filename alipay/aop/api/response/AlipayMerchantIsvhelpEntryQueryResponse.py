#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIsvhelpEntryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIsvhelpEntryQueryResponse, self).__init__()
        self._alipay_logon_id = None
        self._biz_status = None
        self._certify_link = None
        self._external_id = None
        self._failed_reason = None

    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def certify_link(self):
        return self._certify_link

    @certify_link.setter
    def certify_link(self, value):
        self._certify_link = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def failed_reason(self):
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, value):
        if isinstance(value, list):
            self._failed_reason = list()
            for i in value:
                self._failed_reason.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIsvhelpEntryQueryResponse, self).parse_response_content(response_content)
        if 'alipay_logon_id' in response:
            self.alipay_logon_id = response['alipay_logon_id']
        if 'biz_status' in response:
            self.biz_status = response['biz_status']
        if 'certify_link' in response:
            self.certify_link = response['certify_link']
        if 'external_id' in response:
            self.external_id = response['external_id']
        if 'failed_reason' in response:
            self.failed_reason = response['failed_reason']
