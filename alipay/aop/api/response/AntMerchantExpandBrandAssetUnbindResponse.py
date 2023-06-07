#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandBrandAssetUnbindResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandBrandAssetUnbindResponse, self).__init__()
        self._fail_asset_ids = None
        self._fail_msg = None
        self._result = None

    @property
    def fail_asset_ids(self):
        return self._fail_asset_ids

    @fail_asset_ids.setter
    def fail_asset_ids(self, value):
        if isinstance(value, list):
            self._fail_asset_ids = list()
            for i in value:
                self._fail_asset_ids.append(i)
    @property
    def fail_msg(self):
        return self._fail_msg

    @fail_msg.setter
    def fail_msg(self, value):
        self._fail_msg = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandBrandAssetUnbindResponse, self).parse_response_content(response_content)
        if 'fail_asset_ids' in response:
            self.fail_asset_ids = response['fail_asset_ids']
        if 'fail_msg' in response:
            self.fail_msg = response['fail_msg']
        if 'result' in response:
            self.result = response['result']
