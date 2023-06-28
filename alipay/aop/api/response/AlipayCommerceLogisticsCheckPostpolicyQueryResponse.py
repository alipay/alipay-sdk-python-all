#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcocheckYzPolicyCheckDetail import EcocheckYzPolicyCheckDetail


class AlipayCommerceLogisticsCheckPostpolicyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsCheckPostpolicyQueryResponse, self).__init__()
        self._app_check_info_list = None
        self._invalid_app_id_list = None

    @property
    def app_check_info_list(self):
        return self._app_check_info_list

    @app_check_info_list.setter
    def app_check_info_list(self, value):
        if isinstance(value, list):
            self._app_check_info_list = list()
            for i in value:
                if isinstance(i, EcocheckYzPolicyCheckDetail):
                    self._app_check_info_list.append(i)
                else:
                    self._app_check_info_list.append(EcocheckYzPolicyCheckDetail.from_alipay_dict(i))
    @property
    def invalid_app_id_list(self):
        return self._invalid_app_id_list

    @invalid_app_id_list.setter
    def invalid_app_id_list(self, value):
        if isinstance(value, list):
            self._invalid_app_id_list = list()
            for i in value:
                self._invalid_app_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsCheckPostpolicyQueryResponse, self).parse_response_content(response_content)
        if 'app_check_info_list' in response:
            self.app_check_info_list = response['app_check_info_list']
        if 'invalid_app_id_list' in response:
            self.invalid_app_id_list = response['invalid_app_id_list']
