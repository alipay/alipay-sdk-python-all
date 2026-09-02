#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfRecipestatusSyncModel(object):

    def __init__(self):
        self._account = None
        self._alipay_url = None
        self._aq_url = None
        self._event_time = None
        self._message = None
        self._order_id = None
        self._prescription_id = None
        self._record_id = None
        self._signin_form_id = None
        self._status = None
        self._status_desc = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def alipay_url(self):
        return self._alipay_url

    @alipay_url.setter
    def alipay_url(self, value):
        self._alipay_url = value
    @property
    def aq_url(self):
        return self._aq_url

    @aq_url.setter
    def aq_url(self, value):
        self._aq_url = value
    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def prescription_id(self):
        return self._prescription_id

    @prescription_id.setter
    def prescription_id(self, value):
        self._prescription_id = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def signin_form_id(self):
        return self._signin_form_id

    @signin_form_id.setter
    def signin_form_id(self, value):
        self._signin_form_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.alipay_url:
            if hasattr(self.alipay_url, 'to_alipay_dict'):
                params['alipay_url'] = self.alipay_url.to_alipay_dict()
            else:
                params['alipay_url'] = self.alipay_url
        if self.aq_url:
            if hasattr(self.aq_url, 'to_alipay_dict'):
                params['aq_url'] = self.aq_url.to_alipay_dict()
            else:
                params['aq_url'] = self.aq_url
        if self.event_time:
            if hasattr(self.event_time, 'to_alipay_dict'):
                params['event_time'] = self.event_time.to_alipay_dict()
            else:
                params['event_time'] = self.event_time
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.prescription_id:
            if hasattr(self.prescription_id, 'to_alipay_dict'):
                params['prescription_id'] = self.prescription_id.to_alipay_dict()
            else:
                params['prescription_id'] = self.prescription_id
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.signin_form_id:
            if hasattr(self.signin_form_id, 'to_alipay_dict'):
                params['signin_form_id'] = self.signin_form_id.to_alipay_dict()
            else:
                params['signin_form_id'] = self.signin_form_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfRecipestatusSyncModel()
        if 'account' in d:
            o.account = d['account']
        if 'alipay_url' in d:
            o.alipay_url = d['alipay_url']
        if 'aq_url' in d:
            o.aq_url = d['aq_url']
        if 'event_time' in d:
            o.event_time = d['event_time']
        if 'message' in d:
            o.message = d['message']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'prescription_id' in d:
            o.prescription_id = d['prescription_id']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'signin_form_id' in d:
            o.signin_form_id = d['signin_form_id']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        return o


