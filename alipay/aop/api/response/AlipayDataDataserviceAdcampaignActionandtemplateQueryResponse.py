#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreativeActionAndTemplateResponse import CreativeActionAndTemplateResponse


class AlipayDataDataserviceAdcampaignActionandtemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignActionandtemplateQueryResponse, self).__init__()
        self._result_list = None

    @property
    def result_list(self):
        return self._result_list

    @result_list.setter
    def result_list(self, value):
        if isinstance(value, list):
            self._result_list = list()
            for i in value:
                if isinstance(i, CreativeActionAndTemplateResponse):
                    self._result_list.append(i)
                else:
                    self._result_list.append(CreativeActionAndTemplateResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcampaignActionandtemplateQueryResponse, self).parse_response_content(response_content)
        if 'result_list' in response:
            self.result_list = response['result_list']
