#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberCardVoucherBenefitEntity(object):

    def __init__(self):
        self._fail_reason_list = None
        self._success_voucher_list = None
        self._voucher_activity_id = None
        self._voucher_type = None

    @property
    def fail_reason_list(self):
        return self._fail_reason_list

    @fail_reason_list.setter
    def fail_reason_list(self, value):
        if isinstance(value, list):
            self._fail_reason_list = list()
            for i in value:
                self._fail_reason_list.append(i)
    @property
    def success_voucher_list(self):
        return self._success_voucher_list

    @success_voucher_list.setter
    def success_voucher_list(self, value):
        if isinstance(value, list):
            self._success_voucher_list = list()
            for i in value:
                self._success_voucher_list.append(i)
    @property
    def voucher_activity_id(self):
        return self._voucher_activity_id

    @voucher_activity_id.setter
    def voucher_activity_id(self, value):
        self._voucher_activity_id = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.fail_reason_list:
            if isinstance(self.fail_reason_list, list):
                for i in range(0, len(self.fail_reason_list)):
                    element = self.fail_reason_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fail_reason_list[i] = element.to_alipay_dict()
            if hasattr(self.fail_reason_list, 'to_alipay_dict'):
                params['fail_reason_list'] = self.fail_reason_list.to_alipay_dict()
            else:
                params['fail_reason_list'] = self.fail_reason_list
        if self.success_voucher_list:
            if isinstance(self.success_voucher_list, list):
                for i in range(0, len(self.success_voucher_list)):
                    element = self.success_voucher_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.success_voucher_list[i] = element.to_alipay_dict()
            if hasattr(self.success_voucher_list, 'to_alipay_dict'):
                params['success_voucher_list'] = self.success_voucher_list.to_alipay_dict()
            else:
                params['success_voucher_list'] = self.success_voucher_list
        if self.voucher_activity_id:
            if hasattr(self.voucher_activity_id, 'to_alipay_dict'):
                params['voucher_activity_id'] = self.voucher_activity_id.to_alipay_dict()
            else:
                params['voucher_activity_id'] = self.voucher_activity_id
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberCardVoucherBenefitEntity()
        if 'fail_reason_list' in d:
            o.fail_reason_list = d['fail_reason_list']
        if 'success_voucher_list' in d:
            o.success_voucher_list = d['success_voucher_list']
        if 'voucher_activity_id' in d:
            o.voucher_activity_id = d['voucher_activity_id']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


