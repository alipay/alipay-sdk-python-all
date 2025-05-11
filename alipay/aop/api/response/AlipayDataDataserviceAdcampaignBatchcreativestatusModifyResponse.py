#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OperateFailRes import OperateFailRes


class AlipayDataDataserviceAdcampaignBatchcreativestatusModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignBatchcreativestatusModifyResponse, self).__init__()
        self._fail_res_list = None
        self._success_id_list = None

    @property
    def fail_res_list(self):
        return self._fail_res_list

    @fail_res_list.setter
    def fail_res_list(self, value):
        if isinstance(value, list):
            self._fail_res_list = list()
            for i in value:
                if isinstance(i, OperateFailRes):
                    self._fail_res_list.append(i)
                else:
                    self._fail_res_list.append(OperateFailRes.from_alipay_dict(i))
    @property
    def success_id_list(self):
        return self._success_id_list

    @success_id_list.setter
    def success_id_list(self, value):
        if isinstance(value, list):
            self._success_id_list = list()
            for i in value:
                self._success_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcampaignBatchcreativestatusModifyResponse, self).parse_response_content(response_content)
        if 'fail_res_list' in response:
            self.fail_res_list = response['fail_res_list']
        if 'success_id_list' in response:
            self.success_id_list = response['success_id_list']
