#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserFeedbackResult import UserFeedbackResult


class AlipayEngineeringInfrastructureAllBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEngineeringInfrastructureAllBatchqueryResponse, self).__init__()
        self._user_feedback_list = None

    @property
    def user_feedback_list(self):
        return self._user_feedback_list

    @user_feedback_list.setter
    def user_feedback_list(self, value):
        if isinstance(value, list):
            self._user_feedback_list = list()
            for i in value:
                if isinstance(i, UserFeedbackResult):
                    self._user_feedback_list.append(i)
                else:
                    self._user_feedback_list.append(UserFeedbackResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEngineeringInfrastructureAllBatchqueryResponse, self).parse_response_content(response_content)
        if 'user_feedback_list' in response:
            self.user_feedback_list = response['user_feedback_list']
