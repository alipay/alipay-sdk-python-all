#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryApplyflowQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryApplyflowQueryResponse, self).__init__()
        self._ability_code = None
        self._apply_flow_no = None
        self._bill_key = None
        self._biz_inst = None
        self._biz_type = None
        self._gmt_create = None
        self._gmt_modified = None
        self._org_result_code = None
        self._out_apply_no = None
        self._result_code = None
        self._result_context = None
        self._result_msg = None
        self._status = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def apply_flow_no(self):
        return self._apply_flow_no

    @apply_flow_no.setter
    def apply_flow_no(self, value):
        self._apply_flow_no = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def biz_inst(self):
        return self._biz_inst

    @biz_inst.setter
    def biz_inst(self, value):
        self._biz_inst = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def org_result_code(self):
        return self._org_result_code

    @org_result_code.setter
    def org_result_code(self, value):
        self._org_result_code = value
    @property
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_context(self):
        return self._result_context

    @result_context.setter
    def result_context(self, value):
        self._result_context = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryApplyflowQueryResponse, self).parse_response_content(response_content)
        if 'ability_code' in response:
            self.ability_code = response['ability_code']
        if 'apply_flow_no' in response:
            self.apply_flow_no = response['apply_flow_no']
        if 'bill_key' in response:
            self.bill_key = response['bill_key']
        if 'biz_inst' in response:
            self.biz_inst = response['biz_inst']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'org_result_code' in response:
            self.org_result_code = response['org_result_code']
        if 'out_apply_no' in response:
            self.out_apply_no = response['out_apply_no']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_context' in response:
            self.result_context = response['result_context']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'status' in response:
            self.status = response['status']
