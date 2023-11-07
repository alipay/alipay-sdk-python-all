#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WalkPathMetaDataResult import WalkPathMetaDataResult


class AlipayUserSportsplayPathBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSportsplayPathBatchqueryResponse, self).__init__()
        self._response = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        if isinstance(value, WalkPathMetaDataResult):
            self._response = value
        else:
            self._response = WalkPathMetaDataResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserSportsplayPathBatchqueryResponse, self).parse_response_content(response_content)
        if 'response' in response:
            self.response = response['response']
