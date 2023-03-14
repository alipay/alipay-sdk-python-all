#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ImportSignerInfo(object):

    def __init__(self):
        self._import_fail_message = None
        self._import_status = None
        self._signer_notice_message = None
        self._staff_id = None

    @property
    def import_fail_message(self):
        return self._import_fail_message

    @import_fail_message.setter
    def import_fail_message(self, value):
        self._import_fail_message = value
    @property
    def import_status(self):
        return self._import_status

    @import_status.setter
    def import_status(self, value):
        self._import_status = value
    @property
    def signer_notice_message(self):
        return self._signer_notice_message

    @signer_notice_message.setter
    def signer_notice_message(self, value):
        self._signer_notice_message = value
    @property
    def staff_id(self):
        return self._staff_id

    @staff_id.setter
    def staff_id(self, value):
        self._staff_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.import_fail_message:
            if hasattr(self.import_fail_message, 'to_alipay_dict'):
                params['import_fail_message'] = self.import_fail_message.to_alipay_dict()
            else:
                params['import_fail_message'] = self.import_fail_message
        if self.import_status:
            if hasattr(self.import_status, 'to_alipay_dict'):
                params['import_status'] = self.import_status.to_alipay_dict()
            else:
                params['import_status'] = self.import_status
        if self.signer_notice_message:
            if hasattr(self.signer_notice_message, 'to_alipay_dict'):
                params['signer_notice_message'] = self.signer_notice_message.to_alipay_dict()
            else:
                params['signer_notice_message'] = self.signer_notice_message
        if self.staff_id:
            if hasattr(self.staff_id, 'to_alipay_dict'):
                params['staff_id'] = self.staff_id.to_alipay_dict()
            else:
                params['staff_id'] = self.staff_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ImportSignerInfo()
        if 'import_fail_message' in d:
            o.import_fail_message = d['import_fail_message']
        if 'import_status' in d:
            o.import_status = d['import_status']
        if 'signer_notice_message' in d:
            o.signer_notice_message = d['signer_notice_message']
        if 'staff_id' in d:
            o.staff_id = d['staff_id']
        return o


