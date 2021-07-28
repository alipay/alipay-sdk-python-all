#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AntMemberBenefitInfo import AntMemberBenefitInfo


class AlipayUserAccountNewbieBenefitConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountNewbieBenefitConsultResponse, self).__init__()
        self._alipay_logon_id = None
        self._benefit_info = None
        self._result_code = None
        self._result_desc = None
        self._success = None

    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def benefit_info(self):
        return self._benefit_info

    @benefit_info.setter
    def benefit_info(self, value):
        if isinstance(value, AntMemberBenefitInfo):
            self._benefit_info = value
        else:
            self._benefit_info = AntMemberBenefitInfo.from_alipay_dict(value)
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountNewbieBenefitConsultResponse, self).parse_response_content(response_content)
        if 'alipay_logon_id' in response:
            self.alipay_logon_id = response['alipay_logon_id']
        if 'benefit_info' in response:
            self.benefit_info = response['benefit_info']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
        if 'success' in response:
            self.success = response['success']
