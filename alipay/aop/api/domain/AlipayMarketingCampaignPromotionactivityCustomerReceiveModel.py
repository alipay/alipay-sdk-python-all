#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignPromotionactivityCustomerReceiveModel(object):

    def __init__(self):
        self._activity_id = None
        self._apdid = None
        self._client_ip = None
        self._merchant_pid = None
        self._out_biz_no = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def apdid(self):
        return self._apdid

    @apdid.setter
    def apdid(self, value):
        self._apdid = value
    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.apdid:
            if hasattr(self.apdid, 'to_alipay_dict'):
                params['apdid'] = self.apdid.to_alipay_dict()
            else:
                params['apdid'] = self.apdid
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignPromotionactivityCustomerReceiveModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'apdid' in d:
            o.apdid = d['apdid']
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


