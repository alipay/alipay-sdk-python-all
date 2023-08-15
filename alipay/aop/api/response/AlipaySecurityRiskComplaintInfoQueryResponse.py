#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ComplaintTradeInfo import ComplaintTradeInfo


class AlipaySecurityRiskComplaintInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskComplaintInfoQueryResponse, self).__init__()
        self._complain_amount = None
        self._complain_content = None
        self._complain_url = None
        self._complaint_trade_info_list = None
        self._contact = None
        self._gmt_complain = None
        self._gmt_overdue = None
        self._gmt_process = None
        self._gmt_risk_finish_time = None
        self._id = None
        self._opposite_name = None
        self._opposite_pid = None
        self._process_code = None
        self._process_img_url_list = None
        self._process_message = None
        self._process_remark = None
        self._status = None
        self._status_description = None
        self._task_id = None
        self._trade_no = None

    @property
    def complain_amount(self):
        return self._complain_amount

    @complain_amount.setter
    def complain_amount(self, value):
        self._complain_amount = value
    @property
    def complain_content(self):
        return self._complain_content

    @complain_content.setter
    def complain_content(self, value):
        self._complain_content = value
    @property
    def complain_url(self):
        return self._complain_url

    @complain_url.setter
    def complain_url(self, value):
        self._complain_url = value
    @property
    def complaint_trade_info_list(self):
        return self._complaint_trade_info_list

    @complaint_trade_info_list.setter
    def complaint_trade_info_list(self, value):
        if isinstance(value, list):
            self._complaint_trade_info_list = list()
            for i in value:
                if isinstance(i, ComplaintTradeInfo):
                    self._complaint_trade_info_list.append(i)
                else:
                    self._complaint_trade_info_list.append(ComplaintTradeInfo.from_alipay_dict(i))
    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value
    @property
    def gmt_complain(self):
        return self._gmt_complain

    @gmt_complain.setter
    def gmt_complain(self, value):
        self._gmt_complain = value
    @property
    def gmt_overdue(self):
        return self._gmt_overdue

    @gmt_overdue.setter
    def gmt_overdue(self, value):
        self._gmt_overdue = value
    @property
    def gmt_process(self):
        return self._gmt_process

    @gmt_process.setter
    def gmt_process(self, value):
        self._gmt_process = value
    @property
    def gmt_risk_finish_time(self):
        return self._gmt_risk_finish_time

    @gmt_risk_finish_time.setter
    def gmt_risk_finish_time(self, value):
        self._gmt_risk_finish_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def opposite_name(self):
        return self._opposite_name

    @opposite_name.setter
    def opposite_name(self, value):
        self._opposite_name = value
    @property
    def opposite_pid(self):
        return self._opposite_pid

    @opposite_pid.setter
    def opposite_pid(self, value):
        self._opposite_pid = value
    @property
    def process_code(self):
        return self._process_code

    @process_code.setter
    def process_code(self, value):
        self._process_code = value
    @property
    def process_img_url_list(self):
        return self._process_img_url_list

    @process_img_url_list.setter
    def process_img_url_list(self, value):
        if isinstance(value, list):
            self._process_img_url_list = list()
            for i in value:
                self._process_img_url_list.append(i)
    @property
    def process_message(self):
        return self._process_message

    @process_message.setter
    def process_message(self, value):
        self._process_message = value
    @property
    def process_remark(self):
        return self._process_remark

    @process_remark.setter
    def process_remark(self, value):
        self._process_remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_description(self):
        return self._status_description

    @status_description.setter
    def status_description(self, value):
        self._status_description = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskComplaintInfoQueryResponse, self).parse_response_content(response_content)
        if 'complain_amount' in response:
            self.complain_amount = response['complain_amount']
        if 'complain_content' in response:
            self.complain_content = response['complain_content']
        if 'complain_url' in response:
            self.complain_url = response['complain_url']
        if 'complaint_trade_info_list' in response:
            self.complaint_trade_info_list = response['complaint_trade_info_list']
        if 'contact' in response:
            self.contact = response['contact']
        if 'gmt_complain' in response:
            self.gmt_complain = response['gmt_complain']
        if 'gmt_overdue' in response:
            self.gmt_overdue = response['gmt_overdue']
        if 'gmt_process' in response:
            self.gmt_process = response['gmt_process']
        if 'gmt_risk_finish_time' in response:
            self.gmt_risk_finish_time = response['gmt_risk_finish_time']
        if 'id' in response:
            self.id = response['id']
        if 'opposite_name' in response:
            self.opposite_name = response['opposite_name']
        if 'opposite_pid' in response:
            self.opposite_pid = response['opposite_pid']
        if 'process_code' in response:
            self.process_code = response['process_code']
        if 'process_img_url_list' in response:
            self.process_img_url_list = response['process_img_url_list']
        if 'process_message' in response:
            self.process_message = response['process_message']
        if 'process_remark' in response:
            self.process_remark = response['process_remark']
        if 'status' in response:
            self.status = response['status']
        if 'status_description' in response:
            self.status_description = response['status_description']
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
