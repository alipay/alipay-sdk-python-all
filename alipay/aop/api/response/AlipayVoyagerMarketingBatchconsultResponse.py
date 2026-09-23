#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitDisplayVO import BenefitDisplayVO
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO


class AlipayVoyagerMarketingBatchconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerMarketingBatchconsultResponse, self).__init__()
        self._best_benefit_list = None
        self._result = None

    @property
    def best_benefit_list(self):
        return self._best_benefit_list

    @best_benefit_list.setter
    def best_benefit_list(self, value):
        if isinstance(value, BenefitDisplayVO):
            self._best_benefit_list = value
        else:
            self._best_benefit_list = BenefitDisplayVO.from_alipay_dict(value)
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, ResultInfoDTO):
            self._result = value
        else:
            self._result = ResultInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayVoyagerMarketingBatchconsultResponse, self).parse_response_content(response_content)
        if 'best_benefit_list' in response:
            self.best_benefit_list = response['best_benefit_list']
        if 'result' in response:
            self.result = response['result']
