#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantJobInfo(object):

    def __init__(self):
        self._active_tag = None
        self._job_group_name = None
        self._leads_name = None
        self._merchant_id = None
        self._woker_name = None

    @property
    def active_tag(self):
        return self._active_tag

    @active_tag.setter
    def active_tag(self, value):
        self._active_tag = value
    @property
    def job_group_name(self):
        return self._job_group_name

    @job_group_name.setter
    def job_group_name(self, value):
        self._job_group_name = value
    @property
    def leads_name(self):
        return self._leads_name

    @leads_name.setter
    def leads_name(self, value):
        self._leads_name = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def woker_name(self):
        return self._woker_name

    @woker_name.setter
    def woker_name(self, value):
        self._woker_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_tag:
            if hasattr(self.active_tag, 'to_alipay_dict'):
                params['active_tag'] = self.active_tag.to_alipay_dict()
            else:
                params['active_tag'] = self.active_tag
        if self.job_group_name:
            if hasattr(self.job_group_name, 'to_alipay_dict'):
                params['job_group_name'] = self.job_group_name.to_alipay_dict()
            else:
                params['job_group_name'] = self.job_group_name
        if self.leads_name:
            if hasattr(self.leads_name, 'to_alipay_dict'):
                params['leads_name'] = self.leads_name.to_alipay_dict()
            else:
                params['leads_name'] = self.leads_name
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.woker_name:
            if hasattr(self.woker_name, 'to_alipay_dict'):
                params['woker_name'] = self.woker_name.to_alipay_dict()
            else:
                params['woker_name'] = self.woker_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantJobInfo()
        if 'active_tag' in d:
            o.active_tag = d['active_tag']
        if 'job_group_name' in d:
            o.job_group_name = d['job_group_name']
        if 'leads_name' in d:
            o.leads_name = d['leads_name']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'woker_name' in d:
            o.woker_name = d['woker_name']
        return o


