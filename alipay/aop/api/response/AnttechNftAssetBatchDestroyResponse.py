#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftAssetBatchDestroyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftAssetBatchDestroyResponse, self).__init__()
        self._success_nft_list = None

    @property
    def success_nft_list(self):
        return self._success_nft_list

    @success_nft_list.setter
    def success_nft_list(self, value):
        if isinstance(value, list):
            self._success_nft_list = list()
            for i in value:
                self._success_nft_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AnttechNftAssetBatchDestroyResponse, self).parse_response_content(response_content)
        if 'success_nft_list' in response:
            self.success_nft_list = response['success_nft_list']
