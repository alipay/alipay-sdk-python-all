#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CrowdExportData import CrowdExportData


class AlipayMerchantQipanCrowdexportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanCrowdexportQueryResponse, self).__init__()
        self._crowd_code = None
        self._crowd_export_data = None
        self._out_biz_no = None
        self._task_no = None
        self._task_status = None

    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def crowd_export_data(self):
        return self._crowd_export_data

    @crowd_export_data.setter
    def crowd_export_data(self, value):
        if isinstance(value, CrowdExportData):
            self._crowd_export_data = value
        else:
            self._crowd_export_data = CrowdExportData.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def task_no(self):
        return self._task_no

    @task_no.setter
    def task_no(self, value):
        self._task_no = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanCrowdexportQueryResponse, self).parse_response_content(response_content)
        if 'crowd_code' in response:
            self.crowd_code = response['crowd_code']
        if 'crowd_export_data' in response:
            self.crowd_export_data = response['crowd_export_data']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'task_no' in response:
            self.task_no = response['task_no']
        if 'task_status' in response:
            self.task_status = response['task_status']
