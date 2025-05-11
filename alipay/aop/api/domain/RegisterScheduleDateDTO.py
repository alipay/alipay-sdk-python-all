#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RegisterDoctorInfoDTO import RegisterDoctorInfoDTO


class RegisterScheduleDateDTO(object):

    def __init__(self):
        self._date = None
        self._doctor_info_list = None
        self._number_status = None
        self._register_date = None
        self._schedule_desc = None
        self._week_num = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def doctor_info_list(self):
        return self._doctor_info_list

    @doctor_info_list.setter
    def doctor_info_list(self, value):
        if isinstance(value, list):
            self._doctor_info_list = list()
            for i in value:
                if isinstance(i, RegisterDoctorInfoDTO):
                    self._doctor_info_list.append(i)
                else:
                    self._doctor_info_list.append(RegisterDoctorInfoDTO.from_alipay_dict(i))
    @property
    def number_status(self):
        return self._number_status

    @number_status.setter
    def number_status(self, value):
        self._number_status = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def schedule_desc(self):
        return self._schedule_desc

    @schedule_desc.setter
    def schedule_desc(self, value):
        self._schedule_desc = value
    @property
    def week_num(self):
        return self._week_num

    @week_num.setter
    def week_num(self, value):
        self._week_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.doctor_info_list:
            if isinstance(self.doctor_info_list, list):
                for i in range(0, len(self.doctor_info_list)):
                    element = self.doctor_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.doctor_info_list[i] = element.to_alipay_dict()
            if hasattr(self.doctor_info_list, 'to_alipay_dict'):
                params['doctor_info_list'] = self.doctor_info_list.to_alipay_dict()
            else:
                params['doctor_info_list'] = self.doctor_info_list
        if self.number_status:
            if hasattr(self.number_status, 'to_alipay_dict'):
                params['number_status'] = self.number_status.to_alipay_dict()
            else:
                params['number_status'] = self.number_status
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.schedule_desc:
            if hasattr(self.schedule_desc, 'to_alipay_dict'):
                params['schedule_desc'] = self.schedule_desc.to_alipay_dict()
            else:
                params['schedule_desc'] = self.schedule_desc
        if self.week_num:
            if hasattr(self.week_num, 'to_alipay_dict'):
                params['week_num'] = self.week_num.to_alipay_dict()
            else:
                params['week_num'] = self.week_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisterScheduleDateDTO()
        if 'date' in d:
            o.date = d['date']
        if 'doctor_info_list' in d:
            o.doctor_info_list = d['doctor_info_list']
        if 'number_status' in d:
            o.number_status = d['number_status']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'schedule_desc' in d:
            o.schedule_desc = d['schedule_desc']
        if 'week_num' in d:
            o.week_num = d['week_num']
        return o


