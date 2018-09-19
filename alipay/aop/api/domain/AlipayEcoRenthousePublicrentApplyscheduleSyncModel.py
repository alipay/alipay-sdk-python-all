#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcoApplySchedule import EcoApplySchedule


class AlipayEcoRenthousePublicrentApplyscheduleSyncModel(object):

    def __init__(self):
        self._apply_schedule_list = None
        self._cert_no = None
        self._rent_id = None

    @property
    def apply_schedule_list(self):
        return self._apply_schedule_list

    @apply_schedule_list.setter
    def apply_schedule_list(self, value):
        if isinstance(value, list):
            self._apply_schedule_list = list()
            for i in value:
                if isinstance(i, EcoApplySchedule):
                    self._apply_schedule_list.append(i)
                else:
                    self._apply_schedule_list.append(EcoApplySchedule.from_alipay_dict(i))
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def rent_id(self):
        return self._rent_id

    @rent_id.setter
    def rent_id(self, value):
        self._rent_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_schedule_list:
            if isinstance(self.apply_schedule_list, list):
                for i in range(0, len(self.apply_schedule_list)):
                    element = self.apply_schedule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_schedule_list[i] = element.to_alipay_dict()
            if hasattr(self.apply_schedule_list, 'to_alipay_dict'):
                params['apply_schedule_list'] = self.apply_schedule_list.to_alipay_dict()
            else:
                params['apply_schedule_list'] = self.apply_schedule_list
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.rent_id:
            if hasattr(self.rent_id, 'to_alipay_dict'):
                params['rent_id'] = self.rent_id.to_alipay_dict()
            else:
                params['rent_id'] = self.rent_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthousePublicrentApplyscheduleSyncModel()
        if 'apply_schedule_list' in d:
            o.apply_schedule_list = d['apply_schedule_list']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'rent_id' in d:
            o.rent_id = d['rent_id']
        return o


