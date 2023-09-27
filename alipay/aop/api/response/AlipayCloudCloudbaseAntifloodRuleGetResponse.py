#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseAntifloodRuleGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseAntifloodRuleGetResponse, self).__init__()
        self._cidr_block = None
        self._end = None
        self._gmt_create = None
        self._gmt_modified = None
        self._source = None
        self._start = None

    @property
    def cidr_block(self):
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, value):
        self._cidr_block = value
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseAntifloodRuleGetResponse, self).parse_response_content(response_content)
        if 'cidr_block' in response:
            self.cidr_block = response['cidr_block']
        if 'end' in response:
            self.end = response['end']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'source' in response:
            self.source = response['source']
        if 'start' in response:
            self.start = response['start']
