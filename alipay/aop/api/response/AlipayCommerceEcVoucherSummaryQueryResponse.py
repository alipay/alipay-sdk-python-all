#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcVoucherInfo import EcVoucherInfo


class AlipayCommerceEcVoucherSummaryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcVoucherSummaryQueryResponse, self).__init__()
        self._voucher_info_list = None

    @property
    def voucher_info_list(self):
        return self._voucher_info_list

    @voucher_info_list.setter
    def voucher_info_list(self, value):
        if isinstance(value, list):
            self._voucher_info_list = list()
            for i in value:
                if isinstance(i, EcVoucherInfo):
                    self._voucher_info_list.append(i)
                else:
                    self._voucher_info_list.append(EcVoucherInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcVoucherSummaryQueryResponse, self).parse_response_content(response_content)
        if 'voucher_info_list' in response:
            self.voucher_info_list = response['voucher_info_list']
