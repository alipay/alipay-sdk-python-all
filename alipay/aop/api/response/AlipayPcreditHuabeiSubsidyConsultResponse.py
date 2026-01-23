#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubsidySimpleResponse import SubsidySimpleResponse


class AlipayPcreditHuabeiSubsidyConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiSubsidyConsultResponse, self).__init__()
        self._subsidy_aggregated_resp_models = None

    @property
    def subsidy_aggregated_resp_models(self):
        return self._subsidy_aggregated_resp_models

    @subsidy_aggregated_resp_models.setter
    def subsidy_aggregated_resp_models(self, value):
        if isinstance(value, list):
            self._subsidy_aggregated_resp_models = list()
            for i in value:
                if isinstance(i, SubsidySimpleResponse):
                    self._subsidy_aggregated_resp_models.append(i)
                else:
                    self._subsidy_aggregated_resp_models.append(SubsidySimpleResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiSubsidyConsultResponse, self).parse_response_content(response_content)
        if 'subsidy_aggregated_resp_models' in response:
            self.subsidy_aggregated_resp_models = response['subsidy_aggregated_resp_models']
