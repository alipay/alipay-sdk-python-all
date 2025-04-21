#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AliyunCustomerInfoDTO import AliyunCustomerInfoDTO


class AnttechOceanbaseCustomerAliyuncustomerBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseCustomerAliyuncustomerBatchqueryResponse, self).__init__()
        self._aliyun_customer_info_list = None

    @property
    def aliyun_customer_info_list(self):
        return self._aliyun_customer_info_list

    @aliyun_customer_info_list.setter
    def aliyun_customer_info_list(self, value):
        if isinstance(value, list):
            self._aliyun_customer_info_list = list()
            for i in value:
                if isinstance(i, AliyunCustomerInfoDTO):
                    self._aliyun_customer_info_list.append(i)
                else:
                    self._aliyun_customer_info_list.append(AliyunCustomerInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseCustomerAliyuncustomerBatchqueryResponse, self).parse_response_content(response_content)
        if 'aliyun_customer_info_list' in response:
            self.aliyun_customer_info_list = response['aliyun_customer_info_list']
