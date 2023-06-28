#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsSubOrderEmploymentDigest import InsSubOrderEmploymentDigest


class AlipayInsSceneCommonGroupendorseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneCommonGroupendorseQueryResponse, self).__init__()
        self._endorse_fee = None
        self._out_biz_no = None
        self._status = None
        self._sub_order_count = None
        self._sub_order_info_list = None
        self._summary_endorse_order_no = None
        self._summary_premium = None

    @property
    def endorse_fee(self):
        return self._endorse_fee

    @endorse_fee.setter
    def endorse_fee(self, value):
        self._endorse_fee = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_order_count(self):
        return self._sub_order_count

    @sub_order_count.setter
    def sub_order_count(self, value):
        self._sub_order_count = value
    @property
    def sub_order_info_list(self):
        return self._sub_order_info_list

    @sub_order_info_list.setter
    def sub_order_info_list(self, value):
        if isinstance(value, list):
            self._sub_order_info_list = list()
            for i in value:
                if isinstance(i, InsSubOrderEmploymentDigest):
                    self._sub_order_info_list.append(i)
                else:
                    self._sub_order_info_list.append(InsSubOrderEmploymentDigest.from_alipay_dict(i))
    @property
    def summary_endorse_order_no(self):
        return self._summary_endorse_order_no

    @summary_endorse_order_no.setter
    def summary_endorse_order_no(self, value):
        self._summary_endorse_order_no = value
    @property
    def summary_premium(self):
        return self._summary_premium

    @summary_premium.setter
    def summary_premium(self, value):
        self._summary_premium = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneCommonGroupendorseQueryResponse, self).parse_response_content(response_content)
        if 'endorse_fee' in response:
            self.endorse_fee = response['endorse_fee']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
        if 'sub_order_count' in response:
            self.sub_order_count = response['sub_order_count']
        if 'sub_order_info_list' in response:
            self.sub_order_info_list = response['sub_order_info_list']
        if 'summary_endorse_order_no' in response:
            self.summary_endorse_order_no = response['summary_endorse_order_no']
        if 'summary_premium' in response:
            self.summary_premium = response['summary_premium']
