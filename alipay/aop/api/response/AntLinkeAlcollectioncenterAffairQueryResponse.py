#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntLinkeAlcollectioncenterAffairQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntLinkeAlcollectioncenterAffairQueryResponse, self).__init__()
        self._affair_id = None
        self._affair_status = None
        self._order_id = None

    @property
    def affair_id(self):
        return self._affair_id

    @affair_id.setter
    def affair_id(self, value):
        self._affair_id = value
    @property
    def affair_status(self):
        return self._affair_status

    @affair_status.setter
    def affair_status(self, value):
        self._affair_status = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(AntLinkeAlcollectioncenterAffairQueryResponse, self).parse_response_content(response_content)
        if 'affair_id' in response:
            self.affair_id = response['affair_id']
        if 'affair_status' in response:
            self.affair_status = response['affair_status']
        if 'order_id' in response:
            self.order_id = response['order_id']
