#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ConsultActivityResultInfo import ConsultActivityResultInfo


class AlipayMarketingActivityConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityConsultResponse, self).__init__()
        self._consult_result_info_list = None
        self._user_id = None

    @property
    def consult_result_info_list(self):
        return self._consult_result_info_list

    @consult_result_info_list.setter
    def consult_result_info_list(self, value):
        if isinstance(value, list):
            self._consult_result_info_list = list()
            for i in value:
                if isinstance(i, ConsultActivityResultInfo):
                    self._consult_result_info_list.append(i)
                else:
                    self._consult_result_info_list.append(ConsultActivityResultInfo.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityConsultResponse, self).parse_response_content(response_content)
        if 'consult_result_info_list' in response:
            self.consult_result_info_list = response['consult_result_info_list']
        if 'user_id' in response:
            self.user_id = response['user_id']
