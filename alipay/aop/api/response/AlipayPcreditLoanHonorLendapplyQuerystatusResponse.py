#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanHonorLendapplyQuerystatusResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorLendapplyQuerystatusResponse, self).__init__()
        self._apply_status = None
        self._apply_time = None
        self._institution_names = None
        self._out_order_no = None
        self._refuse_code = None
        self._refuse_msg = None
        self._refuse_msg_data = None

    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def institution_names(self):
        return self._institution_names

    @institution_names.setter
    def institution_names(self, value):
        self._institution_names = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def refuse_msg_data(self):
        return self._refuse_msg_data

    @refuse_msg_data.setter
    def refuse_msg_data(self, value):
        self._refuse_msg_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorLendapplyQuerystatusResponse, self).parse_response_content(response_content)
        if 'apply_status' in response:
            self.apply_status = response['apply_status']
        if 'apply_time' in response:
            self.apply_time = response['apply_time']
        if 'institution_names' in response:
            self.institution_names = response['institution_names']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'refuse_msg_data' in response:
            self.refuse_msg_data = response['refuse_msg_data']
