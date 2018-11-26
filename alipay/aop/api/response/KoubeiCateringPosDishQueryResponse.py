#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PosDishQryModel import PosDishQryModel


class KoubeiCateringPosDishQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosDishQueryResponse, self).__init__()
        self._pos_dish_qry_model = None

    @property
    def pos_dish_qry_model(self):
        return self._pos_dish_qry_model

    @pos_dish_qry_model.setter
    def pos_dish_qry_model(self, value):
        if isinstance(value, PosDishQryModel):
            self._pos_dish_qry_model = value
        else:
            self._pos_dish_qry_model = PosDishQryModel.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosDishQueryResponse, self).parse_response_content(response_content)
        if 'pos_dish_qry_model' in response:
            self.pos_dish_qry_model = response['pos_dish_qry_model']
