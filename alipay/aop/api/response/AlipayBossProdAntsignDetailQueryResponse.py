#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AntSignTaskResult import AntSignTaskResult


class AlipayBossProdAntsignDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntsignDetailQueryResponse, self).__init__()
        self._ant_sign_task_result_list = None
        self._app_name = None
        self._biz_no = None
        self._sign_flow_id = None
        self._status = None
        self._tenant = None

    @property
    def ant_sign_task_result_list(self):
        return self._ant_sign_task_result_list

    @ant_sign_task_result_list.setter
    def ant_sign_task_result_list(self, value):
        if isinstance(value, list):
            self._ant_sign_task_result_list = list()
            for i in value:
                if isinstance(i, AntSignTaskResult):
                    self._ant_sign_task_result_list.append(i)
                else:
                    self._ant_sign_task_result_list.append(AntSignTaskResult.from_alipay_dict(i))
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntsignDetailQueryResponse, self).parse_response_content(response_content)
        if 'ant_sign_task_result_list' in response:
            self.ant_sign_task_result_list = response['ant_sign_task_result_list']
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'sign_flow_id' in response:
            self.sign_flow_id = response['sign_flow_id']
        if 'status' in response:
            self.status = response['status']
        if 'tenant' in response:
            self.tenant = response['tenant']
