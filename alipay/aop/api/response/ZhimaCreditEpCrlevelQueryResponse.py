#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpCrlevelQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCrlevelQueryResponse, self).__init__()
        self._cr_rank = None
        self._cr_rank_title = None
        self._has_cr_rank = None

    @property
    def cr_rank(self):
        return self._cr_rank

    @cr_rank.setter
    def cr_rank(self, value):
        self._cr_rank = value
    @property
    def cr_rank_title(self):
        return self._cr_rank_title

    @cr_rank_title.setter
    def cr_rank_title(self, value):
        self._cr_rank_title = value
    @property
    def has_cr_rank(self):
        return self._has_cr_rank

    @has_cr_rank.setter
    def has_cr_rank(self, value):
        self._has_cr_rank = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCrlevelQueryResponse, self).parse_response_content(response_content)
        if 'cr_rank' in response:
            self.cr_rank = response['cr_rank']
        if 'cr_rank_title' in response:
            self.cr_rank_title = response['cr_rank_title']
        if 'has_cr_rank' in response:
            self.has_cr_rank = response['has_cr_rank']
