#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ScalesActivationCodeDeviceRelationInfo import ScalesActivationCodeDeviceRelationInfo


class AlipayMsaasMediarecogAivisionrecgDeviceoperateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogAivisionrecgDeviceoperateQueryResponse, self).__init__()
        self._ret_result = None

    @property
    def ret_result(self):
        return self._ret_result

    @ret_result.setter
    def ret_result(self, value):
        if isinstance(value, list):
            self._ret_result = list()
            for i in value:
                if isinstance(i, ScalesActivationCodeDeviceRelationInfo):
                    self._ret_result.append(i)
                else:
                    self._ret_result.append(ScalesActivationCodeDeviceRelationInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogAivisionrecgDeviceoperateQueryResponse, self).parse_response_content(response_content)
        if 'ret_result' in response:
            self.ret_result = response['ret_result']
