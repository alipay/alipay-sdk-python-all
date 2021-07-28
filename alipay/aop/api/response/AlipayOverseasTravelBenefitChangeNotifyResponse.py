#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Result import Result


class AlipayOverseasTravelBenefitChangeNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelBenefitChangeNotifyResponse, self).__init__()
        self._acquirer_id = None
        self._psp_id = None
        self._result = None

    @property
    def acquirer_id(self):
        return self._acquirer_id

    @acquirer_id.setter
    def acquirer_id(self, value):
        self._acquirer_id = value
    @property
    def psp_id(self):
        return self._psp_id

    @psp_id.setter
    def psp_id(self, value):
        self._psp_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, Result):
            self._result = value
        else:
            self._result = Result.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelBenefitChangeNotifyResponse, self).parse_response_content(response_content)
        if 'acquirer_id' in response:
            self.acquirer_id = response['acquirer_id']
        if 'psp_id' in response:
            self.psp_id = response['psp_id']
        if 'result' in response:
            self.result = response['result']
