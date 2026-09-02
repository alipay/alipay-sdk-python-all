#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTelephoneReassignQueryModel(object):

    def __init__(self):
        self._agreement_no = None
        self._open_id = None
        self._pid_list = None
        self._target_uid = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pid_list(self):
        return self._pid_list

    @pid_list.setter
    def pid_list(self, value):
        if isinstance(value, list):
            self._pid_list = list()
            for i in value:
                self._pid_list.append(i)
    @property
    def target_uid(self):
        return self._target_uid

    @target_uid.setter
    def target_uid(self, value):
        self._target_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pid_list:
            if isinstance(self.pid_list, list):
                for i in range(0, len(self.pid_list)):
                    element = self.pid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pid_list[i] = element.to_alipay_dict()
            if hasattr(self.pid_list, 'to_alipay_dict'):
                params['pid_list'] = self.pid_list.to_alipay_dict()
            else:
                params['pid_list'] = self.pid_list
        if self.target_uid:
            if hasattr(self.target_uid, 'to_alipay_dict'):
                params['target_uid'] = self.target_uid.to_alipay_dict()
            else:
                params['target_uid'] = self.target_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTelephoneReassignQueryModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pid_list' in d:
            o.pid_list = d['pid_list']
        if 'target_uid' in d:
            o.target_uid = d['target_uid']
        return o


