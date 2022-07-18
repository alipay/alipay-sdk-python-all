#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TenantChannelDetailDTO import TenantChannelDetailDTO


class DatadigitalFincloudFinsaasTenantchannelListBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasTenantchannelListBatchqueryResponse, self).__init__()
        self._tenant_channel_list = None

    @property
    def tenant_channel_list(self):
        return self._tenant_channel_list

    @tenant_channel_list.setter
    def tenant_channel_list(self, value):
        if isinstance(value, list):
            self._tenant_channel_list = list()
            for i in value:
                if isinstance(i, TenantChannelDetailDTO):
                    self._tenant_channel_list.append(i)
                else:
                    self._tenant_channel_list.append(TenantChannelDetailDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasTenantchannelListBatchqueryResponse, self).parse_response_content(response_content)
        if 'tenant_channel_list' in response:
            self.tenant_channel_list = response['tenant_channel_list']
