#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTransferPaymentNotifyModel(object):

    def __init__(self):
        self._pass_through_info = None
        self._payer_agent_id = None
        self._transfer_request_id = None

    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value
    @property
    def payer_agent_id(self):
        return self._payer_agent_id

    @payer_agent_id.setter
    def payer_agent_id(self, value):
        self._payer_agent_id = value
    @property
    def transfer_request_id(self):
        return self._transfer_request_id

    @transfer_request_id.setter
    def transfer_request_id(self, value):
        self._transfer_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.pass_through_info:
            if hasattr(self.pass_through_info, 'to_alipay_dict'):
                params['pass_through_info'] = self.pass_through_info.to_alipay_dict()
            else:
                params['pass_through_info'] = self.pass_through_info
        if self.payer_agent_id:
            if hasattr(self.payer_agent_id, 'to_alipay_dict'):
                params['payer_agent_id'] = self.payer_agent_id.to_alipay_dict()
            else:
                params['payer_agent_id'] = self.payer_agent_id
        if self.transfer_request_id:
            if hasattr(self.transfer_request_id, 'to_alipay_dict'):
                params['transfer_request_id'] = self.transfer_request_id.to_alipay_dict()
            else:
                params['transfer_request_id'] = self.transfer_request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTransferPaymentNotifyModel()
        if 'pass_through_info' in d:
            o.pass_through_info = d['pass_through_info']
        if 'payer_agent_id' in d:
            o.payer_agent_id = d['payer_agent_id']
        if 'transfer_request_id' in d:
            o.transfer_request_id = d['transfer_request_id']
        return o


