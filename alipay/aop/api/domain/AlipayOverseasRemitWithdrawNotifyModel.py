#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasRemitWithdrawNotifyModel(object):

    def __init__(self):
        self._participant_id = None
        self._pass_through_info = None
        self._withdraw_amount_currency = None
        self._withdraw_amount_value = None
        self._withdraw_id = None
        self._withdraw_request_id = None
        self._withdraw_result_code = None
        self._withdraw_result_message = None
        self._withdraw_result_status = None
        self._withdraw_time = None

    @property
    def participant_id(self):
        return self._participant_id

    @participant_id.setter
    def participant_id(self, value):
        self._participant_id = value
    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value
    @property
    def withdraw_amount_currency(self):
        return self._withdraw_amount_currency

    @withdraw_amount_currency.setter
    def withdraw_amount_currency(self, value):
        self._withdraw_amount_currency = value
    @property
    def withdraw_amount_value(self):
        return self._withdraw_amount_value

    @withdraw_amount_value.setter
    def withdraw_amount_value(self, value):
        self._withdraw_amount_value = value
    @property
    def withdraw_id(self):
        return self._withdraw_id

    @withdraw_id.setter
    def withdraw_id(self, value):
        self._withdraw_id = value
    @property
    def withdraw_request_id(self):
        return self._withdraw_request_id

    @withdraw_request_id.setter
    def withdraw_request_id(self, value):
        self._withdraw_request_id = value
    @property
    def withdraw_result_code(self):
        return self._withdraw_result_code

    @withdraw_result_code.setter
    def withdraw_result_code(self, value):
        self._withdraw_result_code = value
    @property
    def withdraw_result_message(self):
        return self._withdraw_result_message

    @withdraw_result_message.setter
    def withdraw_result_message(self, value):
        self._withdraw_result_message = value
    @property
    def withdraw_result_status(self):
        return self._withdraw_result_status

    @withdraw_result_status.setter
    def withdraw_result_status(self, value):
        self._withdraw_result_status = value
    @property
    def withdraw_time(self):
        return self._withdraw_time

    @withdraw_time.setter
    def withdraw_time(self, value):
        self._withdraw_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.participant_id:
            if hasattr(self.participant_id, 'to_alipay_dict'):
                params['participant_id'] = self.participant_id.to_alipay_dict()
            else:
                params['participant_id'] = self.participant_id
        if self.pass_through_info:
            if hasattr(self.pass_through_info, 'to_alipay_dict'):
                params['pass_through_info'] = self.pass_through_info.to_alipay_dict()
            else:
                params['pass_through_info'] = self.pass_through_info
        if self.withdraw_amount_currency:
            if hasattr(self.withdraw_amount_currency, 'to_alipay_dict'):
                params['withdraw_amount_currency'] = self.withdraw_amount_currency.to_alipay_dict()
            else:
                params['withdraw_amount_currency'] = self.withdraw_amount_currency
        if self.withdraw_amount_value:
            if hasattr(self.withdraw_amount_value, 'to_alipay_dict'):
                params['withdraw_amount_value'] = self.withdraw_amount_value.to_alipay_dict()
            else:
                params['withdraw_amount_value'] = self.withdraw_amount_value
        if self.withdraw_id:
            if hasattr(self.withdraw_id, 'to_alipay_dict'):
                params['withdraw_id'] = self.withdraw_id.to_alipay_dict()
            else:
                params['withdraw_id'] = self.withdraw_id
        if self.withdraw_request_id:
            if hasattr(self.withdraw_request_id, 'to_alipay_dict'):
                params['withdraw_request_id'] = self.withdraw_request_id.to_alipay_dict()
            else:
                params['withdraw_request_id'] = self.withdraw_request_id
        if self.withdraw_result_code:
            if hasattr(self.withdraw_result_code, 'to_alipay_dict'):
                params['withdraw_result_code'] = self.withdraw_result_code.to_alipay_dict()
            else:
                params['withdraw_result_code'] = self.withdraw_result_code
        if self.withdraw_result_message:
            if hasattr(self.withdraw_result_message, 'to_alipay_dict'):
                params['withdraw_result_message'] = self.withdraw_result_message.to_alipay_dict()
            else:
                params['withdraw_result_message'] = self.withdraw_result_message
        if self.withdraw_result_status:
            if hasattr(self.withdraw_result_status, 'to_alipay_dict'):
                params['withdraw_result_status'] = self.withdraw_result_status.to_alipay_dict()
            else:
                params['withdraw_result_status'] = self.withdraw_result_status
        if self.withdraw_time:
            if hasattr(self.withdraw_time, 'to_alipay_dict'):
                params['withdraw_time'] = self.withdraw_time.to_alipay_dict()
            else:
                params['withdraw_time'] = self.withdraw_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasRemitWithdrawNotifyModel()
        if 'participant_id' in d:
            o.participant_id = d['participant_id']
        if 'pass_through_info' in d:
            o.pass_through_info = d['pass_through_info']
        if 'withdraw_amount_currency' in d:
            o.withdraw_amount_currency = d['withdraw_amount_currency']
        if 'withdraw_amount_value' in d:
            o.withdraw_amount_value = d['withdraw_amount_value']
        if 'withdraw_id' in d:
            o.withdraw_id = d['withdraw_id']
        if 'withdraw_request_id' in d:
            o.withdraw_request_id = d['withdraw_request_id']
        if 'withdraw_result_code' in d:
            o.withdraw_result_code = d['withdraw_result_code']
        if 'withdraw_result_message' in d:
            o.withdraw_result_message = d['withdraw_result_message']
        if 'withdraw_result_status' in d:
            o.withdraw_result_status = d['withdraw_result_status']
        if 'withdraw_time' in d:
            o.withdraw_time = d['withdraw_time']
        return o


