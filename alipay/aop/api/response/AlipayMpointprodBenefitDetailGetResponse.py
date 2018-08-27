#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitInfo import BenefitInfo


class AlipayMpointprodBenefitDetailGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMpointprodBenefitDetailGetResponse, self).__init__()
        self._benefit_infos = None
        self._code = None
        self._msg = None

    @property
    def benefit_infos(self):
        return self._benefit_infos

    @benefit_infos.setter
    def benefit_infos(self, value):
        if isinstance(value, list):
            self._benefit_infos = list()
            for i in value:
                if isinstance(i, BenefitInfo):
                    self._benefit_infos.append(i)
                else:
                    self._benefit_infos.append(BenefitInfo.from_alipay_dict(i))
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayMpointprodBenefitDetailGetResponse, self).parse_response_content(response_content)
        if 'benefit_infos' in response:
            self.benefit_infos = response['benefit_infos']
        if 'code' in response:
            self.code = response['code']
        if 'msg' in response:
            self.msg = response['msg']
