#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherRec import VoucherRec


class AlipayDataDataserviceShoppingmallrecVoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceShoppingmallrecVoucherQueryResponse, self).__init__()
        self._recommend_id = None
        self._request_id = None
        self._voucher_recommend_list = None

    @property
    def recommend_id(self):
        return self._recommend_id

    @recommend_id.setter
    def recommend_id(self, value):
        self._recommend_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def voucher_recommend_list(self):
        return self._voucher_recommend_list

    @voucher_recommend_list.setter
    def voucher_recommend_list(self, value):
        if isinstance(value, list):
            self._voucher_recommend_list = list()
            for i in value:
                if isinstance(i, VoucherRec):
                    self._voucher_recommend_list.append(i)
                else:
                    self._voucher_recommend_list.append(VoucherRec.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceShoppingmallrecVoucherQueryResponse, self).parse_response_content(response_content)
        if 'recommend_id' in response:
            self.recommend_id = response['recommend_id']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'voucher_recommend_list' in response:
            self.voucher_recommend_list = response['voucher_recommend_list']
