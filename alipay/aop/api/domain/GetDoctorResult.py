#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GetDoctorResult(object):

    def __init__(self):
        self._department = None
        self._desc = None
        self._head = None
        self._hospital = None
        self._name = None
        self._schedule = None
        self._title = None

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value
    @property
    def hospital(self):
        return self._hospital

    @hospital.setter
    def hospital(self, value):
        self._hospital = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, value):
        self._schedule = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.head:
            if hasattr(self.head, 'to_alipay_dict'):
                params['head'] = self.head.to_alipay_dict()
            else:
                params['head'] = self.head
        if self.hospital:
            if hasattr(self.hospital, 'to_alipay_dict'):
                params['hospital'] = self.hospital.to_alipay_dict()
            else:
                params['hospital'] = self.hospital
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.schedule:
            if hasattr(self.schedule, 'to_alipay_dict'):
                params['schedule'] = self.schedule.to_alipay_dict()
            else:
                params['schedule'] = self.schedule
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GetDoctorResult()
        if 'department' in d:
            o.department = d['department']
        if 'desc' in d:
            o.desc = d['desc']
        if 'head' in d:
            o.head = d['head']
        if 'hospital' in d:
            o.hospital = d['hospital']
        if 'name' in d:
            o.name = d['name']
        if 'schedule' in d:
            o.schedule = d['schedule']
        if 'title' in d:
            o.title = d['title']
        return o


