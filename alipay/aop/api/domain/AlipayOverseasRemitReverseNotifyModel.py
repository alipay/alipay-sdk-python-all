#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Money import Money
from alipay.aop.api.domain.Money import Money


class AlipayOverseasRemitReverseNotifyModel(object):

    def __init__(self):
        self._pass_through_info = None
        self._reverse_from_amount = None
        self._reverse_id = None
        self._reverse_quote = None
        self._reverse_reason = None
        self._reverse_reason_message = None
        self._reverse_request_id = None
        self._reverse_result = None
        self._reverse_time = None
        self._reverse_to_amount = None
        self._transfer_request_id = None

    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value
    @property
    def reverse_from_amount(self):
        return self._reverse_from_amount

    @reverse_from_amount.setter
    def reverse_from_amount(self, value):
        if isinstance(value, Money):
            self._reverse_from_amount = value
        else:
            self._reverse_from_amount = Money.from_alipay_dict(value)
    @property
    def reverse_id(self):
        return self._reverse_id

    @reverse_id.setter
    def reverse_id(self, value):
        self._reverse_id = value
    @property
    def reverse_quote(self):
        return self._reverse_quote

    @reverse_quote.setter
    def reverse_quote(self, value):
        self._reverse_quote = value
    @property
    def reverse_reason(self):
        return self._reverse_reason

    @reverse_reason.setter
    def reverse_reason(self, value):
        self._reverse_reason = value
    @property
    def reverse_reason_message(self):
        return self._reverse_reason_message

    @reverse_reason_message.setter
    def reverse_reason_message(self, value):
        self._reverse_reason_message = value
    @property
    def reverse_request_id(self):
        return self._reverse_request_id

    @reverse_request_id.setter
    def reverse_request_id(self, value):
        self._reverse_request_id = value
    @property
    def reverse_result(self):
        return self._reverse_result

    @reverse_result.setter
    def reverse_result(self, value):
        self._reverse_result = value
    @property
    def reverse_time(self):
        return self._reverse_time

    @reverse_time.setter
    def reverse_time(self, value):
        self._reverse_time = value
    @property
    def reverse_to_amount(self):
        return self._reverse_to_amount

    @reverse_to_amount.setter
    def reverse_to_amount(self, value):
        if isinstance(value, Money):
            self._reverse_to_amount = value
        else:
            self._reverse_to_amount = Money.from_alipay_dict(value)
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
        if self.reverse_from_amount:
            if hasattr(self.reverse_from_amount, 'to_alipay_dict'):
                params['reverse_from_amount'] = self.reverse_from_amount.to_alipay_dict()
            else:
                params['reverse_from_amount'] = self.reverse_from_amount
        if self.reverse_id:
            if hasattr(self.reverse_id, 'to_alipay_dict'):
                params['reverse_id'] = self.reverse_id.to_alipay_dict()
            else:
                params['reverse_id'] = self.reverse_id
        if self.reverse_quote:
            if hasattr(self.reverse_quote, 'to_alipay_dict'):
                params['reverse_quote'] = self.reverse_quote.to_alipay_dict()
            else:
                params['reverse_quote'] = self.reverse_quote
        if self.reverse_reason:
            if hasattr(self.reverse_reason, 'to_alipay_dict'):
                params['reverse_reason'] = self.reverse_reason.to_alipay_dict()
            else:
                params['reverse_reason'] = self.reverse_reason
        if self.reverse_reason_message:
            if hasattr(self.reverse_reason_message, 'to_alipay_dict'):
                params['reverse_reason_message'] = self.reverse_reason_message.to_alipay_dict()
            else:
                params['reverse_reason_message'] = self.reverse_reason_message
        if self.reverse_request_id:
            if hasattr(self.reverse_request_id, 'to_alipay_dict'):
                params['reverse_request_id'] = self.reverse_request_id.to_alipay_dict()
            else:
                params['reverse_request_id'] = self.reverse_request_id
        if self.reverse_result:
            if hasattr(self.reverse_result, 'to_alipay_dict'):
                params['reverse_result'] = self.reverse_result.to_alipay_dict()
            else:
                params['reverse_result'] = self.reverse_result
        if self.reverse_time:
            if hasattr(self.reverse_time, 'to_alipay_dict'):
                params['reverse_time'] = self.reverse_time.to_alipay_dict()
            else:
                params['reverse_time'] = self.reverse_time
        if self.reverse_to_amount:
            if hasattr(self.reverse_to_amount, 'to_alipay_dict'):
                params['reverse_to_amount'] = self.reverse_to_amount.to_alipay_dict()
            else:
                params['reverse_to_amount'] = self.reverse_to_amount
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
        o = AlipayOverseasRemitReverseNotifyModel()
        if 'pass_through_info' in d:
            o.pass_through_info = d['pass_through_info']
        if 'reverse_from_amount' in d:
            o.reverse_from_amount = d['reverse_from_amount']
        if 'reverse_id' in d:
            o.reverse_id = d['reverse_id']
        if 'reverse_quote' in d:
            o.reverse_quote = d['reverse_quote']
        if 'reverse_reason' in d:
            o.reverse_reason = d['reverse_reason']
        if 'reverse_reason_message' in d:
            o.reverse_reason_message = d['reverse_reason_message']
        if 'reverse_request_id' in d:
            o.reverse_request_id = d['reverse_request_id']
        if 'reverse_result' in d:
            o.reverse_result = d['reverse_result']
        if 'reverse_time' in d:
            o.reverse_time = d['reverse_time']
        if 'reverse_to_amount' in d:
            o.reverse_to_amount = d['reverse_to_amount']
        if 'transfer_request_id' in d:
            o.transfer_request_id = d['transfer_request_id']
        return o


