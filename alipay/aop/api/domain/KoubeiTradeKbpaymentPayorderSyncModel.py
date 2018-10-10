#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbpFundTool import KbpFundTool


class KoubeiTradeKbpaymentPayorderSyncModel(object):

    def __init__(self):
        self._attach = None
        self._fee_type = None
        self._fund_command_id = None
        self._fund_status = None
        self._fund_tool_list = None
        self._gmt_finish = None
        self._out_pay_id = None
        self._request_id = None
        self._total_fee = None

    @property
    def attach(self):
        return self._attach

    @attach.setter
    def attach(self, value):
        self._attach = value
    @property
    def fee_type(self):
        return self._fee_type

    @fee_type.setter
    def fee_type(self, value):
        self._fee_type = value
    @property
    def fund_command_id(self):
        return self._fund_command_id

    @fund_command_id.setter
    def fund_command_id(self, value):
        self._fund_command_id = value
    @property
    def fund_status(self):
        return self._fund_status

    @fund_status.setter
    def fund_status(self, value):
        self._fund_status = value
    @property
    def fund_tool_list(self):
        return self._fund_tool_list

    @fund_tool_list.setter
    def fund_tool_list(self, value):
        if isinstance(value, list):
            self._fund_tool_list = list()
            for i in value:
                if isinstance(i, KbpFundTool):
                    self._fund_tool_list.append(i)
                else:
                    self._fund_tool_list.append(KbpFundTool.from_alipay_dict(i))
    @property
    def gmt_finish(self):
        return self._gmt_finish

    @gmt_finish.setter
    def gmt_finish(self, value):
        self._gmt_finish = value
    @property
    def out_pay_id(self):
        return self._out_pay_id

    @out_pay_id.setter
    def out_pay_id(self, value):
        self._out_pay_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def total_fee(self):
        return self._total_fee

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.attach:
            if hasattr(self.attach, 'to_alipay_dict'):
                params['attach'] = self.attach.to_alipay_dict()
            else:
                params['attach'] = self.attach
        if self.fee_type:
            if hasattr(self.fee_type, 'to_alipay_dict'):
                params['fee_type'] = self.fee_type.to_alipay_dict()
            else:
                params['fee_type'] = self.fee_type
        if self.fund_command_id:
            if hasattr(self.fund_command_id, 'to_alipay_dict'):
                params['fund_command_id'] = self.fund_command_id.to_alipay_dict()
            else:
                params['fund_command_id'] = self.fund_command_id
        if self.fund_status:
            if hasattr(self.fund_status, 'to_alipay_dict'):
                params['fund_status'] = self.fund_status.to_alipay_dict()
            else:
                params['fund_status'] = self.fund_status
        if self.fund_tool_list:
            if isinstance(self.fund_tool_list, list):
                for i in range(0, len(self.fund_tool_list)):
                    element = self.fund_tool_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_tool_list[i] = element.to_alipay_dict()
            if hasattr(self.fund_tool_list, 'to_alipay_dict'):
                params['fund_tool_list'] = self.fund_tool_list.to_alipay_dict()
            else:
                params['fund_tool_list'] = self.fund_tool_list
        if self.gmt_finish:
            if hasattr(self.gmt_finish, 'to_alipay_dict'):
                params['gmt_finish'] = self.gmt_finish.to_alipay_dict()
            else:
                params['gmt_finish'] = self.gmt_finish
        if self.out_pay_id:
            if hasattr(self.out_pay_id, 'to_alipay_dict'):
                params['out_pay_id'] = self.out_pay_id.to_alipay_dict()
            else:
                params['out_pay_id'] = self.out_pay_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.total_fee:
            if hasattr(self.total_fee, 'to_alipay_dict'):
                params['total_fee'] = self.total_fee.to_alipay_dict()
            else:
                params['total_fee'] = self.total_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeKbpaymentPayorderSyncModel()
        if 'attach' in d:
            o.attach = d['attach']
        if 'fee_type' in d:
            o.fee_type = d['fee_type']
        if 'fund_command_id' in d:
            o.fund_command_id = d['fund_command_id']
        if 'fund_status' in d:
            o.fund_status = d['fund_status']
        if 'fund_tool_list' in d:
            o.fund_tool_list = d['fund_tool_list']
        if 'gmt_finish' in d:
            o.gmt_finish = d['gmt_finish']
        if 'out_pay_id' in d:
            o.out_pay_id = d['out_pay_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'total_fee' in d:
            o.total_fee = d['total_fee']
        return o


