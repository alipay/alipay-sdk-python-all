#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalAqreportMsgSendModel(object):

    def __init__(self):
        self._biz_principal = None
        self._department = None
        self._hospital_name = None
        self._msg_create_time = None
        self._msg_modified_time = None
        self._out_biz_no = None
        self._report_name = None
        self._report_num = None
        self._report_time = None
        self._source_name = None
        self._template_code = None
        self._uscc = None
        self._user_card_no = None
        self._user_card_type = None
        self._user_phone_no = None

    @property
    def biz_principal(self):
        return self._biz_principal

    @biz_principal.setter
    def biz_principal(self, value):
        self._biz_principal = value
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def msg_create_time(self):
        return self._msg_create_time

    @msg_create_time.setter
    def msg_create_time(self, value):
        self._msg_create_time = value
    @property
    def msg_modified_time(self):
        return self._msg_modified_time

    @msg_modified_time.setter
    def msg_modified_time(self, value):
        self._msg_modified_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, value):
        self._report_name = value
    @property
    def report_num(self):
        return self._report_num

    @report_num.setter
    def report_num(self, value):
        self._report_num = value
    @property
    def report_time(self):
        return self._report_time

    @report_time.setter
    def report_time(self, value):
        self._report_time = value
    @property
    def source_name(self):
        return self._source_name

    @source_name.setter
    def source_name(self, value):
        self._source_name = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value
    @property
    def user_card_no(self):
        return self._user_card_no

    @user_card_no.setter
    def user_card_no(self, value):
        self._user_card_no = value
    @property
    def user_card_type(self):
        return self._user_card_type

    @user_card_type.setter
    def user_card_type(self, value):
        self._user_card_type = value
    @property
    def user_phone_no(self):
        return self._user_phone_no

    @user_phone_no.setter
    def user_phone_no(self, value):
        self._user_phone_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_principal:
            if hasattr(self.biz_principal, 'to_alipay_dict'):
                params['biz_principal'] = self.biz_principal.to_alipay_dict()
            else:
                params['biz_principal'] = self.biz_principal
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.msg_create_time:
            if hasattr(self.msg_create_time, 'to_alipay_dict'):
                params['msg_create_time'] = self.msg_create_time.to_alipay_dict()
            else:
                params['msg_create_time'] = self.msg_create_time
        if self.msg_modified_time:
            if hasattr(self.msg_modified_time, 'to_alipay_dict'):
                params['msg_modified_time'] = self.msg_modified_time.to_alipay_dict()
            else:
                params['msg_modified_time'] = self.msg_modified_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.report_name:
            if hasattr(self.report_name, 'to_alipay_dict'):
                params['report_name'] = self.report_name.to_alipay_dict()
            else:
                params['report_name'] = self.report_name
        if self.report_num:
            if hasattr(self.report_num, 'to_alipay_dict'):
                params['report_num'] = self.report_num.to_alipay_dict()
            else:
                params['report_num'] = self.report_num
        if self.report_time:
            if hasattr(self.report_time, 'to_alipay_dict'):
                params['report_time'] = self.report_time.to_alipay_dict()
            else:
                params['report_time'] = self.report_time
        if self.source_name:
            if hasattr(self.source_name, 'to_alipay_dict'):
                params['source_name'] = self.source_name.to_alipay_dict()
            else:
                params['source_name'] = self.source_name
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        if self.user_card_no:
            if hasattr(self.user_card_no, 'to_alipay_dict'):
                params['user_card_no'] = self.user_card_no.to_alipay_dict()
            else:
                params['user_card_no'] = self.user_card_no
        if self.user_card_type:
            if hasattr(self.user_card_type, 'to_alipay_dict'):
                params['user_card_type'] = self.user_card_type.to_alipay_dict()
            else:
                params['user_card_type'] = self.user_card_type
        if self.user_phone_no:
            if hasattr(self.user_phone_no, 'to_alipay_dict'):
                params['user_phone_no'] = self.user_phone_no.to_alipay_dict()
            else:
                params['user_phone_no'] = self.user_phone_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalAqreportMsgSendModel()
        if 'biz_principal' in d:
            o.biz_principal = d['biz_principal']
        if 'department' in d:
            o.department = d['department']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'msg_create_time' in d:
            o.msg_create_time = d['msg_create_time']
        if 'msg_modified_time' in d:
            o.msg_modified_time = d['msg_modified_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'report_num' in d:
            o.report_num = d['report_num']
        if 'report_time' in d:
            o.report_time = d['report_time']
        if 'source_name' in d:
            o.source_name = d['source_name']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'uscc' in d:
            o.uscc = d['uscc']
        if 'user_card_no' in d:
            o.user_card_no = d['user_card_no']
        if 'user_card_type' in d:
            o.user_card_type = d['user_card_type']
        if 'user_phone_no' in d:
            o.user_phone_no = d['user_phone_no']
        return o


