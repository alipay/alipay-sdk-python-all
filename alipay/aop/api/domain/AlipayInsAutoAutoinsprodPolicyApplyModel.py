#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliverInfo import DeliverInfo


class AlipayInsAutoAutoinsprodPolicyApplyModel(object):

    def __init__(self):
        self._agent_no = None
        self._bus_income_account_no = None
        self._deliver_info = None
        self._enquiry_biz_id = None
        self._force_income_account_no = None
        self._income_account_no = None
        self._quote_biz_id = None
        self._who_payed = None

    @property
    def agent_no(self):
        return self._agent_no

    @agent_no.setter
    def agent_no(self, value):
        self._agent_no = value
    @property
    def bus_income_account_no(self):
        return self._bus_income_account_no

    @bus_income_account_no.setter
    def bus_income_account_no(self, value):
        self._bus_income_account_no = value
    @property
    def deliver_info(self):
        return self._deliver_info

    @deliver_info.setter
    def deliver_info(self, value):
        if isinstance(value, DeliverInfo):
            self._deliver_info = value
        else:
            self._deliver_info = DeliverInfo.from_alipay_dict(value)
    @property
    def enquiry_biz_id(self):
        return self._enquiry_biz_id

    @enquiry_biz_id.setter
    def enquiry_biz_id(self, value):
        self._enquiry_biz_id = value
    @property
    def force_income_account_no(self):
        return self._force_income_account_no

    @force_income_account_no.setter
    def force_income_account_no(self, value):
        self._force_income_account_no = value
    @property
    def income_account_no(self):
        return self._income_account_no

    @income_account_no.setter
    def income_account_no(self, value):
        self._income_account_no = value
    @property
    def quote_biz_id(self):
        return self._quote_biz_id

    @quote_biz_id.setter
    def quote_biz_id(self, value):
        self._quote_biz_id = value
    @property
    def who_payed(self):
        return self._who_payed

    @who_payed.setter
    def who_payed(self, value):
        self._who_payed = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_no:
            if hasattr(self.agent_no, 'to_alipay_dict'):
                params['agent_no'] = self.agent_no.to_alipay_dict()
            else:
                params['agent_no'] = self.agent_no
        if self.bus_income_account_no:
            if hasattr(self.bus_income_account_no, 'to_alipay_dict'):
                params['bus_income_account_no'] = self.bus_income_account_no.to_alipay_dict()
            else:
                params['bus_income_account_no'] = self.bus_income_account_no
        if self.deliver_info:
            if hasattr(self.deliver_info, 'to_alipay_dict'):
                params['deliver_info'] = self.deliver_info.to_alipay_dict()
            else:
                params['deliver_info'] = self.deliver_info
        if self.enquiry_biz_id:
            if hasattr(self.enquiry_biz_id, 'to_alipay_dict'):
                params['enquiry_biz_id'] = self.enquiry_biz_id.to_alipay_dict()
            else:
                params['enquiry_biz_id'] = self.enquiry_biz_id
        if self.force_income_account_no:
            if hasattr(self.force_income_account_no, 'to_alipay_dict'):
                params['force_income_account_no'] = self.force_income_account_no.to_alipay_dict()
            else:
                params['force_income_account_no'] = self.force_income_account_no
        if self.income_account_no:
            if hasattr(self.income_account_no, 'to_alipay_dict'):
                params['income_account_no'] = self.income_account_no.to_alipay_dict()
            else:
                params['income_account_no'] = self.income_account_no
        if self.quote_biz_id:
            if hasattr(self.quote_biz_id, 'to_alipay_dict'):
                params['quote_biz_id'] = self.quote_biz_id.to_alipay_dict()
            else:
                params['quote_biz_id'] = self.quote_biz_id
        if self.who_payed:
            if hasattr(self.who_payed, 'to_alipay_dict'):
                params['who_payed'] = self.who_payed.to_alipay_dict()
            else:
                params['who_payed'] = self.who_payed
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsAutoAutoinsprodPolicyApplyModel()
        if 'agent_no' in d:
            o.agent_no = d['agent_no']
        if 'bus_income_account_no' in d:
            o.bus_income_account_no = d['bus_income_account_no']
        if 'deliver_info' in d:
            o.deliver_info = d['deliver_info']
        if 'enquiry_biz_id' in d:
            o.enquiry_biz_id = d['enquiry_biz_id']
        if 'force_income_account_no' in d:
            o.force_income_account_no = d['force_income_account_no']
        if 'income_account_no' in d:
            o.income_account_no = d['income_account_no']
        if 'quote_biz_id' in d:
            o.quote_biz_id = d['quote_biz_id']
        if 'who_payed' in d:
            o.who_payed = d['who_payed']
        return o


