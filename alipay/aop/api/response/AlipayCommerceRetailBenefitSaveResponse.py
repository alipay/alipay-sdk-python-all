#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailBenefitSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailBenefitSaveResponse, self).__init__()
        self._activity_id = None
        self._copy_edit_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def copy_edit_id(self):
        return self._copy_edit_id

    @copy_edit_id.setter
    def copy_edit_id(self, value):
        self._copy_edit_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailBenefitSaveResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'copy_edit_id' in response:
            self.copy_edit_id = response['copy_edit_id']
