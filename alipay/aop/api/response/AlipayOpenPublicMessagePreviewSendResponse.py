#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MsgSendErrorData import MsgSendErrorData


class AlipayOpenPublicMessagePreviewSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicMessagePreviewSendResponse, self).__init__()
        self._error_datas = None

    @property
    def error_datas(self):
        return self._error_datas

    @error_datas.setter
    def error_datas(self, value):
        if isinstance(value, list):
            self._error_datas = list()
            for i in value:
                if isinstance(i, MsgSendErrorData):
                    self._error_datas.append(i)
                else:
                    self._error_datas.append(MsgSendErrorData.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicMessagePreviewSendResponse, self).parse_response_content(response_content)
        if 'error_datas' in response:
            self.error_datas = response['error_datas']
