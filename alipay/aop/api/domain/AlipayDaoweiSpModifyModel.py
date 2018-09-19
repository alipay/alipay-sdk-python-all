#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CalendarScheduleInfo import CalendarScheduleInfo
from alipay.aop.api.domain.LicenseInfo import LicenseInfo


class AlipayDaoweiSpModifyModel(object):

    def __init__(self):
        self._calendar_schedule = None
        self._cert_no = None
        self._cert_type = None
        self._desc = None
        self._license_list = None
        self._logon_id = None
        self._mobile = None
        self._name = None
        self._nick_name = None
        self._out_sp_id = None
        self._photo_url = None
        self._status = None

    @property
    def calendar_schedule(self):
        return self._calendar_schedule

    @calendar_schedule.setter
    def calendar_schedule(self, value):
        if isinstance(value, CalendarScheduleInfo):
            self._calendar_schedule = value
        else:
            self._calendar_schedule = CalendarScheduleInfo.from_alipay_dict(value)
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def license_list(self):
        return self._license_list

    @license_list.setter
    def license_list(self, value):
        if isinstance(value, list):
            self._license_list = list()
            for i in value:
                if isinstance(i, LicenseInfo):
                    self._license_list.append(i)
                else:
                    self._license_list.append(LicenseInfo.from_alipay_dict(i))
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def out_sp_id(self):
        return self._out_sp_id

    @out_sp_id.setter
    def out_sp_id(self, value):
        self._out_sp_id = value
    @property
    def photo_url(self):
        return self._photo_url

    @photo_url.setter
    def photo_url(self, value):
        self._photo_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.calendar_schedule:
            if hasattr(self.calendar_schedule, 'to_alipay_dict'):
                params['calendar_schedule'] = self.calendar_schedule.to_alipay_dict()
            else:
                params['calendar_schedule'] = self.calendar_schedule
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.license_list:
            if isinstance(self.license_list, list):
                for i in range(0, len(self.license_list)):
                    element = self.license_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.license_list[i] = element.to_alipay_dict()
            if hasattr(self.license_list, 'to_alipay_dict'):
                params['license_list'] = self.license_list.to_alipay_dict()
            else:
                params['license_list'] = self.license_list
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.out_sp_id:
            if hasattr(self.out_sp_id, 'to_alipay_dict'):
                params['out_sp_id'] = self.out_sp_id.to_alipay_dict()
            else:
                params['out_sp_id'] = self.out_sp_id
        if self.photo_url:
            if hasattr(self.photo_url, 'to_alipay_dict'):
                params['photo_url'] = self.photo_url.to_alipay_dict()
            else:
                params['photo_url'] = self.photo_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDaoweiSpModifyModel()
        if 'calendar_schedule' in d:
            o.calendar_schedule = d['calendar_schedule']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'license_list' in d:
            o.license_list = d['license_list']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'out_sp_id' in d:
            o.out_sp_id = d['out_sp_id']
        if 'photo_url' in d:
            o.photo_url = d['photo_url']
        if 'status' in d:
            o.status = d['status']
        return o


