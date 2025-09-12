#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HonorLoanInfoDTO import HonorLoanInfoDTO


class HonorLendApplyResultDTO(object):

    def __init__(self):
        self._apply_no = None
        self._apply_status = None
        self._apply_time = None
        self._channel_customer_id = None
        self._institution_names = None
        self._loan_info = None
        self._loan_source = None
        self._out_order_no = None
        self._refuse_msg = None
        self._refuse_msg_data = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def channel_customer_id(self):
        return self._channel_customer_id

    @channel_customer_id.setter
    def channel_customer_id(self, value):
        self._channel_customer_id = value
    @property
    def institution_names(self):
        return self._institution_names

    @institution_names.setter
    def institution_names(self, value):
        self._institution_names = value
    @property
    def loan_info(self):
        return self._loan_info

    @loan_info.setter
    def loan_info(self, value):
        if isinstance(value, HonorLoanInfoDTO):
            self._loan_info = value
        else:
            self._loan_info = HonorLoanInfoDTO.from_alipay_dict(value)
    @property
    def loan_source(self):
        return self._loan_source

    @loan_source.setter
    def loan_source(self, value):
        self._loan_source = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def refuse_msg_data(self):
        return self._refuse_msg_data

    @refuse_msg_data.setter
    def refuse_msg_data(self, value):
        self._refuse_msg_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.channel_customer_id:
            if hasattr(self.channel_customer_id, 'to_alipay_dict'):
                params['channel_customer_id'] = self.channel_customer_id.to_alipay_dict()
            else:
                params['channel_customer_id'] = self.channel_customer_id
        if self.institution_names:
            if hasattr(self.institution_names, 'to_alipay_dict'):
                params['institution_names'] = self.institution_names.to_alipay_dict()
            else:
                params['institution_names'] = self.institution_names
        if self.loan_info:
            if hasattr(self.loan_info, 'to_alipay_dict'):
                params['loan_info'] = self.loan_info.to_alipay_dict()
            else:
                params['loan_info'] = self.loan_info
        if self.loan_source:
            if hasattr(self.loan_source, 'to_alipay_dict'):
                params['loan_source'] = self.loan_source.to_alipay_dict()
            else:
                params['loan_source'] = self.loan_source
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.refuse_msg:
            if hasattr(self.refuse_msg, 'to_alipay_dict'):
                params['refuse_msg'] = self.refuse_msg.to_alipay_dict()
            else:
                params['refuse_msg'] = self.refuse_msg
        if self.refuse_msg_data:
            if hasattr(self.refuse_msg_data, 'to_alipay_dict'):
                params['refuse_msg_data'] = self.refuse_msg_data.to_alipay_dict()
            else:
                params['refuse_msg_data'] = self.refuse_msg_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorLendApplyResultDTO()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'channel_customer_id' in d:
            o.channel_customer_id = d['channel_customer_id']
        if 'institution_names' in d:
            o.institution_names = d['institution_names']
        if 'loan_info' in d:
            o.loan_info = d['loan_info']
        if 'loan_source' in d:
            o.loan_source = d['loan_source']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'refuse_msg' in d:
            o.refuse_msg = d['refuse_msg']
        if 'refuse_msg_data' in d:
            o.refuse_msg_data = d['refuse_msg_data']
        return o


