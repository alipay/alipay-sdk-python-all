#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FqQrCodeExtendParams import FqQrCodeExtendParams


class AlipayPcreditHuabeiIsvOpeninfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiIsvOpeninfoQueryResponse, self).__init__()
        self._disclaimer = None
        self._ext_info = None
        self._isv_marketing_copy = None
        self._merchant_name = None
        self._out_request_no = None
        self._smid = None
        self._store_id = None

    @property
    def disclaimer(self):
        return self._disclaimer

    @disclaimer.setter
    def disclaimer(self, value):
        self._disclaimer = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, FqQrCodeExtendParams):
            self._ext_info = value
        else:
            self._ext_info = FqQrCodeExtendParams.from_alipay_dict(value)
    @property
    def isv_marketing_copy(self):
        return self._isv_marketing_copy

    @isv_marketing_copy.setter
    def isv_marketing_copy(self, value):
        self._isv_marketing_copy = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiIsvOpeninfoQueryResponse, self).parse_response_content(response_content)
        if 'disclaimer' in response:
            self.disclaimer = response['disclaimer']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'isv_marketing_copy' in response:
            self.isv_marketing_copy = response['isv_marketing_copy']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'smid' in response:
            self.smid = response['smid']
        if 'store_id' in response:
            self.store_id = response['store_id']
