#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingBeneficiaryGroupSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBeneficiaryGroupSyncResponse, self).__init__()
        self._sync_biz_no = None

    @property
    def sync_biz_no(self):
        return self._sync_biz_no

    @sync_biz_no.setter
    def sync_biz_no(self, value):
        self._sync_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBeneficiaryGroupSyncResponse, self).parse_response_content(response_content)
        if 'sync_biz_no' in response:
            self.sync_biz_no = response['sync_biz_no']
