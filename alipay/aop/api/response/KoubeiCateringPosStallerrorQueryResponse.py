#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ErrorDishStallEntity import ErrorDishStallEntity


class KoubeiCateringPosStallerrorQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosStallerrorQueryResponse, self).__init__()
        self._error_dish_stall_entity = None

    @property
    def error_dish_stall_entity(self):
        return self._error_dish_stall_entity

    @error_dish_stall_entity.setter
    def error_dish_stall_entity(self, value):
        if isinstance(value, ErrorDishStallEntity):
            self._error_dish_stall_entity = value
        else:
            self._error_dish_stall_entity = ErrorDishStallEntity.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosStallerrorQueryResponse, self).parse_response_content(response_content)
        if 'error_dish_stall_entity' in response:
            self.error_dish_stall_entity = response['error_dish_stall_entity']
