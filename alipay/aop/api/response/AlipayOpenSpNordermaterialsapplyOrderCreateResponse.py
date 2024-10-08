#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNordermaterialsapplyOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsapplyOrderCreateResponse, self).__init__()
        self._apply_id = None
        self._materials_template_type = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def materials_template_type(self):
        return self._materials_template_type

    @materials_template_type.setter
    def materials_template_type(self, value):
        self._materials_template_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsapplyOrderCreateResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'materials_template_type' in response:
            self.materials_template_type = response['materials_template_type']
