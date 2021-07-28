#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VerifiedInfo(object):

    def __init__(self):
        self._application_no = None
        self._ext_info = None
        self._note = None
        self._remark = None
        self._status = None
        self._verified_by = None
        self._verify_date_time = None

    @property
    def application_no(self):
        return self._application_no

    @application_no.setter
    def application_no(self, value):
        self._application_no = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        self._note = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def verified_by(self):
        return self._verified_by

    @verified_by.setter
    def verified_by(self, value):
        self._verified_by = value
    @property
    def verify_date_time(self):
        return self._verify_date_time

    @verify_date_time.setter
    def verify_date_time(self, value):
        self._verify_date_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_no:
            if hasattr(self.application_no, 'to_alipay_dict'):
                params['application_no'] = self.application_no.to_alipay_dict()
            else:
                params['application_no'] = self.application_no
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.note:
            if hasattr(self.note, 'to_alipay_dict'):
                params['note'] = self.note.to_alipay_dict()
            else:
                params['note'] = self.note
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.verified_by:
            if hasattr(self.verified_by, 'to_alipay_dict'):
                params['verified_by'] = self.verified_by.to_alipay_dict()
            else:
                params['verified_by'] = self.verified_by
        if self.verify_date_time:
            if hasattr(self.verify_date_time, 'to_alipay_dict'):
                params['verify_date_time'] = self.verify_date_time.to_alipay_dict()
            else:
                params['verify_date_time'] = self.verify_date_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VerifiedInfo()
        if 'application_no' in d:
            o.application_no = d['application_no']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'note' in d:
            o.note = d['note']
        if 'remark' in d:
            o.remark = d['remark']
        if 'status' in d:
            o.status = d['status']
        if 'verified_by' in d:
            o.verified_by = d['verified_by']
        if 'verify_date_time' in d:
            o.verify_date_time = d['verify_date_time']
        return o


