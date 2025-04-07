#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftBaseinfoNftidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftBaseinfoNftidQueryResponse, self).__init__()
        self._nft_hash = None
        self._nft_id = None
        self._nft_issue_time = None

    @property
    def nft_hash(self):
        return self._nft_hash

    @nft_hash.setter
    def nft_hash(self, value):
        self._nft_hash = value
    @property
    def nft_id(self):
        return self._nft_id

    @nft_id.setter
    def nft_id(self, value):
        self._nft_id = value
    @property
    def nft_issue_time(self):
        return self._nft_issue_time

    @nft_issue_time.setter
    def nft_issue_time(self, value):
        self._nft_issue_time = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftBaseinfoNftidQueryResponse, self).parse_response_content(response_content)
        if 'nft_hash' in response:
            self.nft_hash = response['nft_hash']
        if 'nft_id' in response:
            self.nft_id = response['nft_id']
        if 'nft_issue_time' in response:
            self.nft_issue_time = response['nft_issue_time']
