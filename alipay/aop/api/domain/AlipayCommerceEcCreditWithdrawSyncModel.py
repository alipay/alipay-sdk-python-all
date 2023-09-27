#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BankOrderInfo import BankOrderInfo


class AlipayCommerceEcCreditWithdrawSyncModel(object):

    def __init__(self):
        self._alipay_pay_no = None
        self._enterprise_id = None
        self._ext_info = None
        self._fail_reason = None
        self._out_biz_no = None
        self._result = None

    @property
    def alipay_pay_no(self):
        return self._alipay_pay_no

    @alipay_pay_no.setter
    def alipay_pay_no(self, value):
        self._alipay_pay_no = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, BankOrderInfo):
            self._ext_info = value
        else:
            self._ext_info = BankOrderInfo.from_alipay_dict(value)
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_pay_no:
            if hasattr(self.alipay_pay_no, 'to_alipay_dict'):
                params['alipay_pay_no'] = self.alipay_pay_no.to_alipay_dict()
            else:
                params['alipay_pay_no'] = self.alipay_pay_no
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcCreditWithdrawSyncModel()
        if 'alipay_pay_no' in d:
            o.alipay_pay_no = d['alipay_pay_no']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'result' in d:
            o.result = d['result']
        return o


