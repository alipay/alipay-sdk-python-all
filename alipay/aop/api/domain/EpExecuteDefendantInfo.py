#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpExecuteDefendantInfo(object):

    def __init__(self):
        self._case_no = None
        self._case_register_date = None
        self._case_state = None
        self._execution_court = None
        self._performed_name = None
        self._zxbd = None
        self._zzjgdm = None

    @property
    def case_no(self):
        return self._case_no

    @case_no.setter
    def case_no(self, value):
        self._case_no = value
    @property
    def case_register_date(self):
        return self._case_register_date

    @case_register_date.setter
    def case_register_date(self, value):
        self._case_register_date = value
    @property
    def case_state(self):
        return self._case_state

    @case_state.setter
    def case_state(self, value):
        self._case_state = value
    @property
    def execution_court(self):
        return self._execution_court

    @execution_court.setter
    def execution_court(self, value):
        self._execution_court = value
    @property
    def performed_name(self):
        return self._performed_name

    @performed_name.setter
    def performed_name(self, value):
        self._performed_name = value
    @property
    def zxbd(self):
        return self._zxbd

    @zxbd.setter
    def zxbd(self, value):
        self._zxbd = value
    @property
    def zzjgdm(self):
        return self._zzjgdm

    @zzjgdm.setter
    def zzjgdm(self, value):
        self._zzjgdm = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_no:
            if hasattr(self.case_no, 'to_alipay_dict'):
                params['case_no'] = self.case_no.to_alipay_dict()
            else:
                params['case_no'] = self.case_no
        if self.case_register_date:
            if hasattr(self.case_register_date, 'to_alipay_dict'):
                params['case_register_date'] = self.case_register_date.to_alipay_dict()
            else:
                params['case_register_date'] = self.case_register_date
        if self.case_state:
            if hasattr(self.case_state, 'to_alipay_dict'):
                params['case_state'] = self.case_state.to_alipay_dict()
            else:
                params['case_state'] = self.case_state
        if self.execution_court:
            if hasattr(self.execution_court, 'to_alipay_dict'):
                params['execution_court'] = self.execution_court.to_alipay_dict()
            else:
                params['execution_court'] = self.execution_court
        if self.performed_name:
            if hasattr(self.performed_name, 'to_alipay_dict'):
                params['performed_name'] = self.performed_name.to_alipay_dict()
            else:
                params['performed_name'] = self.performed_name
        if self.zxbd:
            if hasattr(self.zxbd, 'to_alipay_dict'):
                params['zxbd'] = self.zxbd.to_alipay_dict()
            else:
                params['zxbd'] = self.zxbd
        if self.zzjgdm:
            if hasattr(self.zzjgdm, 'to_alipay_dict'):
                params['zzjgdm'] = self.zzjgdm.to_alipay_dict()
            else:
                params['zzjgdm'] = self.zzjgdm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpExecuteDefendantInfo()
        if 'case_no' in d:
            o.case_no = d['case_no']
        if 'case_register_date' in d:
            o.case_register_date = d['case_register_date']
        if 'case_state' in d:
            o.case_state = d['case_state']
        if 'execution_court' in d:
            o.execution_court = d['execution_court']
        if 'performed_name' in d:
            o.performed_name = d['performed_name']
        if 'zxbd' in d:
            o.zxbd = d['zxbd']
        if 'zzjgdm' in d:
            o.zzjgdm = d['zzjgdm']
        return o


