#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FeedbackOptionsVO import FeedbackOptionsVO


class AlipayCommerceMedicalLargermodelFeedbackQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalLargermodelFeedbackQueryResponse, self).__init__()
        self._feedback_options_list = None

    @property
    def feedback_options_list(self):
        return self._feedback_options_list

    @feedback_options_list.setter
    def feedback_options_list(self, value):
        if isinstance(value, list):
            self._feedback_options_list = list()
            for i in value:
                if isinstance(i, FeedbackOptionsVO):
                    self._feedback_options_list.append(i)
                else:
                    self._feedback_options_list.append(FeedbackOptionsVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalLargermodelFeedbackQueryResponse, self).parse_response_content(response_content)
        if 'feedback_options_list' in response:
            self.feedback_options_list = response['feedback_options_list']
