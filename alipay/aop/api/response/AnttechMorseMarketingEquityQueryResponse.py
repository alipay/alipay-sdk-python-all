#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherResultInfo import VoucherResultInfo


class AnttechMorseMarketingEquityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingEquityQueryResponse, self).__init__()
        self._out_biz_no = None
        self._resource_id = None
        self._voucher_result_info_list = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def voucher_result_info_list(self):
        return self._voucher_result_info_list

    @voucher_result_info_list.setter
    def voucher_result_info_list(self, value):
        if isinstance(value, list):
            self._voucher_result_info_list = list()
            for i in value:
                if isinstance(i, VoucherResultInfo):
                    self._voucher_result_info_list.append(i)
                else:
                    self._voucher_result_info_list.append(VoucherResultInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingEquityQueryResponse, self).parse_response_content(response_content)
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'resource_id' in response:
            self.resource_id = response['resource_id']
        if 'voucher_result_info_list' in response:
            self.voucher_result_info_list = response['voucher_result_info_list']
