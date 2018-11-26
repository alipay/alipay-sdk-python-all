#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PosDishCookModel import PosDishCookModel


class KoubeiCateringPosCooklistQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosCooklistQueryResponse, self).__init__()
        self._cook_models = None

    @property
    def cook_models(self):
        return self._cook_models

    @cook_models.setter
    def cook_models(self, value):
        if isinstance(value, list):
            self._cook_models = list()
            for i in value:
                if isinstance(i, PosDishCookModel):
                    self._cook_models.append(i)
                else:
                    self._cook_models.append(PosDishCookModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosCooklistQueryResponse, self).parse_response_content(response_content)
        if 'cook_models' in response:
            self.cook_models = response['cook_models']
