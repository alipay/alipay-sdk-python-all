#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserTwostageIndirectUseModel(object):

    def __init__(self):
        self._dynamic_id = None
        self._org_pid = None
        self._pay_smid = None
        self._sence_no = None
        self._source_pid = None

    @property
    def dynamic_id(self):
        return self._dynamic_id

    @dynamic_id.setter
    def dynamic_id(self, value):
        self._dynamic_id = value
    @property
    def org_pid(self):
        return self._org_pid

    @org_pid.setter
    def org_pid(self, value):
        self._org_pid = value
    @property
    def pay_smid(self):
        return self._pay_smid

    @pay_smid.setter
    def pay_smid(self, value):
        self._pay_smid = value
    @property
    def sence_no(self):
        return self._sence_no

    @sence_no.setter
    def sence_no(self, value):
        self._sence_no = value
    @property
    def source_pid(self):
        return self._source_pid

    @source_pid.setter
    def source_pid(self, value):
        self._source_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.dynamic_id:
            if hasattr(self.dynamic_id, 'to_alipay_dict'):
                params['dynamic_id'] = self.dynamic_id.to_alipay_dict()
            else:
                params['dynamic_id'] = self.dynamic_id
        if self.org_pid:
            if hasattr(self.org_pid, 'to_alipay_dict'):
                params['org_pid'] = self.org_pid.to_alipay_dict()
            else:
                params['org_pid'] = self.org_pid
        if self.pay_smid:
            if hasattr(self.pay_smid, 'to_alipay_dict'):
                params['pay_smid'] = self.pay_smid.to_alipay_dict()
            else:
                params['pay_smid'] = self.pay_smid
        if self.sence_no:
            if hasattr(self.sence_no, 'to_alipay_dict'):
                params['sence_no'] = self.sence_no.to_alipay_dict()
            else:
                params['sence_no'] = self.sence_no
        if self.source_pid:
            if hasattr(self.source_pid, 'to_alipay_dict'):
                params['source_pid'] = self.source_pid.to_alipay_dict()
            else:
                params['source_pid'] = self.source_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserTwostageIndirectUseModel()
        if 'dynamic_id' in d:
            o.dynamic_id = d['dynamic_id']
        if 'org_pid' in d:
            o.org_pid = d['org_pid']
        if 'pay_smid' in d:
            o.pay_smid = d['pay_smid']
        if 'sence_no' in d:
            o.sence_no = d['sence_no']
        if 'source_pid' in d:
            o.source_pid = d['source_pid']
        return o


