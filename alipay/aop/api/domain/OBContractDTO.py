#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OBContractDTO(object):

    def __init__(self):
        self._bid = None
        self._contract_no = None
        self._effective_time = None
        self._id = None
        self._lead_no = None
        self._ma_end_time = None
        self._ma_start_time = None

    @property
    def bid(self):
        return self._bid

    @bid.setter
    def bid(self, value):
        self._bid = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def lead_no(self):
        return self._lead_no

    @lead_no.setter
    def lead_no(self, value):
        self._lead_no = value
    @property
    def ma_end_time(self):
        return self._ma_end_time

    @ma_end_time.setter
    def ma_end_time(self, value):
        self._ma_end_time = value
    @property
    def ma_start_time(self):
        return self._ma_start_time

    @ma_start_time.setter
    def ma_start_time(self, value):
        self._ma_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.bid:
            if hasattr(self.bid, 'to_alipay_dict'):
                params['bid'] = self.bid.to_alipay_dict()
            else:
                params['bid'] = self.bid
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.effective_time:
            if hasattr(self.effective_time, 'to_alipay_dict'):
                params['effective_time'] = self.effective_time.to_alipay_dict()
            else:
                params['effective_time'] = self.effective_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.lead_no:
            if hasattr(self.lead_no, 'to_alipay_dict'):
                params['lead_no'] = self.lead_no.to_alipay_dict()
            else:
                params['lead_no'] = self.lead_no
        if self.ma_end_time:
            if hasattr(self.ma_end_time, 'to_alipay_dict'):
                params['ma_end_time'] = self.ma_end_time.to_alipay_dict()
            else:
                params['ma_end_time'] = self.ma_end_time
        if self.ma_start_time:
            if hasattr(self.ma_start_time, 'to_alipay_dict'):
                params['ma_start_time'] = self.ma_start_time.to_alipay_dict()
            else:
                params['ma_start_time'] = self.ma_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OBContractDTO()
        if 'bid' in d:
            o.bid = d['bid']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'effective_time' in d:
            o.effective_time = d['effective_time']
        if 'id' in d:
            o.id = d['id']
        if 'lead_no' in d:
            o.lead_no = d['lead_no']
        if 'ma_end_time' in d:
            o.ma_end_time = d['ma_end_time']
        if 'ma_start_time' in d:
            o.ma_start_time = d['ma_start_time']
        return o


