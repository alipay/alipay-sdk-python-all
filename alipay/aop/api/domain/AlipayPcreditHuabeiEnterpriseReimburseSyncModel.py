#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiEnterpriseReimburseSyncModel(object):

    def __init__(self):
        self._biz_reimburse_id = None
        self._end_date = None
        self._partner_id = None
        self._start_date = None
        self._status = None
        self._title = None
        self._user_id = None

    @property
    def biz_reimburse_id(self):
        return self._biz_reimburse_id

    @biz_reimburse_id.setter
    def biz_reimburse_id(self, value):
        self._biz_reimburse_id = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_reimburse_id:
            if hasattr(self.biz_reimburse_id, 'to_alipay_dict'):
                params['biz_reimburse_id'] = self.biz_reimburse_id.to_alipay_dict()
            else:
                params['biz_reimburse_id'] = self.biz_reimburse_id
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiEnterpriseReimburseSyncModel()
        if 'biz_reimburse_id' in d:
            o.biz_reimburse_id = d['biz_reimburse_id']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        if 'title' in d:
            o.title = d['title']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


