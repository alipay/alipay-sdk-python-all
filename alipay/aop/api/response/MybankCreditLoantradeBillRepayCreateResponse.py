#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RefuseVo import RefuseVo


class MybankCreditLoantradeBillRepayCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeBillRepayCreateResponse, self).__init__()
        self._ev_seq_no = None
        self._refuse_msg = None
        self._success = None

    @property
    def ev_seq_no(self):
        return self._ev_seq_no

    @ev_seq_no.setter
    def ev_seq_no(self, value):
        self._ev_seq_no = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        if isinstance(value, RefuseVo):
            self._refuse_msg = value
        else:
            self._refuse_msg = RefuseVo.from_alipay_dict(value)
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeBillRepayCreateResponse, self).parse_response_content(response_content)
        if 'ev_seq_no' in response:
            self.ev_seq_no = response['ev_seq_no']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'success' in response:
            self.success = response['success']
