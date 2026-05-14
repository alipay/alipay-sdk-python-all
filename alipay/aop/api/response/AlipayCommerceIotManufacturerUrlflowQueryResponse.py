#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FailSnDetail import FailSnDetail


class AlipayCommerceIotManufacturerUrlflowQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotManufacturerUrlflowQueryResponse, self).__init__()
        self._fail_sn_detail_list = None
        self._flow_no = None
        self._out_biz_no = None
        self._status = None

    @property
    def fail_sn_detail_list(self):
        return self._fail_sn_detail_list

    @fail_sn_detail_list.setter
    def fail_sn_detail_list(self, value):
        if isinstance(value, list):
            self._fail_sn_detail_list = list()
            for i in value:
                if isinstance(i, FailSnDetail):
                    self._fail_sn_detail_list.append(i)
                else:
                    self._fail_sn_detail_list.append(FailSnDetail.from_alipay_dict(i))
    @property
    def flow_no(self):
        return self._flow_no

    @flow_no.setter
    def flow_no(self, value):
        self._flow_no = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotManufacturerUrlflowQueryResponse, self).parse_response_content(response_content)
        if 'fail_sn_detail_list' in response:
            self.fail_sn_detail_list = response['fail_sn_detail_list']
        if 'flow_no' in response:
            self.flow_no = response['flow_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
