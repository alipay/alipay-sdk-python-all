#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsGroupOrderBatchDigest import InsGroupOrderBatchDigest


class AlipayInsSceneCommonGrouporderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneCommonGrouporderQueryResponse, self).__init__()
        self._batch_info_list = None
        self._out_biz_no = None
        self._sub_order_count = None
        self._summary_order_premium = None

    @property
    def batch_info_list(self):
        return self._batch_info_list

    @batch_info_list.setter
    def batch_info_list(self, value):
        if isinstance(value, list):
            self._batch_info_list = list()
            for i in value:
                if isinstance(i, InsGroupOrderBatchDigest):
                    self._batch_info_list.append(i)
                else:
                    self._batch_info_list.append(InsGroupOrderBatchDigest.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sub_order_count(self):
        return self._sub_order_count

    @sub_order_count.setter
    def sub_order_count(self, value):
        self._sub_order_count = value
    @property
    def summary_order_premium(self):
        return self._summary_order_premium

    @summary_order_premium.setter
    def summary_order_premium(self, value):
        self._summary_order_premium = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneCommonGrouporderQueryResponse, self).parse_response_content(response_content)
        if 'batch_info_list' in response:
            self.batch_info_list = response['batch_info_list']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'sub_order_count' in response:
            self.sub_order_count = response['sub_order_count']
        if 'summary_order_premium' in response:
            self.summary_order_premium = response['summary_order_premium']
