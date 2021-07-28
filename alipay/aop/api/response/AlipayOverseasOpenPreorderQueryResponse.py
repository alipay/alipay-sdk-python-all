#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TuitionISVAgentInfoDTO import TuitionISVAgentInfoDTO
from alipay.aop.api.domain.TuitionISVAmountInfoDTO import TuitionISVAmountInfoDTO
from alipay.aop.api.domain.TuitionISVResponsePaymentInfoDTO import TuitionISVResponsePaymentInfoDTO
from alipay.aop.api.domain.TuitionISVAmountInfoDTO import TuitionISVAmountInfoDTO
from alipay.aop.api.domain.TuitionISVResult import TuitionISVResult
from alipay.aop.api.domain.TuitionISVOrderStatusDTO import TuitionISVOrderStatusDTO
from alipay.aop.api.domain.TuitionISVStudentInfoDTO import TuitionISVStudentInfoDTO


class AlipayOverseasOpenPreorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenPreorderQueryResponse, self).__init__()
        self._agent_info = None
        self._payment_amount = None
        self._payment_info = None
        self._pre_order_id = None
        self._refund_amount = None
        self._result = None
        self._status = None
        self._status_code = None
        self._student_info = None

    @property
    def agent_info(self):
        return self._agent_info

    @agent_info.setter
    def agent_info(self, value):
        if isinstance(value, TuitionISVAgentInfoDTO):
            self._agent_info = value
        else:
            self._agent_info = TuitionISVAgentInfoDTO.from_alipay_dict(value)
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        if isinstance(value, TuitionISVAmountInfoDTO):
            self._payment_amount = value
        else:
            self._payment_amount = TuitionISVAmountInfoDTO.from_alipay_dict(value)
    @property
    def payment_info(self):
        return self._payment_info

    @payment_info.setter
    def payment_info(self, value):
        if isinstance(value, TuitionISVResponsePaymentInfoDTO):
            self._payment_info = value
        else:
            self._payment_info = TuitionISVResponsePaymentInfoDTO.from_alipay_dict(value)
    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        if isinstance(value, TuitionISVAmountInfoDTO):
            self._refund_amount = value
        else:
            self._refund_amount = TuitionISVAmountInfoDTO.from_alipay_dict(value)
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, TuitionISVResult):
            self._result = value
        else:
            self._result = TuitionISVResult.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, TuitionISVOrderStatusDTO):
            self._status = value
        else:
            self._status = TuitionISVOrderStatusDTO.from_alipay_dict(value)
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    @property
    def student_info(self):
        return self._student_info

    @student_info.setter
    def student_info(self, value):
        if isinstance(value, TuitionISVStudentInfoDTO):
            self._student_info = value
        else:
            self._student_info = TuitionISVStudentInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasOpenPreorderQueryResponse, self).parse_response_content(response_content)
        if 'agent_info' in response:
            self.agent_info = response['agent_info']
        if 'payment_amount' in response:
            self.payment_amount = response['payment_amount']
        if 'payment_info' in response:
            self.payment_info = response['payment_info']
        if 'pre_order_id' in response:
            self.pre_order_id = response['pre_order_id']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'result' in response:
            self.result = response['result']
        if 'status' in response:
            self.status = response['status']
        if 'status_code' in response:
            self.status_code = response['status_code']
        if 'student_info' in response:
            self.student_info = response['student_info']
