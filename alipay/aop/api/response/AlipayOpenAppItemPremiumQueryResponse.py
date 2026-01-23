#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppItemPremiumQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppItemPremiumQueryResponse, self).__init__()
        self._audit_status = None
        self._item_id = None
        self._remark = None

    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppItemPremiumQueryResponse, self).parse_response_content(response_content)
        if 'audit_status' in response:
            self.audit_status = response['audit_status']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'remark' in response:
            self.remark = response['remark']
