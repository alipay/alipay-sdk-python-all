#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorLogoffResultDTO(object):

    def __init__(self):
        self._apply_no = None
        self._channel_customer_id = None
        self._logoff_err_desc = None
        self._logoff_status = None
        self._out_order_no = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def channel_customer_id(self):
        return self._channel_customer_id

    @channel_customer_id.setter
    def channel_customer_id(self, value):
        self._channel_customer_id = value
    @property
    def logoff_err_desc(self):
        return self._logoff_err_desc

    @logoff_err_desc.setter
    def logoff_err_desc(self, value):
        self._logoff_err_desc = value
    @property
    def logoff_status(self):
        return self._logoff_status

    @logoff_status.setter
    def logoff_status(self, value):
        self._logoff_status = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.channel_customer_id:
            if hasattr(self.channel_customer_id, 'to_alipay_dict'):
                params['channel_customer_id'] = self.channel_customer_id.to_alipay_dict()
            else:
                params['channel_customer_id'] = self.channel_customer_id
        if self.logoff_err_desc:
            if hasattr(self.logoff_err_desc, 'to_alipay_dict'):
                params['logoff_err_desc'] = self.logoff_err_desc.to_alipay_dict()
            else:
                params['logoff_err_desc'] = self.logoff_err_desc
        if self.logoff_status:
            if hasattr(self.logoff_status, 'to_alipay_dict'):
                params['logoff_status'] = self.logoff_status.to_alipay_dict()
            else:
                params['logoff_status'] = self.logoff_status
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorLogoffResultDTO()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'channel_customer_id' in d:
            o.channel_customer_id = d['channel_customer_id']
        if 'logoff_err_desc' in d:
            o.logoff_err_desc = d['logoff_err_desc']
        if 'logoff_status' in d:
            o.logoff_status = d['logoff_status']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        return o


