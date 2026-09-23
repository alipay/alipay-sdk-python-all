#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitUseVO import BenefitUseVO
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO


class AlipayVoyagerMarketingFreezeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerMarketingFreezeResponse, self).__init__()
        self._benefit_use_infos = None
        self._freeze_order_id = None
        self._result = None

    @property
    def benefit_use_infos(self):
        return self._benefit_use_infos

    @benefit_use_infos.setter
    def benefit_use_infos(self, value):
        if isinstance(value, list):
            self._benefit_use_infos = list()
            for i in value:
                if isinstance(i, BenefitUseVO):
                    self._benefit_use_infos.append(i)
                else:
                    self._benefit_use_infos.append(BenefitUseVO.from_alipay_dict(i))
    @property
    def freeze_order_id(self):
        return self._freeze_order_id

    @freeze_order_id.setter
    def freeze_order_id(self, value):
        self._freeze_order_id = value
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
        response = super(AlipayVoyagerMarketingFreezeResponse, self).parse_response_content(response_content)
        if 'benefit_use_infos' in response:
            self.benefit_use_infos = response['benefit_use_infos']
        if 'freeze_order_id' in response:
            self.freeze_order_id = response['freeze_order_id']
        if 'result' in response:
            self.result = response['result']
