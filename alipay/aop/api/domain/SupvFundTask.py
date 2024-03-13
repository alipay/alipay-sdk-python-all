#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupvFundTask(object):

    def __init__(self):
        self._fund_supv_task_id = None
        self._status = None
        self._supervised_desensitized_access_no = None
        self._supervised_id_number = None
        self._supervised_name = None
        self._supervised_special_account_no = None
        self._supv_agreement_no = None
        self._supv_end = None
        self._supv_start = None
        self._supvervisor_id_number = None
        self._supvervisor_name = None

    @property
    def fund_supv_task_id(self):
        return self._fund_supv_task_id

    @fund_supv_task_id.setter
    def fund_supv_task_id(self, value):
        self._fund_supv_task_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def supervised_desensitized_access_no(self):
        return self._supervised_desensitized_access_no

    @supervised_desensitized_access_no.setter
    def supervised_desensitized_access_no(self, value):
        self._supervised_desensitized_access_no = value
    @property
    def supervised_id_number(self):
        return self._supervised_id_number

    @supervised_id_number.setter
    def supervised_id_number(self, value):
        self._supervised_id_number = value
    @property
    def supervised_name(self):
        return self._supervised_name

    @supervised_name.setter
    def supervised_name(self, value):
        self._supervised_name = value
    @property
    def supervised_special_account_no(self):
        return self._supervised_special_account_no

    @supervised_special_account_no.setter
    def supervised_special_account_no(self, value):
        self._supervised_special_account_no = value
    @property
    def supv_agreement_no(self):
        return self._supv_agreement_no

    @supv_agreement_no.setter
    def supv_agreement_no(self, value):
        self._supv_agreement_no = value
    @property
    def supv_end(self):
        return self._supv_end

    @supv_end.setter
    def supv_end(self, value):
        self._supv_end = value
    @property
    def supv_start(self):
        return self._supv_start

    @supv_start.setter
    def supv_start(self, value):
        self._supv_start = value
    @property
    def supvervisor_id_number(self):
        return self._supvervisor_id_number

    @supvervisor_id_number.setter
    def supvervisor_id_number(self, value):
        self._supvervisor_id_number = value
    @property
    def supvervisor_name(self):
        return self._supvervisor_name

    @supvervisor_name.setter
    def supvervisor_name(self, value):
        self._supvervisor_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_supv_task_id:
            if hasattr(self.fund_supv_task_id, 'to_alipay_dict'):
                params['fund_supv_task_id'] = self.fund_supv_task_id.to_alipay_dict()
            else:
                params['fund_supv_task_id'] = self.fund_supv_task_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.supervised_desensitized_access_no:
            if hasattr(self.supervised_desensitized_access_no, 'to_alipay_dict'):
                params['supervised_desensitized_access_no'] = self.supervised_desensitized_access_no.to_alipay_dict()
            else:
                params['supervised_desensitized_access_no'] = self.supervised_desensitized_access_no
        if self.supervised_id_number:
            if hasattr(self.supervised_id_number, 'to_alipay_dict'):
                params['supervised_id_number'] = self.supervised_id_number.to_alipay_dict()
            else:
                params['supervised_id_number'] = self.supervised_id_number
        if self.supervised_name:
            if hasattr(self.supervised_name, 'to_alipay_dict'):
                params['supervised_name'] = self.supervised_name.to_alipay_dict()
            else:
                params['supervised_name'] = self.supervised_name
        if self.supervised_special_account_no:
            if hasattr(self.supervised_special_account_no, 'to_alipay_dict'):
                params['supervised_special_account_no'] = self.supervised_special_account_no.to_alipay_dict()
            else:
                params['supervised_special_account_no'] = self.supervised_special_account_no
        if self.supv_agreement_no:
            if hasattr(self.supv_agreement_no, 'to_alipay_dict'):
                params['supv_agreement_no'] = self.supv_agreement_no.to_alipay_dict()
            else:
                params['supv_agreement_no'] = self.supv_agreement_no
        if self.supv_end:
            if hasattr(self.supv_end, 'to_alipay_dict'):
                params['supv_end'] = self.supv_end.to_alipay_dict()
            else:
                params['supv_end'] = self.supv_end
        if self.supv_start:
            if hasattr(self.supv_start, 'to_alipay_dict'):
                params['supv_start'] = self.supv_start.to_alipay_dict()
            else:
                params['supv_start'] = self.supv_start
        if self.supvervisor_id_number:
            if hasattr(self.supvervisor_id_number, 'to_alipay_dict'):
                params['supvervisor_id_number'] = self.supvervisor_id_number.to_alipay_dict()
            else:
                params['supvervisor_id_number'] = self.supvervisor_id_number
        if self.supvervisor_name:
            if hasattr(self.supvervisor_name, 'to_alipay_dict'):
                params['supvervisor_name'] = self.supvervisor_name.to_alipay_dict()
            else:
                params['supvervisor_name'] = self.supvervisor_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupvFundTask()
        if 'fund_supv_task_id' in d:
            o.fund_supv_task_id = d['fund_supv_task_id']
        if 'status' in d:
            o.status = d['status']
        if 'supervised_desensitized_access_no' in d:
            o.supervised_desensitized_access_no = d['supervised_desensitized_access_no']
        if 'supervised_id_number' in d:
            o.supervised_id_number = d['supervised_id_number']
        if 'supervised_name' in d:
            o.supervised_name = d['supervised_name']
        if 'supervised_special_account_no' in d:
            o.supervised_special_account_no = d['supervised_special_account_no']
        if 'supv_agreement_no' in d:
            o.supv_agreement_no = d['supv_agreement_no']
        if 'supv_end' in d:
            o.supv_end = d['supv_end']
        if 'supv_start' in d:
            o.supv_start = d['supv_start']
        if 'supvervisor_id_number' in d:
            o.supvervisor_id_number = d['supvervisor_id_number']
        if 'supvervisor_name' in d:
            o.supvervisor_name = d['supvervisor_name']
        return o


