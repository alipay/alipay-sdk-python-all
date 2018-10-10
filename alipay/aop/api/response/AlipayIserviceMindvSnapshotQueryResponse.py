#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceMindvSnapshotQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceMindvSnapshotQueryResponse, self).__init__()
        self._gmt_create = None
        self._id = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceMindvSnapshotQueryResponse, self).parse_response_content(response_content)
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'id' in response:
            self.id = response['id']
