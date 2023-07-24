#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpCreditLinkCreateQueryDataInfo import EpCreditLinkCreateQueryDataInfo


class ZhimaCreditEpCreditlinkCollectCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCreditlinkCollectCreateResponse, self).__init__()
        self._content = None
        self._data_result = None
        self._data_status = None
        self._data_type = None
        self._merchant_request_id = None
        self._product_code = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, EpCreditLinkCreateQueryDataInfo):
            self._content = value
        else:
            self._content = EpCreditLinkCreateQueryDataInfo.from_alipay_dict(value)
    @property
    def data_result(self):
        return self._data_result

    @data_result.setter
    def data_result(self, value):
        self._data_result = value
    @property
    def data_status(self):
        return self._data_status

    @data_status.setter
    def data_status(self, value):
        self._data_status = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def merchant_request_id(self):
        return self._merchant_request_id

    @merchant_request_id.setter
    def merchant_request_id(self, value):
        self._merchant_request_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCreditlinkCollectCreateResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'data_result' in response:
            self.data_result = response['data_result']
        if 'data_status' in response:
            self.data_status = response['data_status']
        if 'data_type' in response:
            self.data_type = response['data_type']
        if 'merchant_request_id' in response:
            self.merchant_request_id = response['merchant_request_id']
        if 'product_code' in response:
            self.product_code = response['product_code']
