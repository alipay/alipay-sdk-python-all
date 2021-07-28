#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChargeItems import ChargeItems
from alipay.aop.api.domain.BillSendExtInfo import BillSendExtInfo
from alipay.aop.api.domain.UserDetails import UserDetails


class AlipayEcoEduKtBillingSendModel(object):

    def __init__(self):
        self._amount = None
        self._charge_bill_title = None
        self._charge_item = None
        self._charge_type = None
        self._child_name = None
        self._class_in = None
        self._end_enable = None
        self._ext_info = None
        self._gmt_end = None
        self._grade = None
        self._out_trade_no = None
        self._partner_id = None
        self._school_no = None
        self._school_pid = None
        self._student_code = None
        self._student_identify = None
        self._users = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def charge_bill_title(self):
        return self._charge_bill_title

    @charge_bill_title.setter
    def charge_bill_title(self, value):
        self._charge_bill_title = value
    @property
    def charge_item(self):
        return self._charge_item

    @charge_item.setter
    def charge_item(self, value):
        if isinstance(value, list):
            self._charge_item = list()
            for i in value:
                if isinstance(i, ChargeItems):
                    self._charge_item.append(i)
                else:
                    self._charge_item.append(ChargeItems.from_alipay_dict(i))
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def child_name(self):
        return self._child_name

    @child_name.setter
    def child_name(self, value):
        self._child_name = value
    @property
    def class_in(self):
        return self._class_in

    @class_in.setter
    def class_in(self, value):
        self._class_in = value
    @property
    def end_enable(self):
        return self._end_enable

    @end_enable.setter
    def end_enable(self, value):
        self._end_enable = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, BillSendExtInfo):
            self._ext_info = value
        else:
            self._ext_info = BillSendExtInfo.from_alipay_dict(value)
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def school_no(self):
        return self._school_no

    @school_no.setter
    def school_no(self, value):
        self._school_no = value
    @property
    def school_pid(self):
        return self._school_pid

    @school_pid.setter
    def school_pid(self, value):
        self._school_pid = value
    @property
    def student_code(self):
        return self._student_code

    @student_code.setter
    def student_code(self, value):
        self._student_code = value
    @property
    def student_identify(self):
        return self._student_identify

    @student_identify.setter
    def student_identify(self, value):
        self._student_identify = value
    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, value):
        if isinstance(value, list):
            self._users = list()
            for i in value:
                if isinstance(i, UserDetails):
                    self._users.append(i)
                else:
                    self._users.append(UserDetails.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.charge_bill_title:
            if hasattr(self.charge_bill_title, 'to_alipay_dict'):
                params['charge_bill_title'] = self.charge_bill_title.to_alipay_dict()
            else:
                params['charge_bill_title'] = self.charge_bill_title
        if self.charge_item:
            if isinstance(self.charge_item, list):
                for i in range(0, len(self.charge_item)):
                    element = self.charge_item[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.charge_item[i] = element.to_alipay_dict()
            if hasattr(self.charge_item, 'to_alipay_dict'):
                params['charge_item'] = self.charge_item.to_alipay_dict()
            else:
                params['charge_item'] = self.charge_item
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.child_name:
            if hasattr(self.child_name, 'to_alipay_dict'):
                params['child_name'] = self.child_name.to_alipay_dict()
            else:
                params['child_name'] = self.child_name
        if self.class_in:
            if hasattr(self.class_in, 'to_alipay_dict'):
                params['class_in'] = self.class_in.to_alipay_dict()
            else:
                params['class_in'] = self.class_in
        if self.end_enable:
            if hasattr(self.end_enable, 'to_alipay_dict'):
                params['end_enable'] = self.end_enable.to_alipay_dict()
            else:
                params['end_enable'] = self.end_enable
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.grade:
            if hasattr(self.grade, 'to_alipay_dict'):
                params['grade'] = self.grade.to_alipay_dict()
            else:
                params['grade'] = self.grade
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.school_no:
            if hasattr(self.school_no, 'to_alipay_dict'):
                params['school_no'] = self.school_no.to_alipay_dict()
            else:
                params['school_no'] = self.school_no
        if self.school_pid:
            if hasattr(self.school_pid, 'to_alipay_dict'):
                params['school_pid'] = self.school_pid.to_alipay_dict()
            else:
                params['school_pid'] = self.school_pid
        if self.student_code:
            if hasattr(self.student_code, 'to_alipay_dict'):
                params['student_code'] = self.student_code.to_alipay_dict()
            else:
                params['student_code'] = self.student_code
        if self.student_identify:
            if hasattr(self.student_identify, 'to_alipay_dict'):
                params['student_identify'] = self.student_identify.to_alipay_dict()
            else:
                params['student_identify'] = self.student_identify
        if self.users:
            if isinstance(self.users, list):
                for i in range(0, len(self.users)):
                    element = self.users[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.users[i] = element.to_alipay_dict()
            if hasattr(self.users, 'to_alipay_dict'):
                params['users'] = self.users.to_alipay_dict()
            else:
                params['users'] = self.users
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduKtBillingSendModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'charge_bill_title' in d:
            o.charge_bill_title = d['charge_bill_title']
        if 'charge_item' in d:
            o.charge_item = d['charge_item']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'child_name' in d:
            o.child_name = d['child_name']
        if 'class_in' in d:
            o.class_in = d['class_in']
        if 'end_enable' in d:
            o.end_enable = d['end_enable']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'grade' in d:
            o.grade = d['grade']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'school_no' in d:
            o.school_no = d['school_no']
        if 'school_pid' in d:
            o.school_pid = d['school_pid']
        if 'student_code' in d:
            o.student_code = d['student_code']
        if 'student_identify' in d:
            o.student_identify = d['student_identify']
        if 'users' in d:
            o.users = d['users']
        return o


