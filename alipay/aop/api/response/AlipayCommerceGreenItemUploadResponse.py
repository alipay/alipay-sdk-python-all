#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QrCodeOperationLog import QrCodeOperationLog


class AlipayCommerceGreenItemUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceGreenItemUploadResponse, self).__init__()
        self._failed_qr_code_log_list = None

    @property
    def failed_qr_code_log_list(self):
        return self._failed_qr_code_log_list

    @failed_qr_code_log_list.setter
    def failed_qr_code_log_list(self, value):
        if isinstance(value, list):
            self._failed_qr_code_log_list = list()
            for i in value:
                if isinstance(i, QrCodeOperationLog):
                    self._failed_qr_code_log_list.append(i)
                else:
                    self._failed_qr_code_log_list.append(QrCodeOperationLog.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceGreenItemUploadResponse, self).parse_response_content(response_content)
        if 'failed_qr_code_log_list' in response:
            self.failed_qr_code_log_list = response['failed_qr_code_log_list']
