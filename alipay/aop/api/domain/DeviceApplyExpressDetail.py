#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceApplyExpressDetail(object):

    def __init__(self):
        self._express_time = None
        self._mail_no = None
        self._standard_desc = None
        self._status_desc = None

    @property
    def express_time(self):
        return self._express_time

    @express_time.setter
    def express_time(self, value):
        self._express_time = value
    @property
    def mail_no(self):
        return self._mail_no

    @mail_no.setter
    def mail_no(self, value):
        self._mail_no = value
    @property
    def standard_desc(self):
        return self._standard_desc

    @standard_desc.setter
    def standard_desc(self, value):
        self._standard_desc = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.express_time:
            if hasattr(self.express_time, 'to_alipay_dict'):
                params['express_time'] = self.express_time.to_alipay_dict()
            else:
                params['express_time'] = self.express_time
        if self.mail_no:
            if hasattr(self.mail_no, 'to_alipay_dict'):
                params['mail_no'] = self.mail_no.to_alipay_dict()
            else:
                params['mail_no'] = self.mail_no
        if self.standard_desc:
            if hasattr(self.standard_desc, 'to_alipay_dict'):
                params['standard_desc'] = self.standard_desc.to_alipay_dict()
            else:
                params['standard_desc'] = self.standard_desc
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
        o = DeviceApplyExpressDetail()
        if 'express_time' in d:
            o.express_time = d['express_time']
        if 'mail_no' in d:
            o.mail_no = d['mail_no']
        if 'standard_desc' in d:
            o.standard_desc = d['standard_desc']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        return o


