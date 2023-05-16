#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsSubOrderEmploymentDigest import InsSubOrderEmploymentDigest


class AlipayInsSceneEmploymentGroupbatchQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEmploymentGroupbatchQueryResponse, self).__init__()
        self._batch_no = None
        self._out_biz_no = None
        self._status = None
        self._sub_order_info_list = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEmploymentGroupbatchQueryResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
        if 'sub_order_info_list' in response:
            self.sub_order_info_list = response['sub_order_info_list']
