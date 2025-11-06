#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UniOpenResItem import UniOpenResItem


class AlipayTradeSolutionprodUnifiedopenQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSolutionprodUnifiedopenQueryResponse, self).__init__()
        self._binding_logon_id = None
        self._fail_reason = None
        self._open_item_result_list = None
        self._out_biz_no = None
        self._uniopen_order_id = None
        self._uniopen_status = None

    @property
    def binding_logon_id(self):
        return self._binding_logon_id

    @binding_logon_id.setter
    def binding_logon_id(self, value):
        self._binding_logon_id = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def open_item_result_list(self):
        return self._open_item_result_list

    @open_item_result_list.setter
    def open_item_result_list(self, value):
        if isinstance(value, list):
            self._open_item_result_list = list()
            for i in value:
                if isinstance(i, UniOpenResItem):
                    self._open_item_result_list.append(i)
                else:
                    self._open_item_result_list.append(UniOpenResItem.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def uniopen_order_id(self):
        return self._uniopen_order_id

    @uniopen_order_id.setter
    def uniopen_order_id(self, value):
        self._uniopen_order_id = value
    @property
    def uniopen_status(self):
        return self._uniopen_status

    @uniopen_status.setter
    def uniopen_status(self, value):
        self._uniopen_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSolutionprodUnifiedopenQueryResponse, self).parse_response_content(response_content)
        if 'binding_logon_id' in response:
            self.binding_logon_id = response['binding_logon_id']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'open_item_result_list' in response:
            self.open_item_result_list = response['open_item_result_list']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'uniopen_order_id' in response:
            self.uniopen_order_id = response['uniopen_order_id']
        if 'uniopen_status' in response:
            self.uniopen_status = response['uniopen_status']
