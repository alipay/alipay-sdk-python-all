#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseSourceuidPidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseSourceuidPidQueryResponse, self).__init__()
        self._alipay_virtual_id = None
        self._source_uid = None

    @property
    def alipay_virtual_id(self):
        return self._alipay_virtual_id

    @alipay_virtual_id.setter
    def alipay_virtual_id(self, value):
        self._alipay_virtual_id = value
    @property
    def source_uid(self):
        return self._source_uid

    @source_uid.setter
    def source_uid(self, value):
        self._source_uid = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseSourceuidPidQueryResponse, self).parse_response_content(response_content)
        if 'alipay_virtual_id' in response:
            self.alipay_virtual_id = response['alipay_virtual_id']
        if 'source_uid' in response:
            self.source_uid = response['source_uid']
