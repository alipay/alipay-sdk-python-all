#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ComplaintTradeInfo import ComplaintTradeInfo


class ComplaintInfoQueryResponse(object):

    def __init__(self):
        self._complain_amount = None
        self._complain_content = None
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


    def to_alipay_dict(self):
        params = dict()
        if self.complain_amount:
            if hasattr(self.complain_amount, 'to_alipay_dict'):
                params['complain_amount'] = self.complain_amount.to_alipay_dict()
            else:
                params['complain_amount'] = self.complain_amount
        if self.complain_content:
            if hasattr(self.complain_content, 'to_alipay_dict'):
                params['complain_content'] = self.complain_content.to_alipay_dict()
            else:
                params['complain_content'] = self.complain_content
        if self.complaint_trade_info_list:
            if isinstance(self.complaint_trade_info_list, list):
                for i in range(0, len(self.complaint_trade_info_list)):
                    element = self.complaint_trade_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.complaint_trade_info_list[i] = element.to_alipay_dict()
            if hasattr(self.complaint_trade_info_list, 'to_alipay_dict'):
                params['complaint_trade_info_list'] = self.complaint_trade_info_list.to_alipay_dict()
            else:
                params['complaint_trade_info_list'] = self.complaint_trade_info_list
        if self.contact:
            if hasattr(self.contact, 'to_alipay_dict'):
                params['contact'] = self.contact.to_alipay_dict()
            else:
                params['contact'] = self.contact
        if self.gmt_complain:
            if hasattr(self.gmt_complain, 'to_alipay_dict'):
                params['gmt_complain'] = self.gmt_complain.to_alipay_dict()
            else:
                params['gmt_complain'] = self.gmt_complain
        if self.gmt_overdue:
            if hasattr(self.gmt_overdue, 'to_alipay_dict'):
                params['gmt_overdue'] = self.gmt_overdue.to_alipay_dict()
            else:
                params['gmt_overdue'] = self.gmt_overdue
        if self.gmt_process:
            if hasattr(self.gmt_process, 'to_alipay_dict'):
                params['gmt_process'] = self.gmt_process.to_alipay_dict()
            else:
                params['gmt_process'] = self.gmt_process
        if self.gmt_risk_finish_time:
            if hasattr(self.gmt_risk_finish_time, 'to_alipay_dict'):
                params['gmt_risk_finish_time'] = self.gmt_risk_finish_time.to_alipay_dict()
            else:
                params['gmt_risk_finish_time'] = self.gmt_risk_finish_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.opposite_name:
            if hasattr(self.opposite_name, 'to_alipay_dict'):
                params['opposite_name'] = self.opposite_name.to_alipay_dict()
            else:
                params['opposite_name'] = self.opposite_name
        if self.opposite_pid:
            if hasattr(self.opposite_pid, 'to_alipay_dict'):
                params['opposite_pid'] = self.opposite_pid.to_alipay_dict()
            else:
                params['opposite_pid'] = self.opposite_pid
        if self.process_code:
            if hasattr(self.process_code, 'to_alipay_dict'):
                params['process_code'] = self.process_code.to_alipay_dict()
            else:
                params['process_code'] = self.process_code
        if self.process_img_url_list:
            if isinstance(self.process_img_url_list, list):
                for i in range(0, len(self.process_img_url_list)):
                    element = self.process_img_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.process_img_url_list[i] = element.to_alipay_dict()
            if hasattr(self.process_img_url_list, 'to_alipay_dict'):
                params['process_img_url_list'] = self.process_img_url_list.to_alipay_dict()
            else:
                params['process_img_url_list'] = self.process_img_url_list
        if self.process_message:
            if hasattr(self.process_message, 'to_alipay_dict'):
                params['process_message'] = self.process_message.to_alipay_dict()
            else:
                params['process_message'] = self.process_message
        if self.process_remark:
            if hasattr(self.process_remark, 'to_alipay_dict'):
                params['process_remark'] = self.process_remark.to_alipay_dict()
            else:
                params['process_remark'] = self.process_remark
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_description:
            if hasattr(self.status_description, 'to_alipay_dict'):
                params['status_description'] = self.status_description.to_alipay_dict()
            else:
                params['status_description'] = self.status_description
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ComplaintInfoQueryResponse()
        if 'complain_amount' in d:
            o.complain_amount = d['complain_amount']
        if 'complain_content' in d:
            o.complain_content = d['complain_content']
        if 'complaint_trade_info_list' in d:
            o.complaint_trade_info_list = d['complaint_trade_info_list']
        if 'contact' in d:
            o.contact = d['contact']
        if 'gmt_complain' in d:
            o.gmt_complain = d['gmt_complain']
        if 'gmt_overdue' in d:
            o.gmt_overdue = d['gmt_overdue']
        if 'gmt_process' in d:
            o.gmt_process = d['gmt_process']
        if 'gmt_risk_finish_time' in d:
            o.gmt_risk_finish_time = d['gmt_risk_finish_time']
        if 'id' in d:
            o.id = d['id']
        if 'opposite_name' in d:
            o.opposite_name = d['opposite_name']
        if 'opposite_pid' in d:
            o.opposite_pid = d['opposite_pid']
        if 'process_code' in d:
            o.process_code = d['process_code']
        if 'process_img_url_list' in d:
            o.process_img_url_list = d['process_img_url_list']
        if 'process_message' in d:
            o.process_message = d['process_message']
        if 'process_remark' in d:
            o.process_remark = d['process_remark']
        if 'status' in d:
            o.status = d['status']
        if 'status_description' in d:
            o.status_description = d['status_description']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


