#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HmEquityInfo import HmEquityInfo


class AlipayCommerceMedicalHmUserequitySyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHmUserequitySyncResponse, self).__init__()
        self._equity_info_list = None
        self._equity_package_code = None
        self._out_biz_serial_no = None
        self._project_tag = None
        self._user_id = None

    @property
    def equity_info_list(self):
        return self._equity_info_list

    @equity_info_list.setter
    def equity_info_list(self, value):
        if isinstance(value, list):
            self._equity_info_list = list()
            for i in value:
                if isinstance(i, HmEquityInfo):
                    self._equity_info_list.append(i)
                else:
                    self._equity_info_list.append(HmEquityInfo.from_alipay_dict(i))
    @property
    def equity_package_code(self):
        return self._equity_package_code

    @equity_package_code.setter
    def equity_package_code(self, value):
        self._equity_package_code = value
    @property
    def out_biz_serial_no(self):
        return self._out_biz_serial_no

    @out_biz_serial_no.setter
    def out_biz_serial_no(self, value):
        self._out_biz_serial_no = value
    @property
    def project_tag(self):
        return self._project_tag

    @project_tag.setter
    def project_tag(self, value):
        self._project_tag = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHmUserequitySyncResponse, self).parse_response_content(response_content)
        if 'equity_info_list' in response:
            self.equity_info_list = response['equity_info_list']
        if 'equity_package_code' in response:
            self.equity_package_code = response['equity_package_code']
        if 'out_biz_serial_no' in response:
            self.out_biz_serial_no = response['out_biz_serial_no']
        if 'project_tag' in response:
            self.project_tag = response['project_tag']
        if 'user_id' in response:
            self.user_id = response['user_id']
