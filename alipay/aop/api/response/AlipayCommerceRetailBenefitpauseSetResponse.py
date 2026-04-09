#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailBenefitpauseSetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailBenefitpauseSetResponse, self).__init__()
        self._copy_edit_id = None

    @property
    def copy_edit_id(self):
        return self._copy_edit_id

    @copy_edit_id.setter
    def copy_edit_id(self, value):
        self._copy_edit_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailBenefitpauseSetResponse, self).parse_response_content(response_content)
        if 'copy_edit_id' in response:
            self.copy_edit_id = response['copy_edit_id']
