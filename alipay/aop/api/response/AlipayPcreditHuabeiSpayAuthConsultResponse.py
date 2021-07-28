#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MultiStagePayInfo import MultiStagePayInfo


class AlipayPcreditHuabeiSpayAuthConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiSpayAuthConsultResponse, self).__init__()
        self._auth_approved = None
        self._multi_stage_pay_info = None
        self._refuse_desc = None

    @property
    def auth_approved(self):
        return self._auth_approved

    @auth_approved.setter
    def auth_approved(self, value):
        self._auth_approved = value
    @property
    def multi_stage_pay_info(self):
        return self._multi_stage_pay_info

    @multi_stage_pay_info.setter
    def multi_stage_pay_info(self, value):
        if isinstance(value, MultiStagePayInfo):
            self._multi_stage_pay_info = value
        else:
            self._multi_stage_pay_info = MultiStagePayInfo.from_alipay_dict(value)
    @property
    def refuse_desc(self):
        return self._refuse_desc

    @refuse_desc.setter
    def refuse_desc(self, value):
        self._refuse_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiSpayAuthConsultResponse, self).parse_response_content(response_content)
        if 'auth_approved' in response:
            self.auth_approved = response['auth_approved']
        if 'multi_stage_pay_info' in response:
            self.multi_stage_pay_info = response['multi_stage_pay_info']
        if 'refuse_desc' in response:
            self.refuse_desc = response['refuse_desc']
