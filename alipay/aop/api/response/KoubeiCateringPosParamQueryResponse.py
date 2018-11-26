#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ParamModel import ParamModel


class KoubeiCateringPosParamQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosParamQueryResponse, self).__init__()
        self._param_model = None

    @property
    def param_model(self):
        return self._param_model

    @param_model.setter
    def param_model(self, value):
        if isinstance(value, ParamModel):
            self._param_model = value
        else:
            self._param_model = ParamModel.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosParamQueryResponse, self).parse_response_content(response_content)
        if 'param_model' in response:
            self.param_model = response['param_model']
