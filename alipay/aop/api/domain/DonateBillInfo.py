#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DonateBillInfo(object):

    def __init__(self):
        self._donate_date = None
        self._donate_doorsill = None
        self._project_id = None
        self._project_title = None

    @property
    def donate_date(self):
        return self._donate_date

    @donate_date.setter
    def donate_date(self, value):
        self._donate_date = value
    @property
    def donate_doorsill(self):
        return self._donate_doorsill

    @donate_doorsill.setter
    def donate_doorsill(self, value):
        self._donate_doorsill = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def project_title(self):
        return self._project_title

    @project_title.setter
    def project_title(self, value):
        self._project_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.donate_date:
            if hasattr(self.donate_date, 'to_alipay_dict'):
                params['donate_date'] = self.donate_date.to_alipay_dict()
            else:
                params['donate_date'] = self.donate_date
        if self.donate_doorsill:
            if hasattr(self.donate_doorsill, 'to_alipay_dict'):
                params['donate_doorsill'] = self.donate_doorsill.to_alipay_dict()
            else:
                params['donate_doorsill'] = self.donate_doorsill
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.project_title:
            if hasattr(self.project_title, 'to_alipay_dict'):
                params['project_title'] = self.project_title.to_alipay_dict()
            else:
                params['project_title'] = self.project_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DonateBillInfo()
        if 'donate_date' in d:
            o.donate_date = d['donate_date']
        if 'donate_doorsill' in d:
            o.donate_doorsill = d['donate_doorsill']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_title' in d:
            o.project_title = d['project_title']
        return o


