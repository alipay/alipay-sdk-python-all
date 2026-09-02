#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandEcoNfcCheckResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandEcoNfcCheckResponse, self).__init__()
        self._allow_bind = None
        self._forbid_bind_reason = None
        self._item_id = None
        self._material_type = None

    @property
    def allow_bind(self):
        return self._allow_bind

    @allow_bind.setter
    def allow_bind(self, value):
        self._allow_bind = value
    @property
    def forbid_bind_reason(self):
        return self._forbid_bind_reason

    @forbid_bind_reason.setter
    def forbid_bind_reason(self, value):
        self._forbid_bind_reason = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandEcoNfcCheckResponse, self).parse_response_content(response_content)
        if 'allow_bind' in response:
            self.allow_bind = response['allow_bind']
        if 'forbid_bind_reason' in response:
            self.forbid_bind_reason = response['forbid_bind_reason']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'material_type' in response:
            self.material_type = response['material_type']
