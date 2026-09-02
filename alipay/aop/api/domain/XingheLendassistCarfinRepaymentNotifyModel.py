#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BankCardSimpleInfo import BankCardSimpleInfo
from alipay.aop.api.domain.DrawdownInfo import DrawdownInfo


class XingheLendassistCarfinRepaymentNotifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._bank_card = None
        self._drawdown_info_list = None
        self._fail_code = None
        self._fail_msg = None
        self._notify_type = None
        self._org_drawdown_no_list = None
        self._out_apply_no = None
        self._out_repayment_no = None
        self._refund_status = None
        self._repayment_no = None
        self._repayment_status = None
        self._repayment_time = None
        self._repayment_total_amt = None
        self._repayment_type = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def bank_card(self):
        return self._bank_card

    @bank_card.setter
    def bank_card(self, value):
        if isinstance(value, BankCardSimpleInfo):
            self._bank_card = value
        else:
            self._bank_card = BankCardSimpleInfo.from_alipay_dict(value)
    @property
    def drawdown_info_list(self):
        return self._drawdown_info_list

    @drawdown_info_list.setter
    def drawdown_info_list(self, value):
        if isinstance(value, list):
            self._drawdown_info_list = list()
            for i in value:
                if isinstance(i, DrawdownInfo):
                    self._drawdown_info_list.append(i)
                else:
                    self._drawdown_info_list.append(DrawdownInfo.from_alipay_dict(i))
    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def fail_msg(self):
        return self._fail_msg

    @fail_msg.setter
    def fail_msg(self, value):
        self._fail_msg = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def org_drawdown_no_list(self):
        return self._org_drawdown_no_list

    @org_drawdown_no_list.setter
    def org_drawdown_no_list(self, value):
        if isinstance(value, list):
            self._org_drawdown_no_list = list()
            for i in value:
                self._org_drawdown_no_list.append(i)
    @property
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value
    @property
    def out_repayment_no(self):
        return self._out_repayment_no

    @out_repayment_no.setter
    def out_repayment_no(self, value):
        self._out_repayment_no = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def repayment_no(self):
        return self._repayment_no

    @repayment_no.setter
    def repayment_no(self, value):
        self._repayment_no = value
    @property
    def repayment_status(self):
        return self._repayment_status

    @repayment_status.setter
    def repayment_status(self, value):
        self._repayment_status = value
    @property
    def repayment_time(self):
        return self._repayment_time

    @repayment_time.setter
    def repayment_time(self, value):
        self._repayment_time = value
    @property
    def repayment_total_amt(self):
        return self._repayment_total_amt

    @repayment_total_amt.setter
    def repayment_total_amt(self, value):
        self._repayment_total_amt = value
    @property
    def repayment_type(self):
        return self._repayment_type

    @repayment_type.setter
    def repayment_type(self, value):
        self._repayment_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.bank_card:
            if hasattr(self.bank_card, 'to_alipay_dict'):
                params['bank_card'] = self.bank_card.to_alipay_dict()
            else:
                params['bank_card'] = self.bank_card
        if self.drawdown_info_list:
            if isinstance(self.drawdown_info_list, list):
                for i in range(0, len(self.drawdown_info_list)):
                    element = self.drawdown_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.drawdown_info_list[i] = element.to_alipay_dict()
            if hasattr(self.drawdown_info_list, 'to_alipay_dict'):
                params['drawdown_info_list'] = self.drawdown_info_list.to_alipay_dict()
            else:
                params['drawdown_info_list'] = self.drawdown_info_list
        if self.fail_code:
            if hasattr(self.fail_code, 'to_alipay_dict'):
                params['fail_code'] = self.fail_code.to_alipay_dict()
            else:
                params['fail_code'] = self.fail_code
        if self.fail_msg:
            if hasattr(self.fail_msg, 'to_alipay_dict'):
                params['fail_msg'] = self.fail_msg.to_alipay_dict()
            else:
                params['fail_msg'] = self.fail_msg
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.org_drawdown_no_list:
            if isinstance(self.org_drawdown_no_list, list):
                for i in range(0, len(self.org_drawdown_no_list)):
                    element = self.org_drawdown_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.org_drawdown_no_list[i] = element.to_alipay_dict()
            if hasattr(self.org_drawdown_no_list, 'to_alipay_dict'):
                params['org_drawdown_no_list'] = self.org_drawdown_no_list.to_alipay_dict()
            else:
                params['org_drawdown_no_list'] = self.org_drawdown_no_list
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
        if self.out_repayment_no:
            if hasattr(self.out_repayment_no, 'to_alipay_dict'):
                params['out_repayment_no'] = self.out_repayment_no.to_alipay_dict()
            else:
                params['out_repayment_no'] = self.out_repayment_no
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.repayment_no:
            if hasattr(self.repayment_no, 'to_alipay_dict'):
                params['repayment_no'] = self.repayment_no.to_alipay_dict()
            else:
                params['repayment_no'] = self.repayment_no
        if self.repayment_status:
            if hasattr(self.repayment_status, 'to_alipay_dict'):
                params['repayment_status'] = self.repayment_status.to_alipay_dict()
            else:
                params['repayment_status'] = self.repayment_status
        if self.repayment_time:
            if hasattr(self.repayment_time, 'to_alipay_dict'):
                params['repayment_time'] = self.repayment_time.to_alipay_dict()
            else:
                params['repayment_time'] = self.repayment_time
        if self.repayment_total_amt:
            if hasattr(self.repayment_total_amt, 'to_alipay_dict'):
                params['repayment_total_amt'] = self.repayment_total_amt.to_alipay_dict()
            else:
                params['repayment_total_amt'] = self.repayment_total_amt
        if self.repayment_type:
            if hasattr(self.repayment_type, 'to_alipay_dict'):
                params['repayment_type'] = self.repayment_type.to_alipay_dict()
            else:
                params['repayment_type'] = self.repayment_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinRepaymentNotifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'bank_card' in d:
            o.bank_card = d['bank_card']
        if 'drawdown_info_list' in d:
            o.drawdown_info_list = d['drawdown_info_list']
        if 'fail_code' in d:
            o.fail_code = d['fail_code']
        if 'fail_msg' in d:
            o.fail_msg = d['fail_msg']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'org_drawdown_no_list' in d:
            o.org_drawdown_no_list = d['org_drawdown_no_list']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        if 'out_repayment_no' in d:
            o.out_repayment_no = d['out_repayment_no']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'repayment_no' in d:
            o.repayment_no = d['repayment_no']
        if 'repayment_status' in d:
            o.repayment_status = d['repayment_status']
        if 'repayment_time' in d:
            o.repayment_time = d['repayment_time']
        if 'repayment_total_amt' in d:
            o.repayment_total_amt = d['repayment_total_amt']
        if 'repayment_type' in d:
            o.repayment_type = d['repayment_type']
        return o


